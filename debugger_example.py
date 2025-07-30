



def print_only_odd_num_in_list(num_list):
    for num in num_list:
        if not num%2==0:
            print(num)
        
massive = range(1, 10)
print_only_odd_num_in_list(massive)