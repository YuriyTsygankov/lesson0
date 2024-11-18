my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_index = 0
while my_index < len(my_list):
    if my_list[my_index] < 0:
        break
    elif my_list[my_index] == 0:
        my_index = my_index + 1
        continue
    else:
        print(my_list[my_index])
        my_index = my_index + 1
