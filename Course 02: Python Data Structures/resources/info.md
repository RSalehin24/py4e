  ### type()
  ```
  to get the type of any variable or constrant:

  numOne = 1
  type(numOne)
  type('123')
  ```
  ## String
  ### length
  ```
  to get the length of string len():

  name = 'Reyan'
  length = len(name)
  ```
  ### slice
  ```
  name = 'Reyanus Salehin'

  first_name = name[0:7]   
  variable[x:y] - x is inclusive, y is exclusive

  y can be greater than the length of string like:
  last_name = name[8:50] 
  will give 'Salehin'; won't give any traceback (error)

  name[:3] -> index: 0 to 2: first to 2
  name[8:] -> index 8 to 15: 8 to last
  name[:] -> returns whole string
  ```
  ### in
  ```
  returns boolean

  searches substring or letter in a string:
  isPresent = first_name in name
  -> True
  rIsPresent = 'r' in name
  -> True
  ```
  ### comparison
  ```
  compares on ASCII code (relatively)

  if 'a' > 'A':
    return True
  if 'B' > 'R':
    return False
  if 'b' == 'b':
    return True

  lower case letters are greater than upper case letters, compare ASCII code. If the code is greater than it is greater otherwise, smaller.
  ```
  ### lower()
  ```
  name_lower = name.lower()
  lower_case = 'Hi there'.lower()
  returns name where all letters are in lower case 

  name_upper = name.upper()
  upper_case = 'hi there'.upper()
  returns name where all letters are in upper case
  ```
### string conversion
```
str() object class
```
### find()
```
takes an substring or letter and returns the index
index = name.find('R')  returns 0

for multiple, only returns the index of first one

returns -1 for 'not found'

name.find('a', 5)
returns the index of first 'a' found from index 5 to later part of the string
```
### replace()
```
takes two sub/strings/letters and replaces the first parameter with the second one

name = name.replace('Reyanus', 'Md. Reyanus')

replaces all instances that can be found
```
### lstrip() rstrp() strip()
```
removes the whitespaces from left: lstrip() and right: rstrip().

strip(): removes both

returns value after stripping
name = name.strip()
```

### startswith()
```
takes a string a letter and checks if the sting starts with it

returns boolean

name.startswith('R')
-> True
```
#### open()
```
parameters: 'filename', 'mode'

open() function opens a hanlder for the file. Which acts as an gateway or api to interact with the file.

file_handler = open('filename', 'mode')

we can get each line the file contains using a for loop:
    line_count = 0;
    for line in file_handler:
      print(line)
      line_count++


whole_file_content = file_handler.read()
character_count = len(whole_file_content)

Condition in for loop:

prints line which starts with 'From:' substring
    
    line_count = 0;
    for line in file_handler:
      line_count++
      line = line.rstrip()
      if line.startswith('From:') :
        print(line)


skips line which starts with 'From:' substring
    
    line_count = 0;
    for line in file_handler:
      line_count++
      line = line.rstrip()
      if line.startswith('From:') :
        continue
      print(line)


skips line which doesn't contain a specific 'sub_string' :

    line_count = 0;
    for line in file_handler:
      line_count++
      line = line.rstrip()
      if not 'sub_string' in linex :
        continue
      print(line)


taking a file_name from user, opening the file and counting the number of lines which starts with 'Subject:' substring in them:

    file_name = input('Enter a file name: ')
    file_handler = open(file_name)
    subject_line_count = 0
    for line in file_handler:
      line = line.rstrip()
      if line.startswith('Subject:') :
        subject_line_count++


handling exception in opening the file:

    file_name = input('Enter a file name: ')
    try:
      file_handler = open(file_name)
    except:
      print('File can be open:', file_name)
      quit()
    subject_line_count = 0
    for line in file_handler:
      line = line.rstrip()
      if line.startswith('Subject:') :
        subject_line_count++
```
### print() AND newline or '\n'
```
print() function prints a newline or adds '\n' after printing something

newline or '\n' is part of whitespace. For this, rstrip(), lstrip(), or strip() can be used to remove them
```
