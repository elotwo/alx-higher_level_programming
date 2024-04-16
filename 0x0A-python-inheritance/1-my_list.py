#!/usr/bin/python3
class list():
    def __init__(self, append):
        self.append =   
class MyList(list):
    def __init__(self, append):
        super().__init__(self, append)
        self.append = append
    def append(self,li):
        if isinstance(li, int):
            super().append(li)
    def print_sorted(self):
            return sorted(self)
