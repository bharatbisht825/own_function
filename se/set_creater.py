import logging
logging.basicConfig(filename="set_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
try:
    def se(s):
                """creates set

                Args:
                    s (iterable)
                """
                if s!=set:
                    raise Exception("this is not a set")
                l=s
                b=[]
                c=[]
                count=0
                for i in l:
                    if(i not in b):
                        c.append(i)
                    b.append(i)
                return c
except Exception as e:
    logging.exception(e)