class IntegerListObject:
    def __init__(self, numbers):
        self.numbers = numbers


def merge_objects(obj1, obj2):

    len1 = len(obj1.numbers)
    len2 = len(obj2.numbers)
    max_len = max(len1, len2)

    list1 = obj1.numbers + [0] * (max_len - len1)
    list2 = obj2.numbers + [0] * (max_len - len2)

    merged_list = [list1[i] + list2[i] for i in range(max_len)]

    return IntegerListObject(merged_list)


obj1 = IntegerListObject([1, 2, 3])
obj2 = IntegerListObject([4, 5])

result_obj = merge_objects(obj1, obj2)

print("List of resulting object:", result_obj.numbers)
