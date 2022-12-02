import logging
logging.basicConfig(filename="dict_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
class dclear:
    def __init__(self,a):
        if type(a)==dict:
            self.old_dict=a
    def dclear(self):
        self.old_dict.clear()
        logging.info(f"the is cleared dictionary is {self.old_dict} ")
a=dclear({"a":1,"b":2})
a.dclear()