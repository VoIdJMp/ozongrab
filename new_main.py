import sqlite3

from grab import Grab
import re
from selenium.webdriver.common.by import By
g = Grab()

connect = sqlite3.connect('db.db')
cursor = connect.cursor()

start = 167802728
end   = 265068260

def get_code_img(str_html):
  p = re.compile('c50/(.*)" srcset')
  res = p.findall(str_html)
  return res[0]

def get_code_img_Z(str_html):
  p = re.compile('wc1200/(.*)" class')
  res = p.findall(str_html)
  return res[0]

def main_func():
  for i in range(start, end + 10):
    g.go('https://www.ozon.ru/context/detail/id/' + str(i) + '/')
    res = g.doc.select('//h1[contains(@class, "a8m7")]')
    cost = g.doc.select('//span[contains(@class, "a8u4 a8v7")]')
    cost_prev = g.doc.select('//span[contains(@class, "a8u9")]')
    tags = g.doc.select('//span[contains(@class, "a0b b5r7")]')
    tags_cont = g.doc.select('//a[contains(@class, "a0b b5r7")]')
    imgs_id = g.doc.select('//div[contains(@class, "b0b9")]')
    desc = g.doc.select('//div[contains(@class, "ra_a")]')
    if len(res) != 0 and res[0].text() != '':
      # print(res[0].text())
      cost1 = 0
      cost1_prev = 0
      status = 'В наличии'
      cur_tag = ''
      desc_cont = ''
      cur_img = ''
      if len(cost) != 0:
        cost1 = cost[0].text()
      else:
        status = 'Нет в наличии'
      if len(cost_prev) != 0:
        cost1_prev = cost_prev[0].text()
      if len(tags) != 0:
        for j in range(0, len(tags)):
          cur_tag += tags[j].text() + '/'
        if len(tags_cont) != 0:
          for j in range(0, len(tags_cont)):
            cur_tag += tags_cont[j].text() + '/'
      if len(imgs_id) != 0:
        for j in range(0, len(imgs_id)):
          #print(imgs_id[j].html())
          cur_img = cur_img + get_code_img(imgs_id[j].html()) + ','
      # if len(desc) != 0:
      #   desc_cont = desc[0].text()
      # print(desc_cont)
      # print(res[0].text())
      # print(cur_img)
      with connect:
        cursor.execute("INSERT INTO `parser_data` (`item_id`, `tags`, `name`, `images`, `cost`, `prev_cost`, `status`) VALUES(?,?,?,?,?,?,?)", (i, cur_tag, res[0].text(), cur_img, cost1, cost1_prev, status))
      # # # print('------------------------------------------')
      # print(i)

while True:
    try:
        main_func()
    except:
        print('Restart')

        #167802737