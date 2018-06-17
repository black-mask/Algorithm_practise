class Solution(object):
    # 判断是否为回文数学
    def isPalindrome(self, x):
        if x < 0:
            # print(False)
            return False
        num_list = []
        while x > 0:
            num = x % 10
            x = x // 10
            num_list.append(num)
        r_num_list = list(reversed(num_list))
        if num_list == r_num_list:
            # print(True)
            return True
        else:
            # print(False)
            return False


if __name__ == '__main__':
    check = Solution()
    check.isPalindrome(414)
