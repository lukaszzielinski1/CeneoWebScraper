from app import app
from flask import redirect, render_template, url_for, filename
import os
import requests
from bs4 import BeautifulSoup
import json

def get_item(ancestor, selector, attribute=None, return_list=False):
    try:
        if return_list:
            return [item.get_text().strip() for item in ancestor.select(selector)]
        if attribute:
            return ancestor.select_one(selector)[attribute]
        return ancestor.select_one(selector).get_text().strip()
    except (AttributeError, TypeError):
        return None

selectors = {
    "author" : ['span.user-post__author-name'],
    "recomendation": ['span.user-post__author-recomendation > em'],
    "stars" : ['span.user-post__score-count'],
    "content" : ['div.user-post__text'],
    "useful" : ['span[id^="votes-yes"]'],
    "useless" : ['span[id^="votes-no"]'],
    "publish_date" : ['span.user-post__published > time:nth-child(1)', 'datetime'],
    "purchase_date" : ['span.user-post__published > time:nth-child(2)', 'datetime'],
    "pros" : ['div.review-feature__title--positives~ div.review-feature__item', None, True],
    "cons" : ['div.review-feature__title--negatives~ div.review-feature__item', None, True]
}

@app.route('/')
@app.route('/index')
@app.route('/index/<name>')
def index(name="Hello World"):
    return render_template("index.html.jinja", text=name)

@app.route('/extract')
def extract(product_id):
    url = f'https://www.ceneo.pl/{product_id}#tab=reviews'
    all_opinions = []
    while(url):

        response = requests.get(url)
        page = BeautifulSoup(response.text, 'html.parser')
        opinions = page.select('div.js_product-review')

        for opinion in opinions:

            single_opinion = {
                key:get_item(opinion,*value)
                    for key, value in selectors.items()
            }
            single_opinion['opinion_id'] = opinion['data-entry-id']
            all_opinions.append(single_opinion)

        try:
            url = f'https://www.ceneo.pl/{product_id}#tab=reviews'+get_item(page, 'a.pagination__next', 'href')
        except TypeError:
            url = None

        with open(f"opinions/{product_id}.json", "w", encoding="UTF-8") as file:
            json.dump(all_opinions, file, indent=4, ensure_ascii=False)
        return redirect(url_for('product',product_id))

@app.route('/products')
def products():
    products = [filename.split(".")[0] for filename in os.listdir("./opinions")]
    return render_template("products.html", products=products)

@app.route('/author')
def author():
    pass

@app.route('/product/<product_id>')
def product(product_id):
    pass