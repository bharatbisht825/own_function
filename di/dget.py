import logging
logging.basicConfig(filename="dict_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
try:
    class dget:
        def __init__(self,a):
            if (type(a)==dict):
                self.old_dict=a
            else:
                raise Exception("this is not a dictionary")
        def dget(self,b):
            """gets value for specified key

            Args:
                b (any): enter the key
            """
            for k,v in self.old_dict.items():
                if(k==b):
                    the_value=v
            logging.info(f"the value im the dictionary is {the_value} ")
except Exception as e:
    logging.exception(e)
a=dget({"a":1,"b":2})
a.dget("b")