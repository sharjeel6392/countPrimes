class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        isPrime = [1 for i in range(n)]
        isPrime[0] = 0
        isPrime[1] = 0
        i = 2
        while (i*i < n):
            if (isPrime[i] == 1):
                for j in range(i*i, n, i):
                    isPrime[j] = 0
            i += 1
            
        count = 0
        for i in range(n):
            if (isPrime[i] == 1):
                count += 1
        return count;
