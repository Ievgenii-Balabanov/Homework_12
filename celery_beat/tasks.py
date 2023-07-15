import bs4
import django
import requests

from celery_beat.models import Author, Quote
from django.core.mail import send_mail
from celery import shared_task
from django.conf import settings

django.setup()


@shared_task
def add_five_quotes():
    BASE_URL = "https://quotes.toscrape.com"
    page_counter = 1
    quote_counter = 0
    quote_dict = {}

    while True:
        link = f"https://quotes.toscrape.com/page/{page_counter}"
        r = requests.get(link)
        soup = bs4.BeautifulSoup(r.text, "html.parser")
        all_quotes = soup.find_all("div", class_="quote")

        if not soup("span", class_="text"):
            send_mail(
                "Quotes are missing!",
                "There is no any available quotes for you!",
                settings.NOREPLY_EMAIL,
                ["test@noreply.com"],
                fail_silently=False,
            )
            return

        for quote in all_quotes:
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text
            author_link = quote.find("a").get("href")

            # if Author.objects.filter(author=author).exists():
            #     continue
            # else:
            if not Author.objects.filter(author=author).exists():
                author_detail = requests.get(BASE_URL + author_link)
                soup = bs4.BeautifulSoup(author_detail.text, "html.parser")
                page_detail = soup.find_all("div", class_="author-details")

                for item in page_detail:
                    # name = item.find("h3", class_="author-title").text
                    birth_date = item.find("span", class_="author-born-date").text
                    place_of_birth = item.find("span", class_="author-born-location").text
                    description = item.find("div", class_="author-description").text

                    Author.objects.create(
                        author=author, birth_date=birth_date, hometown=place_of_birth, description=description
                    )

            author = Author.objects.get(author=author)
            if not Quote.objects.filter(quote=text).exists():
                quote_dict[text]: author.id
                Quote.objects.create(quote=text, author=author)
                quote_counter += 1
                if quote_counter == 5:
                    print(quote_dict)
                    break

        page_counter += 1

        if quote_counter == 5:
            send_mail(
                "Success!",
                "5 new quotes are successfully added!",
                settings.NOREPLY_EMAIL,
                ["test@noreply.com"],
                fail_silently=False,
            )
            break
