file = open(r'/Users/venefica/Desktop/4f3ddcmt.txt', 'r')
text = file.read()
file.close()
start = '"EX Wavelength/EM Wavelength" '
len_start = len(start)
num = text.find(start)
print(num, len_start)
text = text[num + len_start:]
print(text)
text_list = text.split('\n')
text_list_len = len(text_list)
print(text_list)

rows = []
for i in range(text_list_len):
    rows.append(text_list[i].split(' '))
rows[0].insert(0, ' ')
rows_len = len(rows)
print(rows)


text_len = len(text)
text_int = ''
n = 0
for i in range(text_len):
    if text[i] == ',':
        text_int += text[n:i]
        n = i + 1
print(text_int)
text_int_list = text_int.split('\n')


text_int_list_len = len(text_int_list)
em_str = text_int_list[0].split(' ')
em_len = len(em_str)
em_wl =[]   #EM Wavelength
for i in range(em_len - 1):
    em_wl.append(int(em_str[i]))
print(em_wl)
em_wl_len = len(em_wl)
print(em_wl_len)
ex_wl = []
ex_wl_intensity = {}
for i in range(1, text_int_list_len):     #EX Wavelength
    temp_list = text_int_list[i].split(' ')
    temp_list_len = len(temp_list)
    key = int(temp_list[0])
    j = 1
    for j in range(temp_list_len):
        if temp_list[j] == '':
            continue
        data_element = int(temp_list[j])
        if key in ex_wl_intensity:
            ex_wl_intensity[key].append(data_element)
        else:
            ex_wl.append(key)
            ex_wl_intensity[key] = []
print(ex_wl)
ex_wl_len = len(ex_wl)
print(ex_wl_len)
print(ex_wl_intensity)

em_wl_intensity = {}
for i in range(em_wl_len):
    key = em_wl[i]
    em_wl.append(key)
    em_wl_intensity[key] = []
for i in range(em_wl_len):
    key = em_wl[i]
    for j in ex_wl:
        data_element = ex_wl_intensity[j][i]
        em_wl_intensity[key].append(data_element)
print(len(em_wl_intensity))
print(em_wl_intensity)

Z = []
for i in em_wl_intensity.values():
    Z.append(i)
print(len(Z))
print(Z)

Z_float = []
for i in Z:
    temp_z_list = []
    for j in i:
        elem = j / 1000
        temp_z_list.append(elem)
    Z_float.append(temp_z_list)
print(Z_float)
Z_float_len = len(Z_float)

data_for_dataframe = {}
for i in range(em_wl_len):
        data_for_dataframe[em_wl[i]] = Z_float[i]
print(data_for_dataframe)

max_z = []
min_z = []
for i in Z:
    for j in i:
        max_z.append(max(i))
        min_z.append(min(i))
print(max_z)
print(min_z)
print(max(max_z))
print(min(min_z))

def ex_extrems(d, key):
    ex_max = max(d[key])
    ex_min = min(d[key])
    index_max = d[key].index(ex_max)
    index_min = d[key].index(ex_min)
    em_max = em_wl[index_max]
    em_min = em_wl[index_min]
    ex_max = ex_max / 1000
    ex_min = ex_min / 1000
    return print(f'On EX Wavelength {key} nm:''\n' f'maximal intensity {ex_max} on EM Wavelength {em_max} nm''\n' f'minimal intensity {ex_min} on EM Wavelength {em_min} nm')
ex_extrems(ex_wl_intensity, 270)



def em_extrems(d, l, value):
    value_index = l.index(value)

#def absolut_extrems(d):

import csv
with open('/Users/venefica/Desktop/s_report_1', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for i in range(rows_len):
        writer.writerow(rows[i])
#report = open(r'/Users/venefica/Desktop/s_report_1', 'a')
