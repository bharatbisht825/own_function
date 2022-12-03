
def se(s):
            """creates set

            Args:
                s (iterable)
            """
            l=s
            b=[]
            c=[]
            count=0
            for i in l:
                if(i not in b):
                    c.append(i)
                b.append(i)
            return c
    