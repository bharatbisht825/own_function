import logging
import set_creater
logging.basicConfig(filename="set_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
try:
    class seadd:
        def __init__(self,a):
            if (type(a)==set):
                self.old_set=a
        def seadd(self,b):
            """add elements to the set

            Args:
                b (any one): just one value
            """
            old_set_to_list=[]
            input_elemnt_to_list=[]
            if(type(b)==str):
                input_elemnt_to_list=list(b)
            else:
                for i in str(b):
                    input_elemnt_to_list.append(int(i))       
            old_set_to_list=list(self.old_set) 
            old_set_to_list.extend(input_elemnt_to_list)
            u=set_creater.se(old_set_to_list)
            logging.info(f"the set is {u} ")
except Exception as e:
    logging.exception(e)
a=seadd({"a","b","c","d"})
a.seadd("c")
