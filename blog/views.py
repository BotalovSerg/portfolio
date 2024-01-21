from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return HttpResponse("""<html>
                        <title>Сайт Сергея Боталова</title>
                        <h1>Serg Botalov</h1>
                        </html>""")