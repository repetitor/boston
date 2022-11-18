from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/209723/3.html') # скачиваем файл
html = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(html, 'html.parser') # делаем суп

sum = 0
for td in soup.find_all('td'):
    # sum += int(td.contents[0].strip())
    sum += int(td.text.strip()) # the same
print(sum)