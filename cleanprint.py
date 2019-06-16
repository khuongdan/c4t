items = ['giay','ao','quan']
print(items)
print(*items, sep=' ')
new_item = input ('Do khac:')
items.append(new_item)
print(*items, sep=' ')
print(*items, sep=',')
print(*items, sep='|')
