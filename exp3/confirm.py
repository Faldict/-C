#!/usr/bin/env python
from BloomFilter import BloomFilter


def merge(s, l):
    for i in l:
        if i not in s:
            s.append(i)


def calc1():
    fo = open('pg1661.txt', 'r')
    reads = []
    for i in range(10000):
        s = fo.readline()
        l = s.split(' ')
        merge(reads, l)
    return len(reads)


def calc2():
    fo = open('pg1661.txt', 'r')
    count = 0
    reads = BloomFilter(320000)
    for i in range(10000):
        s = fo.readline()
        l = s.split(' ')
        for i in l:
            count += reads.BloomFilter(i)
    return count


def main():
    res1 = calc1()
    res2 = calc2()
    print res1, res2


if __name__ == '__main__':
    main()
