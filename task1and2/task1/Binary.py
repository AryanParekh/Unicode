def con_checker(a,b):#main function that returns the dictionary
    def check(str):#function to check if the number has two consecutive 1's
        l=len(str)#storing the length of binary number
        c=0#counter
        for i in range(l-1):#from i=0 to i=l-2
            if(str[i]==str[i+1]=='1'):#checking for consecutive 1's
                c=c+1#increasing the count if consecutive 1's pair is found
        if(c>0):#returning True or False appropriately
            return True
        return False
    d={}#dictionary to store keys and values
    for i in range(a,b):#from a to b-1
        bool=check(bin(i).split('b')[1])#storing true or false for i th value
        d.update({i:bool})#appending in the dictionary
    return d
