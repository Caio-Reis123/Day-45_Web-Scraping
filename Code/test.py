from bs4 import BeautifulSoup as bs
import requests

response = requests.get('https://news.ycombinator.com/news')
yc_web_page = response.text

soup = bs(yc_web_page, 'html.parser')
# page_title = soup.title

articles = soup.find_all(name='a', class_='titlelink')
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)

article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name='span', class_='score')]

max_value = max(article_upvotes)
max_index = article_upvotes.index(max_value)

print(article_texts[max_index])
print(article_links[max_index])
print(article_upvotes[max_index])


















# with open('website.html', 'r', encoding='utf-8') as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')

# # print(soup.title)
# # print(soup.title.string)
# # print(soup.a)
# # print(soup.p)

# all_anchor_tags = soup.find_all(name='a')


# # for tag in all_anchor_tags:
# #     print(tag.getText())
# #     print(tag.get('href'))

# heading = soup.find(name='h1', id='name')
# # print(heading)

# section_heading = soup.find(name='h3', class_='heading')
# #print(section_heading.get_text())

# company_url = soup.select_one(selector='p a')
# print(company_url)