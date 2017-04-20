import numpy as np

class linear_search():
    """ Starting from the beginning of the array we search for the value x in array.
    :param arr: Array(1D) or list

    """
    def __init__(self, arr):
        self.arr = arr

    def find(self,x,n=None):
        '''
        if arr[i]=x then it return i else None
        :param x: value you want to search
        :param n: till what index you want to search
        :return: Index for the first appearance of x
        '''
        if n==None:
            n = len(self.arr)
        for i in range (n):
            if self.arr[i]==x:
                return i
        return None

    def findAll(self,x,n=None):
        '''
        make an empty list
        if arr[i]=x then append i to that list
        after all iteration return the list
        :param x: value you want to search
        :param n: till what index you want to search
        :return: list of Index for all appearance of x
        '''

        index = []
        if n==None:
            n = len(self.arr)
        for i in range (n):
            if self.arr[i]==x:
                index.append(i)
        return index

    def isPresent(self,x,n=None):
        '''
        if arr[i]=x then it return True else False
        :param x: value you want to search
        :param n: till what index you want to search
        :return: Ture/False if x is found in arr
        '''

        if n==None:
            n = len(self.arr)
        for i in range (n):
            if self.arr[i]==x:
                return True
        return False
        pass

    def showTime(self):
        pass