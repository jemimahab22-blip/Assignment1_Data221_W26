def x_to_the_power_of_y(x,y):
    return  x**y  #storing the computation x the power of y
list_of_pairs = [[5, 2], [3, 0], [4, -7], [2, 0]]#list of pairs we want to use
results_for_list_of_pairs=[]#empty list for us to add results to
for x,y in list_of_pairs:
    if y<0:
        continue
    else:
        results_for_list_of_pairs.append(x_to_the_power_of_y(x, y))
print(results_for_list_of_pairs)
