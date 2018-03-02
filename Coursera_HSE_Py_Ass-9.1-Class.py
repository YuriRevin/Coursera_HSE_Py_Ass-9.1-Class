from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, text):
        self.text = deepcopy(text)

    def __str__(self):
        joined = '\n'.join(['\t'.join([
            str(i) for i in row])for row in self.text])
        string = ''
        for row in self.text:
            for i in row:
                string += str(i)
        return joined

    def size(self):
        rows = len(self.text)
        cols = 0
        for row in self.text:
            if len(row) > cols:
                cols = len(row)
        return rows, cols


exec(stdin.read())
