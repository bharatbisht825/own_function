import logging
logging.basicConfig(filename="tuple_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
try:
    class tmax:
        def __init__(self,a):
            if type(a)==tuple:
                self.old_tuple=a
            else:
                raise Exception("this is not tuple")
        def tmax(self):
            """maximun element in tuple
            """
            mx=self.old_tuple[0]
            for i in (self.old_tuple):
                if(mx<i):
                    mx=i
            logging.info(f"the max of tuple is {mx} ")
except Exception as e:
    logging.exception(e)
a=tmax((1,2,5,8,9))
a.tmax()