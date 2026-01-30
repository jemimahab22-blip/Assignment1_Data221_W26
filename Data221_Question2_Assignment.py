def nested_dictionary_strings(list_of_strings):
    my_dictionary_of_elements={}
    for elements in list_of_strings:
        length_of_the_strings= len(elements)
        if length_of_the_strings %2==0:
            parity = "even"
        else:
            parity = "odd"

        my_dictionary_of_elements[elements]= {
            "length": length_of_the_strings,
            "parity": parity
        }
    return my_dictionary_of_elements
data= ["data", "science"]
print(nested_dictionary_strings(data))

