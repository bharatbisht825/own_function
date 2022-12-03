import logging
logging.basicConfig(filename="dict_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
class dpop:
    def __init__(self,a):
        if (type(a)==dict):
            self.old_dict=a
    def dpop(self,b,c):
        """
        remove the key and displays default value

        Args:
            b (string):  the key you want to remove
            c (string):  the default value to display if key not found
        """
        self.old_dict.pop(b,c)
        logging.info(f"the value im the dictionary is {self.old_dict} ")
a=dpop({"a":1,"b":2})
a.dpop("b","this")