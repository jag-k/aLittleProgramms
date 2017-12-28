import imaplib
import email

mail = imaplib.IMAP4_SSL("imap.yandex.ru", 993)
mail.login(open('login.txt').read(), open('pwd.txt').read())
mail.list()

# Выводит список папок в почтовом ящике.
status, msgs = mail.select()  # Подключаемся к папке "входящие".
assert status == 'OK'

result, data = mail.search(None, 'FROM', '"Yandex Lyceum"')

print('start', end='\r', flush=True)
for latest_email_uid in data[0].split():
    result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email)
    email_m = email_message.EmailMessage()
    print(email_m.get_body())

    if 'Yandex Lyceum' in email_m:
        print('Msg: ')
        print(email_m.get_body())  # Выводит все заголовки.
