import logging
import set_creater
import seadd
logging.basicConfig(filename="set_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
try:
    class sdifference:
        def __init__(self,a):
            if (type(a)==set):
                self.old_set=a
        def sdifference(self,a):
            """difference between two sets

                Args:
                    a (set):
                """
            if type(a)==set:
                y={}
                y=set(y)
                for i in a:
                    if i not in self.old_set:
                        y.add(i)
                logging.info(f"the difference is  {y} ")
            else:
                raise Exception("this is not a set")
except Exception as a:
    logging.exception(a)
a=sdifference({"a","b","g","t"})
a.sdifference({"d"})
