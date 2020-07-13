# from grab import Grab
# g = Grab()
# g.go('https://www.ozon.ru/')
# res = g.doc.select('//div[contains(@class, "a0t6 a7b8")]')

# print(len(res))
# for i in range(0, len(res)):
#   print(res[i].text())

import sqlite3

from grab import Grab
from bs4 import BeautifulSoup as BSHTML
from urllib.request import urlopen
g = Grab()

connect = sqlite3.connect('db.db')
cursor = connect.cursor()

start = 5135079
end = 165068260

def get_code_img(str):
  str = str[::-1]
  new_str = ''
  for i in str:
    if i == '/':
      break
    new_str = i + new_str
  return new_str


def get_img(idx):
  images = soup.findAll('img')

  for image in images:
      #print image source
      if image['class'] == ['o5']:
        img = urlopen('https://cdn1.ozone.ru/multimedia/wc1200/' + get_code_img(image['src'])).read()
        str_id = get_code_img(image['src'])
        out = open("images/" + str_id, "wb")
        out.write(img)
        out.close

def get_name():
  hh1 = soup.find('h1', attrs={'class': 'a8m7'})
  return hh1.text

def get_prev_price():
  prev_cost = soup.findAll('span', attrs={'class': 'a8u9'})
  return prev_cost[0].text


page = urlopen('https://www.ozon.ru/context/detail/id/' + str(150641631))
soup = BSHTML(page, 'html.parser')
print(get_prev_price())
# print(get_name())

# for i in range(start, end):
#   try:
#     page = urlopen('https://www.ozon.ru/context/detail/id/' + str(i))
#     soup = BSHTML(page, "lxml")
#     print(get_name())
#     # print(get_prev_price())
#   except:
#       print('Not Page')


# g.go('https://www.ozon.ru/context/detail/id/' + str(start) + '/')
# res = g.doc.select('//h1[contains(@class, "a9k5")]')
# img = g.doc.select('//img[contains(@class, "a8p8 o5")]')

# print(res[0].text())
# print(img[0].html())

# for i in range(start, end):
#   g.go('https://www.ozon.ru/context/detail/id/' + str(i) + '/')
#   res = g.doc.select('//h1[contains(@class, "a9k5")]')
#   if len(res) != 0:
#     with connect:
#             cursor.execute("INSERT INTO `parser_data` (`item_id`, `name`) VALUES(?,?)", (1, res[0].text()))
#     print(res[0].text())
#     print('------------------------------------------')
#     # print(i)


# import xml.etree.ElementTree as ET
# tree = ET.parse('books.xml')
# root = tree.getroot()
