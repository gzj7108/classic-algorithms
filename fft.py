import math

class FFT_dit2():
    """signal processor:FFT
    a time of extraction according to the base 2
    
    """
     
    def __init__(self):
        """init a fft model"""
        self.length=0
        self.layer=0

    def setlength(self,l):
        """input the length of the signal
            check it must be the 2^n
        """
        if l&(l-1)==0:
            self.length=l
            while(l!=0):
                l=int(l/2)
                self.layer+=1
            self.layer-=1
            #print("layer:",self.layer)

        else:
            print("please choose the right length")

    def reverse_bit(self,i):
        """input the natural order:binary 
            return the bit reversal order:binary
        """
        temp=[]
        for j in range(self.layer):
            temp.append(int(i%2))
            #print(temp)
            i/=2

        temp.reverse()
        i_reverse=0
        index=0
        for j in temp:
            i_reverse+=2**index*j
            index+=1   
        #print("i reverse:",i_reverse)
        return i_reverse
    
    def recurse(self,s,l,layer):
        """recurse the butterfly type operation"""
        l_next=int(l/2)
        pi=3.14159 
        if l ==len(s) :
        
            s_next=self.recurse(s[:],l_next,layer-1)
            #print("s_next:",s_next)
            for i in range(l_next):
                #print("layer2:",layer)
                w=math.cos(-2*pi*i/l)+math.sin(-2*pi*i/l)*1j
                #print("w:",w,"l:",l)
                s[i]=s_next[i]+s_next[i+2**(layer-1)]*w
                s[i+2**(layer-1)]=s_next[i]-s_next[i+2**(layer-1)]*w 
                
            #print("i:",i,"\t",i+2**(layer-1))

        elif layer!=1:
            s_next=self.recurse(s[:],l_next,layer-1)
            #print("s_next:",s_next)
            for i in range(0,len(s),2**layer):
                #print(s)
                #w=math.cos(-2*pi*i/l)+math.sin(-2*pi*i/l)*1j
                
                for j in range(layer):  
                    #print("layerhh:",layer)
                    w=math.cos(-2*pi*(i+j)/l)+math.sin(-2*pi*(i+j)/l)*1j
                    #print("w:",w)
                    s[i+j]=s_next[i+j]+s_next[i+j+2**(layer-1)]*w
                    s[i+j+2**(layer-1)]=s_next[i+j]-s_next[i+j+2**(layer-1)]*w
                   
           
        else:
            #print("s:",s)
            for i in range(0,len(s),2):
                #print("i:",i)
                #print("layer1:",layer)
                w=1
                #print("w:",w)
                t1=s[i]
                t2=s[i+1]
                s[i]=t1+t2*w
                s[i+1]=t1-t2*w
            #print("s:",s)
        return s

    def reverse_signal(self,s):
        """inverse the signal by module reverse bit"""
        x=s[:]
        for i in range(len(s)):
            i_t=fft.reverse_bit(i)
            x[i]=s[i_t]
        #print(x)
        return x


fft=FFT_dit2()
x=[1,2,-1,4]
print("orginal signal:",x)
fft.setlength(len(x))
x=fft.reverse_signal(x)

print("after fourier transform:",fft.recurse([1,-1,2,4],len(x),fft.layer))
"""print("x:",x)
fft.transform()

for i in range(8):
    print("input:",i,"\nreverse:",fft.reverse_bit(3,i))
"""

                