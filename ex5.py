# -*- coding:utf-8 -*-

from ex4 import ParseArgs

args = ParseArgs()
args.parse_args()

if __name__ == "__main__":
    n = 0
    for index, v in args.flags.items():
        if n != index:
            print('args is error')
        n = n + 1

        with open(v) as f:
            print(''.join(f.readlines()))
