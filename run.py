#!/usr/bin/env python3

import feedparser
import markdown
from datetime import datetime

def datetime_format(dttime):
	date_frame = '%a, %d %b %Y %H:%M:%S %z'
	datetime_obj = datetime.strptime(dttime, date_frame)
	return datetime_obj.strftime("%d/%m/%Y %H:%M:%S")

def make_markdown(data):
	text = "# G1 - Rio Grande do Sul\n---\n"
	for n in data.entries:
		published = datetime_format(n.published)
		text += ('- %s: %s **[<span class="material-symbols-outlined">link</span>](%s)**\n' % (published, n.title, n.link))
	return text

def make_html(md):
	head = '''
	<link rel="stylesheet" 
		href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" />
	<style>
		body {
			margin: 3%;
    		margin-left: 20%;
			font-family: "Times New Roman";
			font-size: 14pt;
		}
	</style>
	'''
	body = markdown.markdown(md)
	return (head + body)

def main():
	rs_news = feedparser.parse('https://g1.globo.com/dynamo/rs/rio-grande-do-sul/rss2.xml')
	md = make_markdown(rs_news)
	html = make_html(md)

	with open('G1RS.html', 'w+') as file:
		file.write(html)

if __name__ == '__main__':
	main()
