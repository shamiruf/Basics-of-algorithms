def permutations(array):
    our_list = []

    if len(array) == 0:
        return [[]]

    if len(array) == 1:
        #print("LEN IS 1" + str(array))
        return [array]
    #print("============")
    for x in array:
        other_list = array.copy()
        other_list.remove(x)
        #print("We are take from array: " + str(array) +"this x " + str(x))
        #print("After for sectiob our other_list have: " + str(other_list))
        z = permutations(other_list)
        #print("now z array is : " + str(z))
        for y in z:
            f = [x]
            #print("f + x : " +str(f))
            #print(y)
            if type(y) == int:
                #print('y is  int')
                f.append(y)
            else:
                f.extend(y)
            #print("f " +str(f))
            our_list.append(f)
            #print('OOOOUUUURRRR_LIST ' + str(our_list))

    return our_list
    

print(permutations([]))

#print("==========")

print(permutations([1]))

#print(permutations([1,2,3]))
