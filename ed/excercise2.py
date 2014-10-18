def functionex2(lis):
    newlis=[lis[0]]
    for element in lis[1:]:
        if element == newlis[-1]:
            print element
        else:
            newlis.append(element)
    return newlis
