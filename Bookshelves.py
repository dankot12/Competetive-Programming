import sys

inp = []
inp = map(int,raw_input().split())
N_books = inp[0]
Swaps = inp[1]
book1 = [int(x) for x in inp[2:(N_books+2)]]
book2 = [int(x) for x in inp[(N_books+2):]]
book1.sort()
book2.sort()
book3 = book1[:]
book4 = book2[:]

for i in range(Swaps):
    book1[N_books-1],book2[0] = book2[0],book1[N_books-1]
    book1.sort()
    book2.sort()

    book4[N_books-1],book3[0] = book3[0],book4[N_books-1]
    book3.sort()
    book4.sort()

print min(max(book1)+max(book2),max(book3)+max(book4))
