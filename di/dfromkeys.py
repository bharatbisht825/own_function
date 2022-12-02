import logging
logging.basicConfig(filename="dict_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
class dfromkeys:
    def __init__(self,a):
        if (type(a)==dict or type(a)==set or type(a)==tuple or type(a)==list):
            self.old_dict=a
    def dfromkeys(self,b):
        di={}
        for i in self.old_dict:
            di[i]=b

        logging.info(f"the is new dictionary {di} ")
a=dfromkeys([1,2,3,4,5])
a.dfromkeys(2)