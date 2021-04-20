# reverse string using recursion
# name=jaswanth reverse=htnawsaj
# def reverse(s):
#     l = len(s)
#     if l == 1:
#         return s
#     else:
#         return s[-1] + reverse(s[:-1])
#
#
# if __name__ == '__main__':
#     s = input()
#     r = reverse(s)
#     print(r)

# coinexchange
def rec_coin(target, coins):
    min_coins = target
    if target in coins:
        return 1
    else:
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + rec_coin(target - i, coins)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins


print(rec_coin(63, [1, 5, 10, 25]))
