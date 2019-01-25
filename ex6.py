# -*- coding:utf-8 -*-
from ex4 import ParseArgs
import os
import fnmatch
import subprocess

class Find:
    def __init__(self):
        # 初始化参数
        self.args = ParseArgs()
        args_len = self.args.args_len
        def pass_fuc(value):
            pass
        self.fmt_print = pass_fuc
        self.exec = pass_fuc
        if args_len in self.args.flags:
            end_arg = self.args.flags[args_len]
            if end_arg == '--print':
                self.fmt_print = lambda value: print(value)
            elif end_arg == ';' and 'exec' in self.args.select:
                l = args_len
                sh = ''
                while l in self.args.flags:
                    sh = ' ' + self.args.flags[l] + sh
                    l = l - 1
                sh = self.args.select['exec'] + sh

                def _(f):
                    re_sh = sh.replace('{}', f).strip().split(' ')[:-1]
                    subprocess.call(re_sh)

                self.exec = _
        # 功能扩展
        self.switch = {
            'name': self.__name,
            'type': self.__info,
        }
        self.func = []
        # 过滤
        for function, value in self.args.select.items():
            if function in self.switch:
                self.func.append(self.switch[function](value))

        self.__init_files()

        for item in self.file_path:
            self.exec(item)

    def __init_files(self):
        # 获取目录
        if 0 in self.args.flags and os.path.isdir(self.args.flags[0]):
            work_space = self.args.flags[0]
        else:
            raise Exception('first args not path')
        work_space = os.path.abspath(work_space)
        self.file_path = []
        self.__push_file(work_space, self.file_path)

    def __push_file(self, work_space, file_path):
        file_list = os.listdir(work_space)
        for file in file_list:
            file = os.path.join(work_space, file)
            if self.__exp(file):
                self.fmt_print(file)
                file_path.append(file)
            if os.path.isdir(file):
                self.__push_file(file, file_path)
                continue

    def __exp(self, file):
        for fun in self.func:
            if not fun(file):
                return False

        return True

    def __name(self, fil):
        return lambda f: fnmatch.fnmatch(os.path.split(f)[-1], fil)

    def __info(self, fil):
        type_switch = {
            'd': os.path.isdir,
            'f': os.path.isfile,
            'l': os.path.islink,
        }
        if not fil in type_switch:
            raise Exception('unrecognized type')
        return lambda f: True if type_switch[fil](f) is True else False


if __name__ == "__main__":
    Find()