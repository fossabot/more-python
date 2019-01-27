# -*- coding:utf-8 -*-
from argparse import ArgumentParser
import fileinput
import re


class Sed:

    # 处理参数
    def __init__(self):
        # 开启正则表达式
        parse = ArgumentParser()
        parse.add_argument(
            '-e', dest='regular', action='store_true', required=False)
        parse.add_argument('shell', type=str)
        # 文件
        parse.add_argument('file', nargs='*')
        self.args = parse.parse_args()
        self.over = None
        # 输入流
        self.input_file_scan = fileinput.input(
            self.args.file if len(self.args.file) > 0 else ('-', ))
        self.handle_line = self.__handle_shell()
        self.__read()

    # 处理命令，安排中间件
    # 第一版：完成替换&全局&正则表达式
    def __handle_shell(self):
        # s/regex/value/g
        cmd = self.__handle_escape(self.args.shell)
        handle = []
        if len(cmd) == 4 and cmd[0].strip() == 's':
            if cmd[3] != 'g':
                self.over = 1
            if self.args.regular:
                handle.append(self.__replace_regex)
            else:
                handle.append(self.__replace_str)

        def _(value):
            for h in handle:
                value = h(value, cmd[1], cmd[2])
            return value

        return _

    def __read(self):
        for line in self.input_file_scan:
            print(self.handle_line(line), end='')

    def __replace_str(self, value, old_str, new_str):
        if self.over != None:
            if self.over == 0:
                return value
            elif value.find(old_str) > -1:
                self.over = self.over - 1
        return value.replace(old_str, new_str)

    def __replace_regex(self, value, old_regex, new_str):
        if len(old_regex) == 0:
            return value
        node = re.search(old_regex, value)
        if self.over != None:
            if self.over == 0:
                return value
            elif node != None:
                self.over = self.over - 1
        return value.replace(new_str if node == None else node.group(0),
                             new_str)

    # 转义切割
    def __handle_escape(self, value):
        temp = value.split('/')
        index = 0
        while index < len(temp):
            if temp[index].find('\\') == len(temp[index]) - 1 and len(
                    temp[index]) != 0:
                if index + 1 < len(temp):
                    temp[index] = temp[index][:-1] + '/' + temp[index + 1]
                    del (temp[index + 1])
                else:
                    temp[index] = temp[index][:-1] + '/'
            else:
                index = index + 1

        return temp


if __name__ == "__main__":
    Sed()
