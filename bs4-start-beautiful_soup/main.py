from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_span = soup.find_all("span", class_="titleline")

anchor_list = [span.find("a")for span in article_span]

article_text = [anchor.getText() for anchor in anchor_list]
article_link = [anchor.get("href") for anchor in anchor_list]

article_upvote = [int(scores.getText().split()[0]) for scores in soup.find_all("span", class_="score")]

highest_index = (article_upvote.index(max(article_upvote)))

print(article_text[highest_index])
print(article_link[highest_index])
print(article_upvote[highest_index])























# import lxml
#
# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
#
# # print(soup.prettify())
#
# # print(soup.p)
#
# # print(soup.a)
#
# # all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
# #
# # for tag in all_anchor_tags:
# #     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
#
# company_url = soup.select_one(selector="p a")
# print(company_url.get("href"))
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)
