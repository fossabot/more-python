# -*- coding:utf-8 -*-

import fileinput
import argparse

class Uniq(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__input = fileinput.input(('-',))
        self.__print()
    def __print(self):
        pre = None
        for line in self.__input:
            line = line.strip()
            if pre == None:
                print(line)
            elif pre != line:
                print(line)
            pre = line
if __name__ == "__main__":
    Uniq()