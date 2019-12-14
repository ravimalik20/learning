import random


class Sorting:
    def sort(self, records: list) -> list:
        if len(records) == 0:
            return records

        return self.__merge_sort(records, 0, len(records)-1)

    @classmethod
    def check_sorted(cls, records: list) -> bool:
        n = len(records)

        if n <= 1:
            return True

        i = 1
        while i < n and records[i-1] <= records[i]:
            i += 1

        return i == n

    def __merge_sort(self, records: list, beg: int, end: int) -> list:
        if beg == end:
            return [records[beg]]

        mid = (beg + end) // 2
        list_lhs = self.__merge_sort(records, beg, mid)
        list_rhs = self.__merge_sort(records, mid+1, end)

        return self.__merge(list_lhs, list_rhs)

    @classmethod
    def __merge(cls, list_1, list_2) -> list:
        len_l1, len_l2 = len(list_1), len(list_2)
        list_merged = [0 for _ in range(len_l1 + len_l2)]

        i_l1, i_l2, i_lm = 0, 0, 0

        while i_l1 < len_l1 and i_l2 < len_l2:
            num1, num2 = list_1[i_l1], list_2[i_l2]

            if num1 < num2:
                list_merged[i_lm] = num1
                i_l1 += 1
            else:
                list_merged[i_lm] = num2
                i_l2 += 1
            i_lm += 1

        while i_l1 < len_l1:
            list_merged[i_lm] = list_1[i_l1]
            i_l1 += 1
            i_lm += 1

        while i_l2 < len_l2:
            list_merged[i_lm] = list_2[i_l2]
            i_l2 += 1
            i_lm += 1

        return list_merged


if __name__ == "__main__":
    sorting = Sorting()

    records_1 = list(range(10))  # Already sorted
    records_2 = []  # Empty list
    records_3 = list(range(20, 0, -1))  # Reverse sorted
    records_4 = [random.randint(0, 1000) for _ in range(20)]  # Randomly generated list
    records_5 = [0 for _ in range(20)]  # all elements same

    for records in [records_1, records_2, records_3, records_4, records_5]:
        records_sorted = sorting.sort(records)
        print(records, records_sorted, Sorting.check_sorted(records_sorted))

    print(Sorting.check_sorted(records_4))
