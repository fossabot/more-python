# -*- coding:utf-8 -*-

import sys

# 基于sys.args的参数解析


class ParseArgs:
    flags = {}
    select = {}
    args_len = 0

    def __init__(self):
        self.args_len = len(sys.argv)
        if self.args_len <= 1:
            return
        can_help = True if sys.argv[1].replace('-', '')  in ['h', 'help']  else False
        if can_help :
            print('-h, --help 获得帮助文档')
            return
        select_title = ''
        index = -1
        for item in sys.argv[1:]:
            index = index + 1
            if select_title != '':
                self.select[select_title] = item
                select_title = ''
            elif len(item) > 1 and item[0] == '-':
                select_title = item[2:] if item[1] == '-' else item[1:]
            else:
                self.flags[index] = item
        if select_title != '':
            self.flags[index] = '--' + select_title if len(
                select_title) > 1 else '-' + select_title


if __name__ == "__main__":
    args = ParseArgs()
    print(args.flags, args.select)