def convert_list_into_dicty(list_of_numbers):
    if not list_of_numbers:
        return {}
    total_number_of_elements_in_list= len(list_of_numbers)
    unique_values= sorted(set(list_of_numbers))

    result= {}
    for value in unique_values:
        count= sum(x<=value for x in list_of_numbers)
        percentage= (count/total_number_of_elements_in_list)*100
        result[value]= percentage
    return result

list_of_numbers=[5,3,9,2]
print(convert_list_into_dicty(list_of_numbers))
