try:
    import logging
    logging.basicConfig(filename="dict_file.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
    class dclear:
        def __init__(self,a):
            if type(a)==dict:
                self.old_dict=a
            else:
                raise Exception("this is not a dictionary")
        def dclear(self):
            """
            Clears the dictionary
            """
            self.old_dict.clear()
            logging.info(f"the is cleared dictionary is {self.old_dict} ")
except Exception as e:
    logging.exception(e)
a=dclear({"a":1,"b":2})
a.dclear()