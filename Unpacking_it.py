def print_params (a=1, b="строка", c=True):
    print(a,b,c)
print_params()
print_params(2, 'столбец', False)
print_params(3, 'None')
print_params(a='один', b='два', c='три')
print_params(a='один', b='два')
print_params(b='два', c='три')
print_params(a='один', c='три')
print_params(a='один')
print_params(b='два')
print_params(c='три')
print_params()

print_params(b=25)
print_params(c=[1,2,3])
values_list = [2, "пробел", False]
values_dict = {"a" : 1, "b":"строка", "c" :True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']  
print_params(*values_list_2, 42)
