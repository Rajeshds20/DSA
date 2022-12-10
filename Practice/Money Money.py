'''
Newton visited his friends in Japan on the occasion of Diwali.

He received N gifts there. Some gifts were in Japanese yen (JPY) and Some gifts were in the form of Bitcoin (BTC).

You are given N values T1, T2,. ., TN and N strings S1, S2,. ., SN. Each string Si is either "JPY" or "BTC" representing the type of the i- th gift and value Xi represents the amount of the i- th gift.

You need to convert and calculate how much Japanese Yen Newton got from Japan visit.

(Note: 1BTC = 380000.0 JPY)
Input
The first line of the input contains a single integer N.
The next N lines contains a real number Ti and a string Si.

Sample Input 1:
2
10000 JPY
0.10000000 BTC

Sample Output 1:
48000.00000000

Explanation
Total value = 10000 + 380000*0.1 = 48000


'''


t = 0
for _ in range(int(input())):
    a = input()
    if a[-3:] == 'BTC':
        t += float(a[:-4])*380000
    else:
        t += float(a[:-4])
print('%.8f' % t)
