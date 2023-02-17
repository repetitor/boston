import xlrd3

rb = xlrd3.open_workbook('trekking1.xlsx')

# выбираем активный лист
sheet = rb.sheet_by_index(0)

# val = sheet.row_values(0)[0]


# получаем список значений из всех этих записей
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
vals.pop(0)
# i = 1
#
# medians = []
# d = dict()
# while i < len(vals):
#     line = vals[i][1:]
#     line.sort()
#     medians.append(line[3])
#     d[line[3]] = vals[i][0]
#     i += 1
#
#
# y = 1
# d2 = dict()
# avg_salaries = []
# while y < (sheet.ncols - 1):
#     salaries = sheet.col_values(y)[1:]
#     avg_salary = sum(salaries) / len(salaries)
#     avg_salaries.append(avg_salary)
#     d2[avg_salary] = sheet.col_values(y)[0]
#     y += 1
#
# print(d[max(medians)], d2[max(avg_salaries)])

sorted(vals, key=lambda x: (-x[1], x[0]))
for v in vals:
    print(v[0])

for i in range(7):
    print(i)
