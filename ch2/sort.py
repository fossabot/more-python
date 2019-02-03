# -*- coding:utf-8 -*-
import argparse
import fileinput


class Sort(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        parser = argparse.ArgumentParser()
        parser.add_argument('-t', type=str, default=' ', required=False)
        parser.add_argument(
            '-u', '--uniq', action='store_true', required=False)
        parser.add_argument('-r', action='store_true', required=False)
        parser.add_argument('-k', type=int, required=False)
        parser.add_argument('file', nargs='*')
        self.args = parser.parse_args()
        self.input_file_scan = fileinput.input(
            self.args.file if len(self.args.file) > 0 else ('-', ))

        self.sort_key = (lambda value: value) if self.args.k == None else (
            lambda value: value.split(self.args.t)[self.args.k])
        self.filtration = set if self.args.uniq else lambda value: value
        self.__read()

    def __read(self):
        for item in sorted(
                self.filtration(self.input_file_scan),
                key=self.sort_key,
                reverse=self.args.r):
            print(item.strip())


if __name__ == "__main__":
    Sort()