#!/usr/bin/env python3

import feedparser
import markdown
from datetime import datetime

def datetime_format(dttime):
	date_frame = '%a, %d %b %Y %H:%M:%S %z'
	datetime_obj = datetime.strptime(dttime, date_frame)
	return datetime_obj.strftime("%d/%m/%Y %H:%M:%S")

def make_markdown(url, title):
	data = feedparser.parse(url)
	text = "# G1 RSS - %s\n---\n" % title
	for n in data.entries:
		published = datetime_format(n.published)
		text += ('- %s: %s **[<span class="material-symbols-outlined">link</span>](%s)**\n' % (published, n.title, n.link))
	return text

def make_html(url, title):
	md = make_markdown(url, title)
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
	html = head + body
	with open(title+'.html', 'w+') as file:
		file.write(html)

def main():
	make_html('https://g1.globo.com/dynamo/rs/rio-grande-do-sul/rss2.xml', 'Rio Grande do Sul')
	make_html('https://g1.globo.com/dynamo/brasil/rss2.xml', 'Brasil')

if __name__ == '__main__':
	main()
