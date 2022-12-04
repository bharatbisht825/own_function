import logging
logging.basicConfig(filename="list_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
try:
    class llappend:
        def __init__(self,a):
            if type(a)==list:
                self.old_list=a
            else:
                raise Exception("this is not a list")
        def lappend(self,b):
            """adds item to new list from a list

            Args:
                b (iterable): to append 
            """
            for i in (b):
                self.old_list.append(i)
            logging.info(f"the is list is {self.old_list} ")
except Exception as e:
    logging.exception(e)

a=llappend([1,2])
a.lappend([5,6])


        
        


