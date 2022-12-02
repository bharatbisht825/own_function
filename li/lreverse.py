import logging
logging.basicConfig(filename="list_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
class lreverse:
    def __init__(self,a):
        if type(a)==list:
            self.old_list=a
    def lreverse(self):
        """
        reverses the list

        """
        z=self.old_list[::-1]
        logging.info(f"the reversed list is {z}")
a=lreverse([1,2,3,4])
a.lreverse