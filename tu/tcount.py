
import logging
logging.basicConfig(filename="tuple_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
class tcount:
    def __init__(self,a):
        if type(a)==tuple:
            self.old_tuple=a
    def tcount(self):
        count=0
        for i in (self.old_tuple):
            count=count+1
        logging.info(f"the count of tuple is {count} ")

a=tcount((1,2))
a.tcount()