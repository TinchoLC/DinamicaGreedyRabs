def op(x, y):
    if x == 'a' and y == 'a':
        return 'b'
    elif x == 'a' and y == 'b':
        return 'b'
    elif x == 'a' and y == 'c':
        return 'a'
    
    if x == 'b' and y == 'a':
        return 'c'
    elif x == 'b' and y == 'b':
        return 'b'
    elif x == 'b' and y == 'c':
        return 'a'
        
    if x == 'c' and y == 'a':
        return 'a'
    elif x == 'c' and y == 'b':
        return 'c'
    elif x == 'c' and y == 'c':
        return 'c'

    else:
        return None


#   a b c
# a b b a
# b c b a
# c a c c

X = {'a', 'b', 'c'}
Y = {'b','c'}
Z = {'a','b'}
W = {'a','c'}
A = {'a'}
B = {'b'}
C = {'c'}

def SETMULT(J, K):
    H = set()
    for x in J:
        for y in K:
            z = op(x, y)
            H.add(z)
    return H

# print (SETMULT(C,Y))

def R(s):
    if len(s) == 1:
        return {s[0]}
    else:
        results = set()
        for i in range(1, len(s)):
            left_set = R(s[:i])
            right_set = R(s[i:])
            results |= SETMULT(left_set, right_set)
        return results
# Al usar 2 R(s) y un setmult la cota superior es approx O(n3)

def Rr(s, memo={}):
    if len(s) == 1:
        return {s[0]}
    elif s in memo:
        return memo[s]
    else:
        results = set()
        for i in range(1, len(s)):
            left_set = Rr(s[:i], memo)
            right_set = Rr(s[i:], memo)
            results |= SETMULT(left_set, right_set)
        memo[s] = results
        return results
s = 'aaacb'


def R_iter(s):
    n = len(s)
    dp = [[set() for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n):
        dp[i][i+1] = {s[i]}
    
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l
            for k in range(i+1, j):
                dp[i][j] |= SETMULT(dp[i][k], dp[k][j])
    
    return dp[0][n]

print (R(s))
print (Rr(s))
print (R_iter(s))
