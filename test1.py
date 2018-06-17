class Solution(object):
    # 反转正整数
    def reverse(self, x):
        num_list = [i for i in str(x)]
        if x >= 0:
            nnum_list = reversed(num_list)
            nnum_str = ''.join(nnum_list)
            # print(int(nnum_str))
            return int(nnum_str)
        else:
            nnum_list = reversed(num_list[1:])
            nnum_str = '-' + ''.join(nnum_list)
            # print(int(nnum_str))
            return int(nnum_str)


if __name__ == '__main__':
    a = Solution()
    a.reverse(1234094323409102909231235)
