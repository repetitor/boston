from urllib.request import urlopen

html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
# print(html)

s = str(html)

options = dict()
# print(type(options))
pos = s.find('<code>')
len_code = 6
while pos != -1:
    pos_close_tag = s.find('</code>', pos + len_code)
    code_title = s[pos + len_code:pos_close_tag]
    if code_title in options:
        options[code_title] += 1
    else:
        options[code_title] = 1
    pos = s.find('<code>', pos_close_tag)


print(options)
max = 0
for k in options:
    if options[k] > max:
        max = options[k]

print('max - ', max)

for k2 in options:
    if options[k2] == 4:
        print(k2, end=' ')