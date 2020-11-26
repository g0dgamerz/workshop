# ​Write a Python program to remove duplicates from a list

def Remove(l_o_d):
    final_list = []
    for num in l_o_d:
        if num not in final_list:
            final_list.append(num)
    return final_list


l_o_d = ['python', 'is', 'awesome', 'python', 'is', 'awesome']
print(Remove(l_o_d))
