import json
import requests as r
from urllib.parse import quote
from bs4 import BeautifulSoup 
import re as regex
import sys

def validWikiArticleLinkString(href):
    """ Takes a string and returns True if it contains the substring
        '/wiki/' in the beginning and does not contain any of the
        "special" wiki pages. 
    """
    return (href.find("/wiki/") == 0
            and href.find("(disambiguation)") == -1 
            and href.find("File:") == -1 
            and href.find("Wikipedia:") == -1
            and href.find("Portal:") == -1
            and href.find("Special:") == -1
            and href.find("Help:") == -1
            and href.find("(disambiguation)") == -1 
            and href.find("File:") == -1 
            and href.find("Wikipedia:") == -1
            and href.find("Portal:") == -1
            and href.find("Special:") == -1
            and href.find("Help:") == -1
            and href.find("Template_talk:") == -1
            and href.find("Template:") == -1
            and href.find("Talk:") == -1
            and href.find("Category:") == -1
            and href.find("Bibcode") == -1
            and href.find("Main_Page") == -1)

def first_valid_link(bsElements):
  try:
    for bsElement in bsElements:
      for link in bsElement.find_all('a'):
        if validWikiArticleLinkString(link['href']):
          return link
  except Exception as e:
    print("It leads to a dead end!")
    sys.exit()

def get_next_page(page):
  base_url = "https://en.wikipedia.org"
  url = f"{base_url}{page}"
  request = r.get(url)
  content = BeautifulSoup(request.text, 'html.parser')
  return first_valid_link(content.find("div", {'id':'bodyContent'}).find_all('p'))['href']

def main(in_page):
  print(in_page)
  first_page = f"/wiki/{quote(in_page)}"
  visited = set(first_page)
  num_visitadas = 0
  next_page = get_next_page(first_page)
  print(next_page.split('/')[-1])

  while next_page not in visited:
    page = next_page
    visited.add(page)
    next_page = get_next_page(page)
    num_visitadas += 1

    print(next_page.split('/')[-1])

    if next_page == "/wiki/Philosophy":
      print(f"{num_visitadas} roads from {in_page} to philosophy!")
      return 0

  print("It leads to an infinite loop!")
  return 0

if __name__ == "__main__":
  main(sys.argv[1])
