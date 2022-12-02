import logging
logging.basicConfig(filename="list_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
class llappend:
    def __init__(self,a):
        if type(a)==list:
            self.old_list=a
    def lappend(self,b):
        for i in (b):
            self.old_list.append(i)
        logging.info(f"the is list is {self.old_list} ")

a=llappend([1,2])
a.lappend([5,6])


        
        


