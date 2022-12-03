import logging
logging.basicConfig(filename="dict_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
try:
    class dfromkeys:
        def __init__(self,a):
            if (type(a)==dict or type(a)==set or type(a)==tuple or type(a)==list):
                self.old_dict=a
            else:    
                raise Exception("this is not an iterable")
        def dfromkeys(self,b):
            """makes dictionary from a iterable (as keys) and a specific value (as value)

            Args:
                b (any): it denotes the specific value
            """
            di={}
            for i in self.old_dict:
                di[i]=b

            logging.info(f"the is new dictionary {di} ")
except Exception as e:
    logging.exception(e)
a=dfromkeys([1,2,3,4,5])
a.dfromkeys(2)