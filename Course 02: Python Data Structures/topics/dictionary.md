## Dictionary

### Declaration
```python
dictionary = dict()
dictionary['money'] = 12
dictionary['candy_count'] = 3

dictionary['candy_count'] += 7 

dictionary0 = {}
dictionary0['name'] = 'Reyanus Salehin'
```

### Find key in a dictionary
```python
present = 'name' in dictionary
# present will be false
present = 'name' in dictionary0
# present will be true
```

### Get()
> returns the value if the value is present or returns the default value given in the parameter
```python
dictionary['candy_count'] = dictionary0.get('candy_count', 0) + 1 

# will return the value of the key 'candy_count' (10) and if the 'candy-count' key was not present, it would have returned 0
 ```

### Transversing the dictionary
```python
dictionary = ['name': 'Reyan', 'age': 21, 'degree': 'BSc in SWE', 'varsity': 'IUT']

for key in dictionary:
  print(key, dictionary[key])

# will print the keys and the values for the keys side by side separated by space in new lines
```

### Converting to list()
> returns a list of the keys of the dictionary
```python
list_dict_keys = list(dictionary)
```

### dictionary.keys()
> returns a list of the keys of the dictionary
```python
list_of_keys = dictionary.key()
```

### dictionary.values()
> returns a list of the values of the dictionary
```python
list_of_values = dictionary.values()
```

### dictionary.items()
> returns each key-value pair as a tuple and returns all the tuples in a list
```python
list_tuples_of_key_value = dictionary.items()
```

### Iteration of dictionary.items()
```python
for key,value in dictionary.items():
  print(key, value) 
```

### Sort Dictionary by keys
> returns sorted list of tuples (sorted by key) 
```python
# tuples get sorted by the first element
sorted_dictionary = sorted(dictionary.items())
```

### Sorted Dictionary by values (High to low)
> returns sorted list of tuples (sorted by value)
```python
temp_list = list()

for key, value in dictionary.items():
  temp_list.append((value, key))

temp_list = sorted(temp_list, reverse=True) 

# shorter version
temp_list = sorted([(value, key) for key, value in dictionary.items()], reverse=True)
```