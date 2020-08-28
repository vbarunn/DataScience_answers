# Q2 select pairs with different k


def pair_with_different_k(list_num, k):
    array_len = len(list_num)
    list_num.sort()
    first_index = 0
    second_index = 0
    list_pairs = []
    while second_index < array_len:
        if list_num[second_index] - list_num[first_index] == k:
            list_pairs.append((list_num[first_index], list_num[second_index]))
            first_index += 1
            second_index += 1
        elif list_num[second_index] - list_num[first_index] > k:
            first_index += 1
        else:
            second_index += 1
    return list_pairs


if __name__ == '__main__':
    list_num = [-1, 1, 5, 3, 4, 2]
    k = 2
    pair_list = pair_with_different_k(list_num, k)
    num_of_pairs = len(pair_list)
    print("we will have " + str(num_of_pairs) + " pairs: " + str(pair_list))
