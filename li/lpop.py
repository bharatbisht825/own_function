import logging
logging.basicConfig(filename="list_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
try:
    class lpop:
        def __init__(self,a):
            if type(a)==list:
                self.old_list=a
            else:
                raise Exception("this is not a list")
        def lpop(self,b):
            """
            pops out the element at the list position
            """
            out=self.old_list[b]
            logging.info(f"the popped out element is {out}")
except Exception as e:
    logging.exception(e)
a=lpop([1,2,3,4])
a.lpop(3)