def song_text(name=None, input_file=None, is_print=True, output=None, sep='	—	',
              mode=['through_the_line', 'half'][0]):
    """
    Позволяет "красиво" вывести/записать в файл текст песни с переводом (например взятый с сайта amalgama-lab.com)

    :param name: Название композиции {'autor': *автор*, 'name': *название*} / *Название* (по умолчанию: нет)

    :param input_file: входные данные (по умолчанию: стандартный поток ввода)
    * Примечание: Если задан str, то будет разбита на строки; Если список, то каждый элемент будет считаться строкой;
    Если задан файл с правами на прочтение (open(*file_name*, mode='r')), то прочтение будет из этого файла

    :param is_print: Выводить ли что-либо (в том числе в файл) (по умолчанию выводит)

    :param output: вывод работы программы (по умолчанию: стандартный поток ввода)
    * Примечание: Если будет задана строка (название/путь к файлу) или файл с правами на запись
    (open(*file_name*, mode='w')), то результат будет в эом файле

    :param sep: разделитель между оригиналом и переводом

    :param mode: режим прочтения (по умолчанию: считывание "строка_оригинала-стока_перевода")
    * Примечание: Есть 2 режима считывания: "строка_оригинала-стока_перевода" ('through_the_line') и
    "половина_оригинал-половина_перевод" ('half')

    :return: Возвращает словарь с названием трека (при наличии), автором (при наличии) и готовым текстом
    """
    import sys, os
    if input_file is None:
        input_file = [i for i in sys.stdin]
    elif type(input_file) is str:
        if os.path.isfile(input_file):
            input_file = open(input_file).readlines()
        else:
            input_file = input_file.split('\n')
    else:
        input_file = input_file.readlines()

    s = list(map(lambda x: x.strip(), input_file))
    modes = ['through_the_line', 'half']
    res = {}
    if name is dict:
        if 'name' in name:
            res['name'] = name['name']
        elif 'author' in name:
            res['author'] = name['author']
    else:
        res['name'] = name

    original, translate = [], []

    if mode == modes[0]:
        shift = len(s) // 2
        for i in range(len(s) - 2):
            original.append(s[i])
            translate.append(s[i + shift])

    elif mode == modes[0]:
        for i in range(len(s) - 1, 2):
            original.append(s[i])
            translate.append(s[i + 1])
    else:
        raise ValueError

    res['orig'] = original[:]
    res['translate'] = translate[:]
    text = '\n'.join("%s%s%s" % (original[i], sep, translate[i]) if original[i] and translate[i] else '\n'
                     for i in range(len(original)))
    res['text'] = text

    if is_print:
        if type(output) is str:
            output = open(output, 'w')
        print(text, file=output)

    return res
