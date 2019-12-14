def binary_search(records: list, key: int):
    i_beg, i_end, i_mid = 0, len(records)-1, None

    if i_end == -1:
        return None

    while i_beg <= i_end:
        i_mid = (i_beg + i_end) // 2

        if key > records[i_mid]:
            i_beg = i_mid + 1
        elif key < records[i_mid]:
            i_end = i_mid - 1
        else:
            return i_mid

    return i_mid if records[i_mid] == key else None


if __name__ == "__main__":
    recs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(recs)
    for key in range(0, 11):
        print(key, binary_search(recs, key))

    recs = []
    print(recs)
    for key in range(5):
        print(key, binary_search(recs, key))
