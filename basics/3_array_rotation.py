class ArrayRotation:
    def __init__(self, records: list):
        self.records = records
        self.len = len(records)

    def rotate_left(self, num_times: int):
        if num_times <= 0:
            return self.records

        num_times = num_times % self.len
        pivot = num_times

        self.records = self.records[pivot:] + self.records[:pivot]

        return self.records

    def rotate_right(self, num_times: int):
        if num_times <= 0:
            return self.records

        num_times = num_times % self.len
        pivot = self.len - num_times

        self.records = self.records[pivot:] + self.records[:pivot]

        return self.records


if __name__ == "__main__":
    records = list(range(10))
    ar = ArrayRotation(records)

    print(ar.rotate_left(2))
    print(ar.rotate_right(2))

    print(ar.rotate_right(10))
    print(ar.rotate_left(10))

    print(ar.rotate_left(11))
    print(ar.rotate_right(1))

    print(ar.rotate_left(0))
    print(ar.rotate_right(0))

    print(ar.rotate_left(-1))
    print(ar.rotate_right(-1))
