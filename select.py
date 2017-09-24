# -*-coding:utf8;-*-
# qpy:3
# qpy:console


def select(title="", *quest, numb=True, default=True, lang='eng'):
    if quest:
        print(title+':') if title else False
        for i in range(len(quest)):
            print('\t{}{}'.format(str(i+1)+') ' if numb else "", quest[i]+(';' if i != len(quest) else '.')))
        while True:
            t = input('1: ' if len(quest) == 1 else '1-'+str(len(quest))+': ')
            if t.isdigit():
                if 0 < int(t) < len(quest)+1:
                    return quest[int(t)-1]
    else:
        print(title, end=' ')
        if lang.lower() == 'eng' or lang.lower() == 'en':
            answer = '(Y/n)' if default else '(y/N)'
        elif lang.lower() == 'rus' or lang.lower() == 'ru':
            answer = '(Д/н)' if default else '(д/Н)'
        else:
            answer = '(Y/n)' if default else '(y/N)'
        while True:
            t = input(answer+': ')
            if not t:
                return default
            elif t:
                l = t.lower()
                if l == 'y' or l == 'yes' or l == 'д' or l == 'да':
                    return True
                elif l == 'n' or l == 'no' or l == 'н' or l == 'нет':
                    return False

'''
print(select('hate me?'))
print(select('hate me?', default=False))
print(select('question', 'do', 'you', 'hate', 'me?'))
print(select('question', 'do', 'you', 'hate', 'me?', numb=False))
print(select('question', 'do', numb=False))
print(select('question', 'do'))
'''