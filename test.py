import email
from imaplib import IMAP4_SSL

YA_HOST = "imap.yandex.ru"
YA_PORT = 993
YA_USER = open('login.txt').read()
YA_PASSWORD = open('pwd.txt').read()
SENDER = "Jag_K"

connection = IMAP4_SSL(host=YA_HOST, port=YA_PORT)
connection.login(user=YA_USER, password=YA_PASSWORD)
status, msgs = connection.select('INBOX')
assert status == 'OK'

typ, data = connection.search(None, 'FROM', '"%s"' % SENDER)
print(data)
for num in data[0].split():
    _, message_data = connection.fetch(num, '(RFC822)')
    mail = email.message_from_bytes(message_data[0][1])

    if mail.is_multipart():
        for part in mail.walk():
            content_type = part.get_content_type()
            filename = part.get_filename()
            if filename:
                # Нам плохого не надо, в письме может быть всякое барахло
                with open(part.get_filename(), 'wb') as new_file:
                    new_file.write(part.get_payload(decode=True))
connection.close()
connection.logout()
print('Done!')