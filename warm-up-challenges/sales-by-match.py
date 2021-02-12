
# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    socks_sorted = dict()
    pairs = 0

    for colour in ar:
        if socks_sorted.get(colour):
            socks_sorted[colour] += 1
        else:
            socks_sorted.update({colour: 1})

    for colour in socks_sorted:
        pairs += socks_sorted[colour] // 2

    return pairs


if __name__ == '__main__':

    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    result = sockMerchant(n, ar)

    print('pairs =',result)
