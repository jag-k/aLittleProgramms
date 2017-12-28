def r_dictionary(word):
    from urllib import request, parse
    input_word = word
    word = input_word.replace('?', '%3F')
    link = 'http://gramota.ru/slovari/dic/?word=%s&all=x' % parse.quote_plus(word)
    req = request.urlopen(link)
    raw_data = str(req.read(),
                   encoding='windows-1251').split('</form>')[1].split('<div class="gray">')[0]

    data = ''.join(filter(lambda x: x not in ['\n', '\t'], raw_data)
                   ).rstrip('<div class="clear"></div><div class="gap-saver"></div></div>').split('<h2>')
    pre_res = {}
    res = {}

    dicts_name = {
        'Орфографический словарь': 'lop',
        'Большой толковый словарь': 'bts',
        'Управление в русском языке': 'rose',
        'Русское словесное ударение': 'zarva',
        'Словарь имён собственных': 'ag',
        'Словарь синонимов': 'abr',
        'Синонимы: краткий справочник': 'sqr',
        'Словарь антонимов': 'lv',
        'Словарь методических терминов': 'az',
        'Словарь русских имён': 'petr'
    }

    correct = True

    def remove_html_tags(s: str):
        return ' '.join(filter(lambda x: x, s.replace('<', '>').split('>')[::2]))


    def format_replace(s: str, decorate=True):
        r = [
            ('&mdash;', '—'),
            ('&ndash', '–'),
            (' <b>&loz;</b> ', ' ◊ '),
            ('<b>', '\x1b[1m'),
            ('<B>', '\x1b[1m'),
            ('<i>', ''),
            ('<I>', ''),
            ('<br>', '\n'),
            ('</b>', '\x1b[0m'),
            ('</i>', ''),
            ('</I>', ''),
            ('</div>', ''),
            ('<span class="accent">', '\x1b[31;1m'),
            ('</span>', '\x1b[1m')
        ]
        for before, after in r:
            s = s.replace(before, after if decorate else ('' if after.startswith('\x1b[') else after))
        return remove_html_tags(s).strip()

    for i in filter(lambda x: x, data):
        dic = {}
        if i.startswith('Искомое слово отсутствует'):
            correct = False
            continue

        elif not correct:
            l = []
            for j in filter(lambda x: x, i.split('Похожие слова:</h2>')[1].split('<p style="padding-left:50px">')):
                dic = {}
                url, text = j.split('<a href="')[1].split('&all=x">')
                dic['url'] = 'http://gramota.ru%s&all=x' % url
                dic['decorated_text'] = format_replace(text)
                dic['text'] = format_replace(text, False)
                l.append(dic)
            res['sim_world'] = l

        else:

            if i.startswith('Синонимы: краткий справочник</h2>'):
                dic['url'], name = None, i.replace('<h2>', '').replace('</h2>', '</a></h2>')
            else:
                dic['url'], name = i.replace('<a href="', '').split('/">')

            dic['name'], text = name.split('</a></h2><div style="padding-left:50px">')

            if text.startswith('искомое слово отсутствует'):
                dic['text'], dic['decorated_text'] = None, None
            else:
                dic['decorated_text'] = format_replace(text)
                dic['text'] = format_replace(text, False)
            pre_res[dicts_name[dic['name']]] = dic
    if not res:
        if not pre_res:
            return {'error': 1, 'msg': 'The word "%s" does not russian' % input_word}

        if 'lop' in pre_res and 'text' in pre_res and type(pre_res['lop']['text']) is str:
            res['word'] = pre_res['lop']['text'].split(',')[0]
            res['dicts'] = pre_res
            res['url'] = link
        else:
            return {'error': 2, 'msg': 'The word "%s" does not exist' % input_word}

    return res


if __name__ == '__main__':
    from pprint import pprint
    pprint(r_dictionary(input('Введите слово для проверки: ')))
