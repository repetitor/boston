from urllib.request import urlopen

html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode('utf-8')
# print(html)

s = str(html)
print('py - ', s.count('Python'))
print('cpp - ', s.count('C++'))
