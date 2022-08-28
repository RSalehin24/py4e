import re
import os

file_name_sample = os.getcwd() + '/Course 03: Using Python to access Web Data/assignments/assignment.2.01.sample.data.txt'
file_name_real = os.getcwd() + '/Course 03: Using Python to access Web Data/assignments/assignment.2.01.real.data.txt'

file_handler = open(file_name_real)

number_list = []
total = 0

for line in file_handler:
  line_num_list = re.findall('[0-9]+', line)
  if len(line_num_list) > 0:
    for num in line_num_list:
      number_list.append(num)

for num_string in number_list:
  total += int(num_string)

print(total)
