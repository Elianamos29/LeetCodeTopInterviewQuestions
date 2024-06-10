def spl(num):
    l = []
    while num > 0:
        l.append(num % 10)
        num //= 10
    
    return l

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        j = 1
        i = 0
        l = spl(n)
        ans = 0
        hash_a = {0: n}
        while True:
            ans += l[i] ** 2
            if i == len(l) - 1:
                if ans in hash_a.values():
                    return False
                else:
                    hash_a[j] = ans
                    j += 1
                    if ans == 1:
                        return True
                    else:
                        i = -1
                        l = spl(ans)
                        ans = 0
            i += 1
                
        return False

if __name__ == '__main__':
    s = Solution()
    n = 2
    print(s.isHappy(n))