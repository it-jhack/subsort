

# This program removes subdomain redundancies and returns an optimized list.
# It saves A LOT of time when parsing large subdomain/dns files with grep.

''' EXAMPLE: 
Suppose you have a 30 GB .txt file full of DNS entries.
if you grep for the lines containing the domain "example.com"
you don't need to parse for "sub.example.com" as the results 
of the latter will be contained in the results of the former.
This program removes the subdomain redundancies, returning an
optimized list, which can later be used at a parsing cmd tool
such as grep.
'''

import argparse

parser = argparse.ArgumentParser(description='Remove redundancies returning an optimized list')
parser.add_argument('subdomains_txt_path', type=str, help='Path to the .txt file containing the list to be optimized')
args = parser.parse_args()

def del_file_subds_redund(subdomains_txt_path):
    with open(subdomains_txt_path, 'r') as lfp:
        inscope_list = []
        for line in lfp:
            # add '.' at the beginning of each subdomain to
            # appropriately test subdomains occurrences in logic parsing.
            inscope_list.append('.' + line.strip('\n'))
        
        sorted_inscope_list = sorted(inscope_list, key=len)
        inscope_range = len(sorted_inscope_list)

        # main list to add unique subdomains.
        optimized_list = [] 

        for i in range(inscope_range):
            
            # temporary list
            temp_list = []
            temp_list.extend(sorted_inscope_list)
            temp_list.remove(sorted_inscope_list[i])
            temp_list_string = str(temp_list)

            # main logic is on if-else
            if sorted_inscope_list[i] in temp_list_string:
                flag = 0
                for item in optimized_list:
                    if item in sorted_inscope_list[i]:
                        flag += 1
                if flag == 0:
                    optimized_list.append(sorted_inscope_list[i])
            else:
                temp_list_string_2 = str(optimized_list)
                if sorted_inscope_list[i] not in temp_list_string_2:
                    flag = 0
                    for item in optimized_list:
                        if item in sorted_inscope_list[i]:
                            flag += 1
                    if flag == 0:
                        optimized_list.append(sorted_inscope_list[i])

    # removing '.' at the beginning of each subdomain (not necessary anymore).
    for i, element in enumerate(optimized_list):
        optimized_list[i] = element.strip('.')

    # putting elements in alphabetical order.
    optimized_list.sort() 

    return optimized_list

def print_list_elements(list):
    for element in list:
        print(element)


if __name__ == '__main__':

    optimal_subd_list = []
    optimal_subd_list.extend(del_file_subds_redund(args.subdomains_txt_path))

    print_list_elements(optimal_subd_list)