import datetime as dt

from config import smmry_api_key, news_api_key, mongo_db
from patholator import create_directories
from news_parser import dump_articles
from summarizer import summarize_articles
from translator import translate_summaries
from cleaner import clean_directories
from connect_mongo import send_to_db

today: dt.date = dt.date.today()
root_folder = str(today)

now_datetime: dt.datetime = dt.datetime.now() - dt.timedelta(hours=2)
past: str = (now_datetime - dt.timedelta(hours=24)
             ).replace(microsecond=0).isoformat()
now: str = now_datetime.replace(microsecond=0).isoformat()

all_china = '+China, +Chinese'
no_hunter = '+China, +Chinese, -Hunter'
no_covid = '+China, +Chinese, -COVID'
covid_no_bitcoin = '+China, +Chinese, COVID, -Bitcoin'
no_covid_no_bitcoin = '+China, +Chinese, -COVID, -Bitcoin'
no_covid_no_hunter_with_bitcoin = '+China, +Chinese, -COVID, -Hunter'


def checker() -> int:
    with open('./requests_left/file.txt', 'r', encoding='utf-8') as f:
        lines: list[str] = f.readlines()
    counter = 0
    requests_left = 0
    for line in reversed(lines):
        if line[0] == '[':
            try:
                requests_left = int(line[2:4])
            except ValueError:
                requests_left = int(line[2:3])
            break
        else:
            counter -= 1
    requests_left += counter
    return requests_left


if __name__ == '__main__':
    requests_left = checker()
    additional_number = 0
    while requests_left > 0:
        articles_number = requests_left+additional_number
        print(articles_number)
        create_directories(root_folder)
        dump_articles(past, now, root_folder, articles_number,
                      news_api_key, no_covid_no_hunter_with_bitcoin)
        summarize_articles(root_folder, smmry_api_key)
        translate_summaries(root_folder)
        send_to_db(root_folder, mongo_db)
        message: str = clean_directories(root_folder)
        print(f"{now} : {message}")
        requests_left = checker()
        additional_number += 20
        if additional_number > 100:
            break
