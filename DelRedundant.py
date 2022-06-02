# py for deleting redundant codes
import numpy as np

b_comment = ['#']
nums = "0123456789"
chars = ['+', '-', '*', '-', '=', '==']
funcs =  ["print"]
classes = ["class", "self"]

class simplify:
    def __init__(self, pathName):
        self.path = pathName
        self.tokens = []
    def getToken(self):
        pass
    def deleteRed(self):
        pass
    def printFile(self):
        with open(self.path, mode = 'r', encoding= 'utf-8') as fp:
            temp = fp.read()
        print(temp)

if __name__ == '__main__':
    sp = simplify('./testFile.py')
    sp.deleteRed()
    sp.printFile()
