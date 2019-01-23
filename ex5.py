# -*- coding:utf-8 -*-

from ex4 import ParseArgs

args = ParseArgs()
size = args.parse_args()

if __name__ == "__main__":
    n = 0
    while True:
        if n in args.flags:
            with open(args.flags[n]) as f:
                print(''.join(f.readlines()))
        elif n >= size:
            break
        n = n + 1