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

  first_name = name[0:7]   variable[x:y] 
  x is inclusive, y is exclusive

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

  lower case letters are greater than upper case letters, but in between self, the Alphabetical order remains
  ```
  ### lower()
  ```
  name_lower = name.lower()
  lower_case = 'Hi there'.lower()
  returns name where all letters are in lower case 

  name_upper = name.upper()
  upper_case = 'hi there'.upper()
  returns name where all letters are in upper case
  ![String Methods](./images/string_builtin_methods.png)
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
returns the index of first 'a' found after index 5
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


