import re
class check_register:   #class define
    def __init__(self,name,lastname,code,username,password,email,mobile):
        self._name=name
        self._lastname=lastname
        self._code=code
        self._username=username
        self._password=password
        self._email=emaile
        self._mobile=mobile
        
    def check_name(self,n):   #getting name as input and check it if condition were in place return true else creating error
       n=input("name:")       #It must just include white space and alphabet character
       if(re.findall("\d",n)):#error numeric character
           raise Exception("name can't be numeric")
       if(len(n)<1 or len(n)>21):#error length
           raise Exception("length error")
       if(re.search(n,"(['!' '@' '#' '$' '%' '^' '&' '*' '( ' ')' '+' '=' '*' '/' '?' '>' '.' '<' ',' '[' ']' '{' '}' ']' ':' ';'])")):
          raise Exception("this characters are not defind")
       else:
          if(re.findall(r'\b[a-zA-Z\s]{2,21}\b',n)):
               print("name is correct:)\n")    
               return True
          else:
               print("last name is incorrect!\n")
           
    def check_lastname(self,l):   #getting last name as input and check it if condition were in place return true else creating error
       l=input("last name:")      #It must just include white space and alphabet character
       if(re.findall("\d",l)):    #error numeric character
           raise Exception("last name can't be numeric")
       if(len(l)<1 or len(l)>30):   #error length
           raise Exception("length error")
       else:
           if(re.findall(r'\b[a-zA-Z\s]{2,30}\b',l)):
               print("last name is correct:)\n")
               return True
           else:
               print("last name is incorrect!\n")



    def check_code(self,c):   #getting code as input and check it if condition were in place return true
        c=[]
        print("code:(input just one number in evry line and click enterkey for go to new line)")
        for i in range(0,10):   #getting 10 number as code and save them in a list
            x=int(input(""))
            c.append(x)
        v=0
        for i in range(0,9):   #calculate the sum of the multiplication of numbers in the index of the list
            v+=(c[i]*(10-i))
        m=v%11
        if(m==2):
            if c[9]==2:
                print("code is correct:)\n")
                return True
            else:
                print("code is incorrect!\n")
        elif(m==1):
            if c[9]==1:
                print("code is correct:)\n")
                return True
            else:
                print("code is incorrect!\n")
        elif(m==0):
            if c[9]==0:
                print("code is correct:)\n")
                return True
            else:
                print("code is incorrect!\n")
        elif c[9]==11-m:
            if c[8]>=2 and c[8]<9:
                print("code is correct:)\n")
                return True
            else:
                print("code is incorrect!\n")

        else:
            print("It's not valid")
             
                
    def check_username(self,u):   #getting user name as input and check it if condition were in place return true else creating error
       u=input("user name:")      #It can just include  alphabet character and numeric character and special symble
       if(len(u)<6 or len(u)>50):   #error length
          raise Exception("length error")
       if(u=="admin" or u=="username"):   #error special words
          raise Exception("this word is not valid")
       if(re.findall("\s",u)):   #error white space
          raise Exception("white space error")
       else:
           if(re.findall(r'\b[a-zA-Z0-9_@-]{6,50}\b',u)):
               print("username is correct:)\n")
               return True
           else:
               print("user name is incorrect!\n!")
               
            
    def check_password(self,p):   #getting password as input and check it if condition were in place return true else creating error
       p=input("password:")       #it must include alphabet and numeric character and special symbel
       if(len(p)<8 or len(p)>50): #error lenght
           raise Exception("length error")
       if(re.findall("\s",p)):    #error white space
           raise Exception("white space error")
         
       if not(re.search("[a-zA-Z]",p)):   #error numeric character
           raise Exception("password should have been 1 character at least")
      
       if not(re.search("[0-9]",p)):   #error alphabet character
           raise Exception("password should have been 1 number at least")
      
       if(re.search('[@#$%&-]',p)):
           print("password is correct:)\n")
           return True
           
             
    def check_mobilenumber(self,m):   #getting mobile number as input and check it if condition were in place return true else creating error
        m=input("mobile number:")     #it must just include numeric character
        if(len(m)!=11):               #error length
            raise Exception("length error")
        elif(re.findall("[a-zA-Z]+",m)):  #error alphabet character
           raise Exception("it must be numeric")
        else:
            if(re.findall('[0-9]',m)):
                print("mobile number is correct:)\n")
                return True
            else:
                print("mobile number is incorrect!\n")
            
    def check_email(self,e):   #getting email address as input and check it if condition were in place return true else creating error
        e=input("Email:")
        if(re.findall(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)',e)):
            print("email address is correct:)\n")
            return True
        else:
            print("email address is incorrect!\n")
if __name__ == '__main__':
    check_register.check_name('self','n')
    check_register.check_lastname('self','l')
    check_register.check_code('self','c')
    check_register.check_username('self','u')
    check_register.check_password('self','p')
    check_register.check_mobilenumber('self','m')
    check_register.check_email('self','e')
    print("congratulation,every thing is ok:)")
