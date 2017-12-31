from translateApiKey import apiKey  # https://translate.yandex.ru/developers/keys

class Translate:
    def __init__(self, text, default_lang='en', from_lang=None, api=apiKey):
        from urllib import parse
        self.text = parse.quote_plus(str(text))
        self.api = api
        self.from_lang = from_lang
        self.default_lang = default_lang

    def __getattr__(self, to_lang):
        from urllib import request
        import json
        lang = filter(lambda x: x is not None, [to_lang, self.from_lang])
        url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key=%s&text=%s&lang=%s' % (self.api, self.text,
                                                                                                  '-'.join(lang))
        tran = request.urlopen(url)
        return json.loads(str(tran.read(), encoding='utf-8'))

    def __str__(self):
        return '\n'.join(eval("self." + self.default_lang)['text'])


if __name__ == '__main__':
    t = Translate(input('Введите слово для перевода: ').replace('\\n', '\n'))
    print(t)
