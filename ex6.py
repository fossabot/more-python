# -*- coding:utf-8 -*-
from ex4 import ParseArgs
import os
import fnmatch


class Find:
    def __init__(self):
        # 初始化参数
        self.args = ParseArgs()
        args_len = self.args.parse_args()
        if (args_len - 1 in self.args.flags
            ) and self.args.flags[args_len - 1] == '--print':
            self.print = lambda value: print(value)
        else:
            self.print = lambda value: value
        # 功能扩展
        self.switch = {
            'name': self._name,
            'type': self._info,
        }
        self.func = []
        # 过滤
        for function, value in self.args.select.items():
            if function in self.switch:
                self.func.append(self.switch[function](value))

        self._init_files()

    def _init_files(self):
        # 获取目录
        if 0 in self.args.flags and os.path.isdir(self.args.flags[0]):
            work_space = self.args.flags[0]
        else:
            raise Exception('first args not path')
        self.file_paths = []
        work_space = os.path.abspath(work_space)
        self._push_file(work_space, self.file_paths)

    def _push_file(self, work_space, file_paths):
        file_list = os.listdir(work_space)
        for file in file_list:
            file = os.path.join(work_space, file)
            if self._exp(file):
                self.print(file)
                file_paths.append(file)

            if os.path.isdir(file):
                self._push_file(file, file_paths)
                continue

    def _exp(self, file):
        for fun in self.func:
            if not fun(file):
                return False

        return True

    def _name(self, filter):
        return lambda f: fnmatch.fnmatch(os.path.split(f)[-1], filter)

    def _info(self, filter):
        type_switch = {
            'd': os.path.isdir,
            'f': os.path.isfile,
            'l': os.path.islink,
        }
        if not filter in type_switch:
            raise Exception('unrecognized type')
        return lambda f: True if type_switch[filter](f) is True else False


if __name__ == "__main__":
    f = Find()