import urllib.request
import os
#  beautiful soup used to parse xml
from bs4 import BeautifulSoup

# custom modules
import subprocess
import hotword
import speak

# backup if RSS feed unavailable
back_up_file_name = "/home/pi/2019-ca400-randlea2/src/command_scripts/sports/sports_backup.txt"

def get_sports():
    # get rte rss news feed
    xml_request = urllib.request.urlopen("https://www.rte.ie/feeds/rss/?index=/sport/&limit=20")
    news_headlines = parse_xml(xml_request)
    news_headlines =  news_headlines.replace("'","")
    return news_headlines



def parse_xml(xml):
    # italise xml parser
    xml_parser = BeautifulSoup(xml, features="lxml")
    # each article is an item
    items = xml_parser.find_all("item")
    first_five_items = items[:5]
    first_five_articles = []
    # iterate items to grab article title
    for article in first_five_items:
        first_five_articles.append(article.title.text)
    # join article titles by newline character
    first_five_article_titles = "\n".join(first_five_articles)
    # create news backup
    backup_file = open(back_up_file_name, "w")
    backup_file.write(first_five_article_titles)
    return first_five_article_titles


def current_sports_unavailable():
    # rss feed unavailable, backup will be used
    back_up_file = open(back_up_file_name, "r")
    return back_up_file.read()


def main():
    sports = get_sports()
    # speak in background while listening for hotword
    speak.speak_to_user(sports, background=True)
    hotword.detect_hotword()

if __name__ == "__main__":
    main()