class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        if is_negative:
            x *= -1

        l = self.__length_positive_num(x)

        num_rev = self.__reverse_positive(x, l)
        if is_negative:
            num_rev *= -1

        return num_rev

    def __length_positive_num(self, num: int):
        if num == 0:
            return 1

        l = 0
        while num > 0:
            num = num // 10
            l += 1

        return l

    def __reverse_positive(self, num: int, length: int):
        num_rev = 0

        while num > 0:
            rem = num % 10
            num = num // 10

            num_rev += rem * 10 ** (length - 1)

            length -= 1

        return num_rev


if __name__ == "__main__":
    num = 0
    s = Solution()
    print(s.reverse(num))
