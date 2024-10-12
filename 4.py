def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()

print_params('all', 'two')
print_params(1, 4, True)
print_params('one', 10, False)
print_params(2)
print_params(b=25)
print_params(c=[1,2,3])
print_params()

values_list=[1, 'two', False]
values_dict={a='one', b=False, c=10}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [2, 'one']
print_params(*values_list_2, 42)
