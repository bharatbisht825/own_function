import logging
import set_creater
logging.basicConfig(filename="set_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
try:
    class sclear:
        def __init__(self,a):
            if (type(a)==set):
                self.old_set=a
            else:
                    raise Exception("this is not a set")
        def sclear(self):
            """deletes the set elements
            """
            self.old_set.clear()
            logging.info(f"the set is cleared now {self.old_set} ")
except Exception as e:
    logging.exception(e)
a=sclear({"a","b","c","d"})
a.sclear()
