my_list = [10, 20, 30, 40]

my_list.extend([3, 6, 7])
print("а.) Розширений список:", my_list)

my_list.insert(1, 33333)
print("б.) Список зі вставленим значенням:", my_list)

my_list.reverse()
print("в.) Список у зворотньому порядку:", my_list)

my_list.append(3)
print("г.) Список з доданим значенням у кінець:", my_list)

my_list.remove(3)
print("д.) Список з видаленим першим значенням 3:", my_list)

my_list.sort()
print("е.) Список у порядку збільшення:", my_list)

my_list.clear()
print("ж.) Порожній список:", my_list)
