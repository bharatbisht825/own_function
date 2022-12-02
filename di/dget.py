import logging
logging.basicConfig(filename="dict_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
class dget:
    def __init__(self,a):
        if (type(a)==dict):
            self.old_dict=a
    def dget(self,b):
        di={}
        for k,v in self.old_dict.items():
            di[i]=b

        logging.info(f"the is new dictionary {di} ")
a=dget([1,2,3,4,5])
a.dget(2)