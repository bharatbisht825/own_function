import logging
logging.basicConfig(filename="dict_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
class dsetdefault:
    def __init__(self,a):
        if (type(a)==dict):
            self.old_dict=a
    def dsetdefault(self,b,c):
        
        """
        remove the key and displays default value if key not found then creates the key with default value if default value not specified then adds key with none value

        Args:
            b (string):  the key you want to remove
            c (string):  the default value to display if key not found

        """
        flag=False
        li=[]
        for k,v in self.old_dict.items():
                li.append(k)
        for n in li:     
             if (n!=b):
                 flag=True
        if(flag):
            self.old_dict[b]=c
        else:
            self.old_dict.pop(b,c)
        
        logging.info(f"the value in the dictionary is {self.old_dict} ")
a=dsetdefault({"a":1,"b":2})
a.dsetdefault("u","this")
