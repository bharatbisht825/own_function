import logging
logging.basicConfig(filename="list_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
class lremove:
    def __init__(self,a):
        if type(a)==list:
            self.old_list=a
    def lremove(self,c):
        for k in self.old_list:
                if (k==c):
                        b=k
        first_list=[]
        second_list=[]
        final=[]
        for i in range(0,b):
                first_list.append(self.old_list[i])
        for j in range(b+1,len(self.old_list)):
                second_list.append(self.old_list[j])
        final=first_list+second_list
        logging.info(f"the is list is {final} ")
        return final
a=lremove([1,2,3,4])
a.lremove(2)
    