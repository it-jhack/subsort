## Subsort - The Subdomain Redundancies Sorter.
This program removes subdomain redundancies and returns an optimized list. It saves A LOT of time when parsing large subdomain/dns files with grep.

## Why?
Because it can save you A LOT of time in some situations.

Suppose you have a 30 Gigabytes .json file full of DNS entries. If you grep for the lines containing the domain "example.com", next you don't need to parse for "sub.example.com" as the results of the latter will be contained in the results of the former.

## So what does it do, exactly?
You provide a .txt file containing  domains and subdomains and this program removes the subdomain redundancies, returning an optimized list, which can later be used by another tool such as grep.

So if you provide a .txt file as argument containing:
```
example.com
sub.example.com
another.example.com
test.com
sub.test.com
anothertest.com
```
Then, the application would return:
```
example.com
test.com
anothertest.com
```

## How to Run
Execute on your terminal:
```bash
python subsort.py -f subdomains_file.txt
```
Or you can also import it to your program:
```python
import subsort

subds_list = [
    'example.com',
    'sub.example.com',
    'sub2.example.com',
    'test.com',
    'sub.test.com',
    'anothertest.com',
]

new_list = []
new_list.extend(subsort.del_list_subds_redund(subds_list))

print(new_list)
```

## Requirements
Python 2.7 or higher
