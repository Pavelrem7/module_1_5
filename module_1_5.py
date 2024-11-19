immutable_var = (1, 2, 'a', 'b',  True)
print(immutable_var)
# immutable_var[0] = 2
# print(immutable_var)
# TypeError: 'tuple' object does not support item assignment
# Кортежи неизменяемы, что означает, что вы не можете изменять,
# добавлять или удалять элементы после создания кортежа.
mutable_list = [1, 2, 'a', 'b',  False]
mutable_list[0] = 'one'
mutable_list[1] = 5
print(mutable_list)
