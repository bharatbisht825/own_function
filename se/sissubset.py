import logging
import set_creater
logging.basicConfig(filename="set_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
try:
    class sissubset:
        def __init__(self,a):
            if (type(a)==set):
                self.old_set=a
        def sissubset(self,b):
            """finds if it is a subset of th old set

            Args:
                b (_set_): 
            """
            if(type(b)==set):
                count=0                         
                for i in b:
                    if i in (self.old_set):
                            count=count+1
                                                                   
            else:
                raise Exception("this is not a set")
            if(len(b)==count or len(b)==0):
                logging.info(f"{b} is subset of {self.old_set} ")
            else:
                logging.info(f"{b} is  not a subset of {self.old_set} ")
except Exception as a:
    logging.exception("a")
i=sissubset({1,2,3,4})
i.sissubset({1,2})
