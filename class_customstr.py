class Customstr:
    def __init__(self,str):
        self.str=str
   
    def remove_duplicate(self):
        sav=[]
        res=[]
        for char in self.str : 
            found = 0
            for seen_char in sav:
                if char == seen_char  :
                    found = 1 
                    break 
            if found==0 : 
                sav.append(char)
                res.append(char)
        print("".join(res))

    def set(self,index,set_char):
        self.index=index
        self.set_char=set_char
        list1=list(self.str)
        list1[index]=self.set_char

        print("".join(list1))

    def isflot(self):
     try:
      if self.str == float(self.str) :
        return True
     except:
        return False

    def ispalindrome(self):
        li=[]
        li=self.str
        if li[::-1]==li : 
            print("ture")
        else :
            print("false")
        
   
x=Customstr("3.14")
a=x.remove_duplicate()
a1=x.set(0,"A")
a2=x.ispalindrome()
a3=x.isflot()
print(a3)
        
