def groups_of_3(lst: list[int]) -> list[list[int]]:
    """
    Purpose:
    The purpose of this function is to group the elements of the input list into sublists of three elements each.
    If the number of elements is not a multiple of three, the last sublist will contain fewer than three elements.

    Input:
    - lst: A list of integers (list[int]) that we want to group into sublists of three.

    Output:
    - A list of lists (list[list[int]]) where each sublist contains at most three elements from the original list.
      If there are fewer than three elements left at the end of the list, the last sublist will contain the remaining elements.
    """
    result = []
    for i in range(0, len(lst), 3):
        result.append(lst[i:i + 3])
    return result
