def r_dictionary(word):
    from urllib import request, parse

    raw_data = str(request.urlopen('http://gramota.ru/slovari/dic/?word=%s&all=x' % parse.quote_plus(word)).read(),
                   encoding='windows-1251').split('</form>')[1].split('<div class="gray">')[0]

    data = ''.join(filter(lambda x: x not in ['\n', '\t'], raw_data)
                   ).rstrip('<div class="clear"></div><div class="gap-saver"></div></div>').split('<h2>')
    l = []

    def format_replace(s: str):
        s = s.replace('<br>', '\n').replace(' <b>&loz;</b> ', ' ◊ ').replace('<b>', '\x1b[1m')
        s = s.replace('</b>', '\x1b[0m').replace('<i>', '').replace('</i>', '').replace('</div>', '')
        s = s.replace('&mdash;', '—').replace('<span class="accent">', '\x1b[31;1m').replace('</span>', '\x1b[1m')
        return s

    for i in filter(lambda x: x, data):
        dic = {}
        if i.startswith('Синонимы: краткий справочник</h2>'):
            dic['url'], name = None, i.replace('<h2>', '').replace('</h2>', '</a></h2>')
        else:
            dic['url'], name = i.replace('<a href="', '').split('/">')

        dic['name'], text = name.split('</a></h2><div style="padding-left:50px">')

        if text in ('искомое слово отсутствует</div>', 'искомое слово отсутствует'):
            dic['text'] = None
        else:
            dic['text'] = format_replace(text)
        l.append(dic)

    return l
