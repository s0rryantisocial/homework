immutable_var = tuple
tuple_ = 1, 2, 5, 'apple'
print(tuple_)
#tuple_ [0] = 3 \\ TypeError: 'tuple' object does not support item assignment Был бы список получилось бы
#print(tuple_)
mutable_list = tuple
tuple_ = ([3, 4], 5, 'peach')
print(tuple_)
tuple_[0][0] = 'Hello'
print(tuple_)
