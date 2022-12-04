import logging
logging.basicConfig(filename="list_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
try:
    class lclear:
        def __init__(self,a):
            if type(a)==list:
                self.old_list=a
            else:
                raise Exception("this is not a list")
        def lclear(self):
            """deletes the list items
            """
            self.old_list.clear()
            logging.info(f"the is cleared list is {self.old_list} ")
except Exception as e:
    logging.exception(e)
a=lclear([1,2])
a.lclear()