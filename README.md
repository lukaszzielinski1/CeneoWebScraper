# CeneoWebScraper


## Struktura opinii w serwisie Ceneo [Ceneo.pl](https://www.ceneo.pl/)

|Składowa|Selektor|Nazwa zmiennej|Typ zmiennej|
|--------|--------|--------------|------------|
|opinia|div.js_product-review|opinion|obj|
|indentyfikator opinii|div.js_product-review["data-entry-id"\]|opinion_id|int|
|autor opinii|span.user-post__author-name|author|str|
|rekomendacja|span.user-post__author-recomendation > em|recommendation|str|
|liczba gwiazdek|span.user-post__score_count|stars|str|
|treść opinii|div.user-post__text|content|str|
|lista zalet|div.review-feature__title--positives ~ div.review-feature__item|pros|list|
|lista wad|div.review-feature__title--negatives ~ div.review-feature__item|cons|list|
|dla ilu osób przydatna|buttton.vote-yes > span|useful|int|
|dla ilu osób nieprzydatna|buttton.vote-no > span|useless|int|
|data wystawienie opinii|span.user-post__published > time:nth-child(1)["datetime"]|publish_date|list|
|data zakupu|span.user-post__published > time:nth-child(2)["datetime"]|purchase_date|list|

## Etapy pracy nad projektem
1. Pobranie do pojedynczych zmiennych składowych pojedynczej opinii
2. Zapisanie wszystkich składowych pojedynczej opinii do słownika
3. Pobranie wszystkich opinii z pojedynczej strony do słowników i zapisanie ich liście
4. Zapisanie wszystkich opiinii z listy do pliku .json
5. Pobranie wszystkich opinii o produkcie i zapisanie ich na liście w postaci słowników
6. Dodanie możliwości podania kodu produktu przez użytkownika
7. Optymalizacja kodu
    a. utworzenie funkcji do ekstracji elementów strony
    b. utworzenie słownika selektorów
    c. użycie dictionary comprahansion do pobrania skladowych pojedynczej opinii na podstawie słownika selektorów
8. Analiza opinii produtku
    a. wyliczenie podstawowych statystyk 
        - liczba opinii
        - liczba opinii z zaletami 
        - liczba opinii z wadami
        - średnia ocena produktu
9. Zapisanie danych w pliku .json
10. Utworzenie wykresu opartego na danych



## Użyte biblioteki
|Biblioteka|Funkcja|
|----------|------------------|
|Beautiful Soup|Parsowanie plików html|
|Flask|Framework aplikacji webowych|
|matplotlib|Tworzenie wykresów|
|numpy|Tworzenie tabeli i list|
|pandas|Analiza  danych|
|requests|Obsługa HTTP |
|Markdown|Obsługa plików .md|
|pyplot|Tworzenie wykresów|