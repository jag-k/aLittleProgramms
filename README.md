# aLittlePrograms (ALP)
"Сборник" мини-програм
1. check_input(condition, res, prompt, prompt2):

    Проверяет введённые данные по заданым условиям

1. color(text, attributes, to_normal_end):
    
    Делает текст (`text`) цветным
    
    ###### подробнее на Wiki

1. colorClass.Color(text, attributes, to_normal_end):
    
    То же самое, что и `color`, только имеет больший функционал (Возможность добавлять/складывать со строками и с `Color`)
    
    ###### подробнее на Wiki

1. not_necessary(prompt):
    
    Возвращает `None`, если ввод был пустым

1. r_dictionary(word):
    
    Возвращает список со словарями
    
    ###### подробнее на Wiki

1. Reprint(title):

    Класс, при помощи которого можно перевыводить информацию.
    
    ###Внимание!! перевывод не работает одновременно с вводом (input() или sys.stdin)
    

1. rptint(values, sep, end, file):
    
    Выводит в консоль и записывает в файл этот же вывод)

1. select(title, *quest, numb, default, lang, inpt, out):
    
    Самая глобальная на данный момент функция. Имеет 2 режима работы:
        
    1. Выбор из списка 1 вариант
    2. Ответ Да/Нет (T/F) на `title`
    
    ###### подробнее на Wiki

1. speaker.Speak(text, file_format, quality, lang, speaker, speed, emotion, key):
    
    Преобразует текст в речь
    
    ###Внимание!! Для работы этой функции нужен файл `speakerKey.py` с параметром `KEY` внури
    
    ###### подробнее на Wiki

1. translate.en(text) / translate.ru(text):
    
    Переводит с иностранного языка на русский (`translate.ru(text)`) или на английский (`translate.en(text)`)
    
    ###Внимание!! Для работы этой функции нужен файл `translateApiKey.py` с параметром `apiKey` внури
    
    ###### подробнее на Wiki

1. UnixTime.py:
    
    Просто примеры "работы" с Unix временем)) (Вдруг кому-нибудь понадобится)
