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
        for n in self.next:
            for item in n:
                if os.path.isfile(item):
                    self.__decode(item)

    # 解析文本
    def __decode(self, file):
        with open(file) as f:
            index = 1
            print_path = True
            for line in f:
                result = re.search(self.arg.value, line)
                if result != None:
                    if print_path:
                        print(f'\n{os.path.abspath(file)}\n', end='')
                        print_path = False
                    print(f'{index}: {line.strip()}')
                index = index + 1


if __name__ == "__main__":
    Grep().run()