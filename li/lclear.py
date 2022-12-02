import logging
logging.basicConfig(filename="list_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
class lclear:
    def __init__(self,a):
        if type(a)==list:
            self.old_list=a
    def lclear(self):
        self.old_list.clear()
        logging.info(f"the is cleared list is {self.old_list} ")
a=lclear([1,2])
a.lclear()