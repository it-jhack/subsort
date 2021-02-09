

# This program removes subdomain redundancies and returns an optimized list.
# It saves A LOT of time when parsing large subdomain/dns files with grep.

''' EXAMPLE: 
Suppose you have a 30 GB .txt file full of DNS entries.
if you grep for the lines containing the domain "example.com"
you don't need to parse for "sub.example.com" as the results 
of the latter will be contained in the results of the former.
This program removes the subdomain redundancies, returning an
optimized list, which can later be used at grep.
'''

import argparse

parser = argparse.ArgumentParser(description='Remove redundancies returning an optimized list')
parser.add_argument('domains_txt_path', type=str, help='Path to the .txt file containing the list to be optimized')

args = parser.parse_args()

def remove_list_redundancies(domains_txt_path):
    with open(domains_txt_path, 'r') as lfp:
        inscope_list = []
        for line in lfp:
            inscope_list.append(line.strip('\n'))
        
        sorted_inscope_list = sorted(inscope_list, key=len)
        inscope_range = len(sorted_inscope_list)

        optimized_list = []

        for i in range(inscope_range):
                
            disposable_list = []
            disposable_list.extend(sorted_inscope_list)
            disposable_list.remove(sorted_inscope_list[i])
            disposable_list_string = str(disposable_list)

            if sorted_inscope_list[i] in disposable_list_string:
                flag = 0
                for item in optimized_list:
                    if item in sorted_inscope_list[i]:
                        flag += 1
                if flag == 0:
                    optimized_list.append(sorted_inscope_list[i])
            else:
                disposable_list_string_2 = str(optimized_list)
                if sorted_inscope_list[i] not in disposable_list_string_2:
                    flag = 0
                    for item in optimized_list:
                        if item in sorted_inscope_list[i]:
                            flag += 1
                    if flag == 0:
                        optimized_list.append(sorted_inscope_list[i])
    return optimized_list

def print_list_elements(list):
    for element in list:
        print(element)


if __name__ == '__main__':
    optimal_subd_list = []
    optimal_subd_list.extend(remove_list_redundancies(args.domains_txt_path))

    print_list_elements(optimal_subd_list)