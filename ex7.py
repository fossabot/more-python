#-*- coding:utf-8 -*-
# 使用argparse包

from argparse import ArgumentParser
import glob
import os
import re


# 参数处理
class Grep:
    def __init__(self):
        args = ArgumentParser()
        args.add_argument('value', type=str, help='匹配的文本')
        args.add_argument('path', nargs='+', help='文件')
        self.arg = args.parse_args()
        self.next = map(lambda p: glob.glob(p), self.arg.path)

    def run(self):
        for items in self.next:
            files = filter(lambda value: os.path.isfile(value), items)
            for f in files:
                self.__decode(f)

    # 解析文本
    def __decode(self, file):
        with open(file) as f:
            index = 0
            print_path = True
            for line in f:
                result = re.search(self.arg.value, line)
                index = index + 1
                if result == None:
                    continue
                if print_path:
                    print(f'\n{os.path.abspath(file)}\n', end='')
                    print_path = False
                print(f'{index}: {line.strip()}')


if __name__ == "__main__":
    Grep().run()