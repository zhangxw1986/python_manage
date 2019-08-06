# -*- coding:utf-8 -*-


def capital():
    with open('./a.txt') as inf, open('./out.txt','w') as outf:
        for line in inf:
            # newline = " ".join([ word.capitalize() for word in line.split()])
            # outf.write(newline)
            # outf.write('\n')
            print(*[word.capitalize() for word in line.split()],file=outf)


if __name__ == "__main__":
    capital()