import itertools
"""PRACT 1 QUESTION 6
"""
IN = input('Enter the vector    ')
N = input('Enter the value of N ')

def chunks(vector,size):
    """ dividing a list into equal size n chunks
    """
    reverse_chunk_list = []
    for i in range(0, len(vector), size):
        reverse_chunk_list.append(vector[i:i+size])
    print("The chunks are ", reverse_chunk_list)
    reverse_chunk_list.sort(reverse=True)
    reverse_chunk_list = list(itertools.chain.from_iterable(reverse_chunk_list))
    return reverse_chunk_list

def reverse(vector, n):
    """function to reverse the input vector of size n
    """
    list1 = []
    vector_length = len(vector)
    difference = vector_length-n
    new_vector = vector[difference:]
    list1.append(new_vector)
    left_vector = vector[:difference]
    if len(left_vector) >= n:
        chunked_list = chunks(left_vector, n)
    else:
        chunked_list = left_vector
    list1 = list(itertools.chain.from_iterable(list1))
    return list1+chunked_list

OUT = reverse(IN, N)
print(OUT)
