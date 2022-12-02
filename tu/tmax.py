import logging
logging.basicConfig(filename="tuple_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
class tmax:
    def __init__(self,a):
        if type(a)==tuple:
            self.old_tuple=a
    def tmax(self):
        mx=self.old_tuple[0]
        for i in (self.old_tuple):
            if(mx<i):
                mx=i
        logging.info(f"the max of tuple is {mx} ")

a=tmax((1,2,5,8,9))
a.tmax()