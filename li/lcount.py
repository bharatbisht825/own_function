import logging
logging.basicConfig(filename="list_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
try:
    class lcount:
        def __init__(self,a):
            if type(a)==list:
                self.old_list=a
            else:
                raise Exception("this is not a list")
        def lcount(self):
            """count element in  list
            """
            count=0
            for i in (self.old_list):
                count=count+1
            logging.info(f"the count of list is {count} ")
except Exception as e:
    logging.exception(e)

a=lcount([1,2])
a.lcount()