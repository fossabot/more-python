# -*- coding:utf-8 -*-

import sys

# 基于sys.args的参数解析

class ParseArgs:
    flags = {}
    select = {}
    l = 0
    def parse_args(self):
        args = sys.argv
        l = len(sys.argv) - 1
        if len(args) == 2 and (args[1] == '-h' or args[1] == '--help'):
            print('-h, --help 获得帮助文档')
            return 
        select_title = ''
        index = -1
        for item in args[1:]:
            index = index + 1
            if len(item) > 1 and item[0] == '-' and select_title == '':
                select_title = item[2:] if item[1] == '-' else item[1:]
                continue
            if select_title != '':
                self.select[select_title] = item
                select_title = ''
                continue
            self.flags[index] = item
        if select_title != '':
            self.flags[index] = '--' + select_title if len(select_title) > 1 else '-' + select_title
        return l

if __name__ == "__main__":
    args = ParseArgs()
    args.parse_args()
    print(args.flags, args.select)