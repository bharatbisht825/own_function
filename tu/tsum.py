import logging
logging.basicConfig(filename="tuple_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
class tsum:
    def __init__(self,a):
        if type(a)==tuple:
            self.old_tuple=a
    def tsum(self):
        su=0
        for i in (self.old_tuple):
            su=su+i
        logging.info(f"the sum of tuple is {su} ")

a=tsum((1,5))
a.tsum()