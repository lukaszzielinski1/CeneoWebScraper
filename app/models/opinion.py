from app.utils import get_item
from app.parameters import selectors

class Opinion:
    def __init__(self, product_id=0, author='', recommendation=None, stars=0, useful=0, useless=0, publish_date=None, purchase_date=None, pros=[], cons=[], content=''):
        self.product_id = product_id
        self.author = author
        self.reccomendation = recommendation
        self.stars = stars
        self.content = content
        self.useful = useful
        self.useless = useless
        self.publish_date = publish_date
        self.purchase_date = purchase_date
        self.pros = pros
        self.cons = cons 
        return self

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def to_dict(self):
        pass
    
    def extract_opinion(self,opinion):
        for key, value in selectors.items():
            setattr(self, key, get_item(opinion, *value))
        self.opinion_id = opinion
        ['data-entry-id']

        return self
        