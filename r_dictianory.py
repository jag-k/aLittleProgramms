from pprint import pprint


def r_dictionary(word):
    from urllib import request, parse
    word = word.replace('?', '%3F')
    raw_data = str(request.urlopen('http://gramota.ru/slovari/dic/?word=%s&all=x' % parse.quote_plus(word)).read(),
                   encoding='windows-1251').split('</form>')[1].split('<div class="gray">')[0]

    data = ''.join(filter(lambda x: x not in ['\n', '\t'], raw_data)
                   ).rstrip('<div class="clear"></div><div class="gap-saver"></div></div>').split('<h2>')
    l = []

    correct = True

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
            s = s.replace(before, after if decorate else '')
        return s

    for i in filter(lambda x: x, data):
        dic = {}
        if i.startswith('Искомое слово отсутствует'):
            correct = False
            continue

        elif not correct:
            for j in i.split('Похожие слова:</h2>')[1].split('<p style="padding-left:50px">'):
                dic = {}
                url, text = j.split('<a href="')[1].split('&all=x">')
                dic['url'] = url+'&all=x'
                dic['decorated_text'] = format_replace(text)
                dic['text'] = format_replace(text, False)
                l.append(dic)

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
            l.append(dic)

    return l
