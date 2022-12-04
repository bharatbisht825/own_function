import logging
logging.basicConfig(filename="tuple_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
try:

    class tmin:
        def __init__(self,a):
            if type(a)==tuple:
                self.old_tuple=a
            else:
                raise Exception("this is not a tuple")
        def tmin(self):
            """minimum element of tuple
            """
            mi=self.old_tuple[0]
            for i in (self.old_tuple):
                if(mi>i):
                    mi=i
            logging.info(f"the min of tuple is {mi} ")
except Exception as e:
    logging.exception(e)
a=tmin((1,2,5,8,9))
a.tmin()