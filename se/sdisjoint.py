import logging
import set_creater
import seadd
logging.basicConfig(filename="set_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
try:
    class sdisjoint:
        def __init__(self,a):
            if (type(a)==set):
                self.old_set=a
        def sdisjoint(self,a):
            """difference between two sets

                Args:
                    a (set):
                """
            flag=True
            if type(a)==set:
                y={}
                y=set(y)
                for i in a:
                    if i in self.old_set:
                        y.add(i)
                if(len(y)==0):
                         logging.info(f"it has no common elements  {flag} ")
                else:
                        flag=False
                        logging.info(f"it has common elements {flag} , {y}")
            
            else:
                raise Exception("this is not a set")
except Exception as a:
    logging.exception(a)
a=sdisjoint({1, 2, 3, 4, 5 })
a.sdisjoint({1, 3, 5, 7, })