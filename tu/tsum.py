import logging
logging.basicConfig(filename="tuple_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
try:
    class tsum:
        def __init__(self,a):
            if type(a)==tuple:
                self.old_tuple=a
            else:
                raise Exception("this is not a tuple")
        def tsum(self):
            """sum of all elements in tuple
            """
            su=0
            for i in (self.old_tuple):
                su=su+i
            logging.info(f"the sum of tuple is {su} ")
except Exception as e:
    logging.exception(e)
a=tsum((1,5))
a.tsum()