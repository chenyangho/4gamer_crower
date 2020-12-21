import sys
import requests as rq
from bs4 import BeautifulSoup

news_type = ["遊戲資訊", "硬體新聞", "影劇動漫", "玩具周邊", "電子競技", "深度專題", "實況直播", "展覽活動"]
game_news = []
hard_news = []
animate_news = []
toys_news = []
gaming_news = []
deep_project = []
live_news = []
event_news = []

def get_url(news_url, user_date):
	r = rq.get(news_url)
	if r.status_code == rq.codes.ok:
		soup = BeautifulSoup(r.text, "html.parser")
		news_url = soup.find_all("h4")
		for a in news_url:
			url = a.select_one("a").get("href")
			data_in_news(url, user_date)

def data_in_news(url, user_date):
	r = rq.get(url)
	if r.status_code == rq.codes.ok:
		soup = BeautifulSoup(r.text, "html.parser")
		# time
		time_in_data = soup.find("time")
		date = time_in_data.getText().split()[0]
		date_for_count = int(date[0:4] + date[5:7] + date[8:10])
		date_check(date_for_count, user_date)
		# type
		type_in_data = soup.find("p", class_="category").getText().strip()
		# title
		title_in_data = soup.find("h1").getText().strip()
		# img
		img_url = soup.find("img").get("src")
		# detail
		p_in_data = soup.find_all("p", limit=5)
		for word in p_in_data:
			text = word.getText().strip()
		check_type(date, type_in_data, title_in_data, url, img_url, text)

def date_check(post_time, user_date):
	if user_date > post_time:
		sys.exit()

def page_counter(user_date):
	news_url = "https://www.4gamers.com.tw/news"
	page_count = "?page="
	for i in range(1,3):
		if i == 1:
			get_url(news_url, user_date)
		else:
			get_url(news_url + page_count + str(i), user_date)

def check_type(date, type_in_data, title_in_data, url, img_url, text):
	if type_in_data == news_type[0]:
		game_news.append([date, type_in_data, title_in_data, url, img_url, text])
	elif type_in_data == news_type[1]:
		hard_news.append([date, type_in_data, title_in_data, url, img_url, text])
	elif type_in_data == news_type[2]:
		animate_news.append([date, type_in_data, title_in_data, url, img_url, text])
	elif type_in_data == news_type[3]:
		toys_news.append([date, type_in_data, title_in_data, url, img_url, text])
	elif type_in_data == news_type[4]:
		gaming_news.append([date, type_in_data, title_in_data, url, img_url, text])
	elif type_in_data == news_type[5]:
		deep_project.append([date, type_in_data, title_in_data, url, img_url, text])
	elif type_in_data == news_type[6]:
		live_news.append([date, type_in_data, title_in_data, url, img_url, text])
	elif type_in_data == news_type[7]:
		event_news.append([date, type_in_data, title_in_data, url, img_url, text])

if __name__	== '__main__':
	user_date = int(input("輸入終止日(ex : 20201221 ) : "))
	page_counter(user_date)