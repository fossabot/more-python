# -*- coding:utf-8 -*-

import argparse

class Cat(object):
    def __init__(self):
        super().__init__()
        handle = argparse.ArgumentParser()
        handle.add_argument('files',nargs='*')
        self.args = handle.parse_args()
    def handle(self):
        for file in self.args.files:
            with open(file) as f:
                print(''.join(f.readlines()))

if __name__ == "__main__":
    Cat().handle()