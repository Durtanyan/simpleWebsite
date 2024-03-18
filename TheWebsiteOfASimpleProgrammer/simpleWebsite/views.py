from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

def index(request):
	return HttpResponse('Первая страница сайта...')

def categories(requests, cat_id):
	return HttpResponse("""<!DOCTYPE html>
		<html lang="ru">
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<title>Ты ж программист...</title>
		</head>
		<body>
			<h1>Вторая страница сайта...</h1>
		</body>
		</html>""")

def categories_by_slug(requests, cat_slug):
	if requests.GET:
		print(requests.GET)
	return HttpResponse("""<!DOCTYPE html>
		<html lang="ru">
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<title>Ты ж программист...</title>
		</head>
		<body>
			<h1>Третья страница сайта...</h1>
		</body>
		</html>""")

def archive(requests, year):
	if year > 2023:
		raise Http404()
	return HttpResponse("""
		<!DOCTYPE html>
		<html lang="ru">
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<title>Ты ж программист...</title>
		</head>
		<body>
			<h1>Четвертая страница сайта...</h1>
		</body>
		</html>
		""")

def page_not_found(requests, exception):
	return HttpResponseNotFound('<h1>Вашпе нет такой страницы...</h1>')