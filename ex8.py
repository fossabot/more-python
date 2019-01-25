# -*- coding:utf-8 -*-

from argparse import ArgumentParser
import fileinput
import os
import re


class Cut:
    def __init__(self):
        #  参数初始化
        args = ArgumentParser()
        args.add_argument('-c', type=str, required=False)
        args.add_argument('-d', type=str, default=' ', required=False)
        args.add_argument('-f', type=str, required=False)
        args.add_argument('files', nargs='*')
        self.args = args.parse_args()
        # 校验输入
        if not self.__verify():
            raise Exception('verify error')
        self.__read()

    # 切换输入流
    def __read(self):
        self.input = fileinput.input(
            self.args.files if len(self.args.files) > 0 else ('-', ))

    def run(self):
        for line in self.input:
            print(self.__handle(line))
        self.input.close()
        self.input = None

    def __handle(self, line):
        # c命令处理
        if self.args.c != None and '-' in self.args.c:
            line = self.__continue(self.args.c, line)
        # f命令处理
        if self.args.f != None:
            item = line.split(self.args.d)
            if '-' in self.args.f:
                line = self.args.d.join(self.__continue(self.args.f, item))
            elif ',' in self.args.f:
                result = list(
                    map(lambda i: item[int(i)] if len(item) > int(i) else None,
                        self.args.f.split(',')))
                line = ' '.join([item for item in result if item != None])
            elif int(self.args.f) < len(item):
                line = item[int(self.args.f)]
        return line

    def __continue(self, sh, line):
        handle_c = f'{sh}{len(line)}' if sh[-1] == '-' else (
            f'{0}{sh}' if sh[0] == '-' else sh)
        right, left = handle_c.split('-')
        right, left = min(int(right), int(left)), max(int(right), int(left))
        line = line[right:left]
        return line

    # 校验
    def __verify(self):
        result = True
        if self.args.c != None:
            result = result and (True if re.search(r'\d*-\d*', self.args.c)
                                 else False)

        if self.args.f != None:
            result = result and (True if re.search(r'(\d*-\d*)|(\d+(,\d+)*)*',
                                                   self.args.f) else False)
            if result:
                self.args.f = re.search(r'(\d*-\d*)|(\d+(,\d+)*)*',
                                        self.args.f).group(0)
        return result


if __name__ == "__main__":
    Cut().run()