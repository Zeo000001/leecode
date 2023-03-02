# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。

# 回文数：
def isPalindrome(x):
    x = str(x)
    length = len(x)
    if length == 1:
        return True
    else:
        for i in range(0, int(length / 2)):
            print(x[i], x[length - i-1])
            if x[i] != x[length - i-1]:
                return False
        return True
#反转数字的函数
def reverseNumber(x):
    r=0
    while x:
        r=r*10+x%10
        x=int(x/10)
    return r
'''
回文数的解法还可以是反转数字
首先数字是负数就一定不是回文数
其次进行数字的反转
 while (x)
            {
                r = r * 10 + (x % 10);
                x /= 10;
            }
当x不为0时，让r从0增加
x每次去除一个低位的数字
'''
if __name__ == '__main__':
    input = 123565431
    print(isPalindrome(input))
    print(reverseNumber(input))
