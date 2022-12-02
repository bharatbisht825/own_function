import logging
logging.basicConfig(filename="list_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
class lpop:
    def __init__(self,a):
        if type(a)==list:
            self.old_list=a
    def lpop(self,b):
        """
        pops out the element at the list position
        """
        out=self.old_list[b]
        logging.info(f"the popped out element is {out}")
a=lpop([1,2,3,4])
a.lpop(3)