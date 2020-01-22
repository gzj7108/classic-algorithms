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

        else:
            print("please choose the right length")

    def reverse_bit(self,i):
        """input the natural order:binary 
            return the bit reversal order:binary
        """
        temp=[]
        for j in range(self.layer):
            temp.append(int(i%2))
            i/=2

        temp.reverse()
        
        i_reverse=0
        index=0
        for j in temp:
            i_reverse+=2**index*j
            index+=1   

        return i_reverse
    
    def recurse(self,s,l,layer):
        """recurse the butterfly type operation"""
        l_next=int(l/2)
        pi=3.14159 
        if l ==len(s) :
        
            s_next=self.recurse(s[:],l_next,layer-1)
            for i in range(l_next):
                w=math.cos(-2*pi*i/l)+math.sin(-2*pi*i/l)*1j
                #optimize the performance
                t=s_next[i+2**(layer-1)]*w
                s[i]=s_next[i]+t
                s[i+2**(layer-1)]=s_next[i]-t        

        elif layer!=1:
            s_next=self.recurse(s[:],l_next,layer-1)
            for i in range(0,len(s),2**layer):               
                for j in range(layer):  
                    w=math.cos(-2*pi*(i+j)/l)+math.sin(-2*pi*(i+j)/l)*1j
                    #optimize the performance
                    t=s_next[i+j+2**(layer-1)]*w
                    s[i+j]=s_next[i+j]+t
                    s[i+j+2**(layer-1)]=s_next[i+j]-t

        else:
            for i in range(0,len(s),2):
                w=1
                t1=s[i]
                #optimize the performance
                t2=s[i+1]*w
                s[i]=t1+t2
                s[i+1]=t1-t2

        return s

    def reverse_signal(self,s):
        """inverse the signal by module reverse bit"""
        x=s[:]
        for i in range(len(s)):
            i_t=fft.reverse_bit(i)
            x[i]=s[i_t]

        return x



#test
fft=FFT_dit2()
x=[1,2,-1,4]
print("orginal signal:",x)
fft.setlength(len(x))
x=fft.reverse_signal(x)
print("after fourier transform:",fft.recurse(x,len(x),fft.layer))

                