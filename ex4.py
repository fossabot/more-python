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


#------- 重构代码
# -*- coding:utf-8 -*-

# import sys


# # update 模仿argparse
# class ParseArgs:
#     # location 根据位置定位 数据应该像[ ['arg1', 'arg2'], ['arg3', 'arg4']] 将连续的数据放在一起
#     location = []
#     # parameter 是参数 kv的关系
#     parameter = {}

#     # 参数列表，用来添加
#     # 每个item分别是dest, p, required, draw, nargs
#     argument = []

#     can_help = False
#     def __init__(self):
#         if len(sys.argv) <= 1:
#             return
#         self.can_help = True if sys.argv[1].replace('-', '')  in ['h', 'help']  else False
        
    
#     # 参数添加 link 是长短链接或者是名字, dest 是getattr用到的, required 是判断是否必须 nargs用来匹配个数
#     def add_argument(self, *links, dest, required=True, nargs='*', help='', action=''):
#         # 有链接类的不需要nargs
#         # 过滤
#         addr_to = list(set(links))
#         addr_to.sort(key=links.index)
#         links = addr_to

#         # 输出
#         draw = []
#         # 参数匹配
#         p = []
#         is_location = None
#         for link in links:
#             if link == '':
#                 return
            
#             if is_location == None:
#                 if link[0] != '-':
#                     p.append(link)
#                     draw.append(link)
#                     is_location = True
#                 else:
#                     is_location = False
            
#             if not is_location:
#                 if len(link) > 2 and link[1] == '-':
#                     p.append(link[2:])
#                 else:
#                     p.append(link[1:])
#                 draw.append(link)
#         if not is_location:
#             nargs = '.'
#             if action == 'store_true':
#                 action = True
#             elif action == 'store_false':
#                 action = False
#             else:
#                 nargs = '-'
#         # 更新 dest
#         dest = [dest] if dest != '' else p
#         draw = '%s\t%s'%("  ".join(draw), help)
#         self.argument.append((dest, p, required, draw, nargs, True)if is_location else (dest, p,required, draw, nargs, action))

#     # 返回一个args类
#     def parse_args(self):
#         # 输出帮助
#         if self.can_help:
#             for item in self.argument:
#                 print(item[3])
#             return
#         args_index = 1
#         for item in self.argument:
#             if len(sys.argv) <= args_index:
#                 raise IndexError()
#             nargs = item[4]
#             required = item[2]
#             dest = item[0]
#             p = item[1]
#             action = item[5]
#             # ? 判断必须，如果不存在则报错
#             if nargs == '?' and required == True:
#                 raise ModuleNotFoundError()
            
#             # if nargs == '*':
#         # select_title = ''
#         # tmp_location = []
#         # index = -1
#         # for item in sys.argv[1:]:
#         #     index = index + 1
#         #     if select_title != '':
#         #         self.parameter[select_title] = item
#         #         select_title = ''
#         #     elif len(item) > 1 and item[0] == '-':
#         #         select_title = item[2:] if item[1] == '-' else item[1:]
#         #     else:
#         #         self.tmp_location[index] = item
                
#         # if select_title != '':
#         #     self.tmp_location[index] = '--' + select_title if len(
#         #         select_title) > 1 else '-' + select_title

# class args(object):
#     def __init__(self, args_key_value):
#         self.__kv = args_key_value
#     def __getattr__(self, name):
#         if name in self.__kv:
#             return self.__kv[name]
#         return super().__getattr__(name)

# if __name__ == "__main__":
#     args = ParseArgs()
#     args.add_argument('-', '--help', dest='hello', required=True,help='帮助文档')
#     args.parse_args()