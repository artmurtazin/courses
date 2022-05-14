# import re
# from collections import defaultdict
# # with open('dataset_3380_5.txt', 'r') as inf:
# #     s = inf.read().strip()
# #     # print(s)
#
# dict = {}
# c = []
#
# with open('dataset_3380_5.txt') as file: #Читаем файл
#   for s in file:
#     s = file.read().strip().splitlines() # read().splitlines() - чтобы небыло пустых строк
#     #s2 = re.sub(r'(^[ \t]+|[ \t]+(?=:))', '', s, flags=re.M)
#
# for i, b in enumerate(s):
#   s[i] = b.replace('\t', ' ')
#   # s[i] = b.replace(',', ' ')
#
# # for i in s:
# #     i = i.split()
# #     c.append(i)
# # print(c)
#
# #
# # print(s)
# dict = defaultdict(lambda: s)
# for i in s:
#   # s2[i] = b.replace('\t', ' ')
#   print(i)
#   key, value1, value2 = i.split(' ')  # Разделяем каждую строку по двоеточии(в key будет - пицца, в value - 01)
#   dict[key].append([value1, value2])
#   # dict.update({key: [value1, value2]})
#
# print(s)
# print(dict)
#
# print(d['7'])


# with open('file.txt') as file: #Читаем файл
#   for s in file:
#     s = s.strip() # read().splitlines() - чтобы небыло пустых строк
#
#     s2 = re.sub("\s\s+", " ", s)
#     key, value1, value2 = s2.split(' ')  # Разделяем каждую строку по двоеточии(в key будет - пицца, в value - 01)
#     dict.update({key: [value1, value2]})

# print(s)
# dic = {} # Создаем пустой словарь
#
# for i in s: # Проходимся по каждой строчке
#   key, value1, value2 = i.split(' ') # Разделяем каждую строку по двоеточии(в key будет - пицца, в value - 01)
#   dic.update({key: [value1, value2]})	 # Добавляем в словарь
#
# print(dic) # Вывод словаря на консоль

# dic = {1 :[3, 2], 2:4}
#
# print(dic)

# import re
# s = "The   fox jumped   over    the log."
# s2 = re.sub("\s\s+" , " ", s)
#
# print(s2)





###############
# with open('dataset_3380_5.txt', 'r') as inf:
#     s = inf.read().strip()
#     s2 = re.sub(r'(^[ \t]+|[ \t]+(?=:))', '', s, flags=re.M)
#
# print('s = ')
# print(s)
# print('s2 = ')
# print(s2)


####################################### Код из интернета #################################
#
class_rawinfo = {}
#new_heights = 0
#new_students = 0
class_info = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
#class_info = []

with open('dataset_3380_5 (2).txt') as in_f_obj:
	for line in in_f_obj:
		#print(line)
		string = line.rstrip().split('\t')
		#print(string)
#n = int(input())
#for _ in range(n):
	#string = input().split('	')
		if string[0] not in class_rawinfo:
			class_rawinfo[string[0]] = [int(string[2]), 1]
		elif string[0] in class_rawinfo:
			heights = class_rawinfo[string[0]][0] + int(string[2])
			students = class_rawinfo[string[0]][1] + 1
			class_rawinfo[string[0]] = [heights, students]

for k, v in class_rawinfo.items():
	#print(k, str(v[0] / v[1]))
	#list.pop([int(k)-1])
	class_info[int(k)-1] = v[0] / v[1]
	#print(class_rawinfo)
	#print(class_info)

with open('03_07_05_output.txt', 'w') as out_f_obj:
	for i in range(len(class_info)):
		#print(i+1, str(class_info[i]))
		output = str(i+1) + ' ' + str(class_info[i]) + '\n'
		#print(output)
		out_f_obj.write(output)