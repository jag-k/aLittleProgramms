from urllib import request, parse
from translateApiKey import apiKey  #https://translate.yandex.ru/developers/keys


def en(text):
    translate = request.urlopen('https://translate.yandex.net/api/v1.5/tr.json/translate?key={}&text={}&lang={}'.format(
        apiKey,
        parse.quote_plus(str(text)),
        'en'))
    return eval(str(translate.read(), encoding='utf-8'))


def ru(text):
    translate = request.urlopen('https://translate.yandex.net/api/v1.5/tr.json/translate?key={}&text={}&lang={}'.format(
        apiKey,
        parse.quote_plus(str(text)),
        'ru'))
    return eval(str(translate.read(), encoding='utf-8'))
