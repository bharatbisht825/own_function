import logging
import set_creater
logging.basicConfig(filename="set_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
class sclear:
    def __init__(self,a):
        if (type(a)==set):
            self.old_set=a
    def sclear(self):
        self.old_set.clear()
        logging.info(f"the set is cleared now {self.old_set} ")
a=sclear({"a","b","c","d"})
a.sclear()
