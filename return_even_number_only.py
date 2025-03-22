def even_number(all_number):
    even_number_only = []
    for i in (all_number):
        if i % 2 == 0:
            even_number_only.append(i)
    return even_number_only


newlist = [1,4,5,45,23,5,567,755,234]
evenonly = even_number(newlist)
print(f'even numbers only  {evenonly}')
