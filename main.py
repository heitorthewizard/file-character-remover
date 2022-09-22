file_name = input('Enter file name: ')
new_file_name = input("Name the new file: ")
items_list = list()

print('Add "-0" when you are done')

while True:
    item = input('Item to remove: ')
    if item == '-0': break
    items_list.append(item)


handle_file = open(file_name, 'r')

content = str()

for line in handle_file:
    for item in items_list:
        line = line.replace(item, '')
        line = line.strip() + '\n'
    content += line

try:
    with open(new_file_name, 'w') as f:
        f.write(content)
except:
    print('Something went wrong')

print('New file created!')
