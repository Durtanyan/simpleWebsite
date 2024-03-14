from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('Первая страница сайта...')

def categories(requests):
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
