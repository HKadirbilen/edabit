"""
Testing K^K == N?

Write a function that returns True if k^k == n for input (n, k) and return False otherwise.

Examples
k_to_k(4, 2) ➞ True

k_to_k(387420489, 9) ➞ True
# 9^9 == 387420489

k_to_k(3124, 5) ➞ False

k_to_k(17, 3) ➞ False

Notes
The ^ operator refers to exponentiation operation **, not the bitwise XOR operation.
"""



from edatest import Edatest
Test = Edatest()

def k_to_k(n, k):
    if k**k == n:
        return True
    else:
        return False

if __name__ == '__main__':
    Test.assert_equals(k_to_k(4, 2), True)
    Test.assert_equals(k_to_k(387420489, 9), True)
    Test.assert_equals(k_to_k(302875106592253, 13), True)
    Test.assert_equals(k_to_k(341427877364219557396646723584, 22), True)
    Test.assert_equals(k_to_k(1330877630632711998713399240963346255985889330161650994325137953641, 41), True)
    Test.assert_equals(k_to_k(369729637649726772657187905628805440595668764281741102430259972423552570455277523421410650010128232727940978889548326540119429996769494359451621570193644014418071060667659301384999779999159200499899, 99), True)
    Test.assert_equals(k_to_k(3124, 5), False)
    Test.assert_equals(k_to_k(17, 3), False)
    Test.assert_equals(k_to_k(823544, 7), False)
    Test.assert_equals(k_to_k(443426488243037769948249630619149892801, 27), False)