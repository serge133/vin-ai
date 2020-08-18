def index_of_largest_element(array): 
  
    # Initialize maximum element 
    max = array[0]

    largest_index = 0
  
    # Traverse array elements from second 
    # and compare every element with  
    # current max 
    index=0
    for i in range(1, len(array)): 
        index+=1
        if array[i] > max: 
            max = array[i] 
            largest_index=index
    return largest_index