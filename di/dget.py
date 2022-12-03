import logging
logging.basicConfig(filename="dict_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
class dget:
    def __init__(self,a):
        if (type(a)==dict):
            self.old_dict=a
    def dget(self,b):
        for k,v in self.old_dict.items():
            if(k==b):
                the_value=v
        logging.info(f"the value im the dictionary is {the_value} ")
a=dget({"a":1,"b":2})
a.dget("b")