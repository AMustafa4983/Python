import yagmail


user = 'abdelrahman4983@gmail.com'
app_password = 'atmrxqilfxdaidef' # a token for gmail

File = open('mails.txt','r')
emails = File.readlines()
print(emails)

body = '''  I am a senior student in computer science school and I am interested in pursuing Artificial intelligence/data science.
            I am looking for a part-time/ full-time training or internship position at your institution. I welcome any ideas and I am looking forward to hearing from you at 
            My email: abdelrahman4983@gmail.com
            phone number: +201009697739
            Linkedin: https://www.linkedin.com/in/abdelrahman-mustafa-590701198/

            Sincerely
            Abdelrahman Mustafa
            Senior student school of computer science
            Zagazig university/ Egypt
        '''

subject = 'Looking for job opportunity'
content = [body,'Abdelrahman_Mohamed_Resume_softwareEngineer.pdf']

for to in emails:

    with yagmail.SMTP(user, app_password) as yag:
        yag.send(to, subject, content)
        print('Sent email successfully for {}'.format(to))