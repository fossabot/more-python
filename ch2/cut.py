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
            items = line.split(self.args.d)
            if '-' in self.args.f:
                line = ' '.join(self.__continue(self.args.f, items))
            elif ',' in self.args.f:
                has_none_items = map(
                    lambda i: items[int(i)] if len(items) > int(i) else None,
                    self.args.f.split(','))
                line = ' '.join(
                    [item for item in has_none_items if item != None])
            elif int(self.args.f) < len(items):
                line = items[int(self.args.f)]
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
        if self.args.c != None:
            sh = re.search(r'\d*-\d*', self.args.c)
            if sh != None:
                self.args.c = sh.group(0)
            else:
                return False
        if self.args.f != None:
            sh = re.search(r'(\d*-\d*)|(\d+(,\d+)*)*', self.args.f)
            if sh != None:
                self.args.f = sh.group(0)
            else:
                return False
        return True


if __name__ == "__main__":
    Cut().run()