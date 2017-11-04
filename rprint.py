def rptint(*values, sep=' ', end='\n', file=None):
    from select import select
    if file is not None:
        print(*values, sep=sep, end=end, file=file)
    else:
        text = sep.join(map(str, values))+end
        print(text)
        if select('\nЗаписать в файл?', lang='rus'):
            with open(input('Введите имя файла: '), 'r+') as file:
                read = file.read()
                if read:
                    file.write(read+'\n'+text)
                else:
                    file.write(text)
