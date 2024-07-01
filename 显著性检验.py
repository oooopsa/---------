import numpy as np
import matplotlib.pyplot as plt


class SingleParamsHypothesisTest:
    
    def __init__(self,x,alpha,target,given,type = "u", OneTailOrTwo= "t"):
        
        if isinstance(x,(list,np.ndarray)):
            self.x = x
        else:
            self.x = np.array(x)
        
        self.x = x
        self.mean = np.mean(x)
        self.std = np.std(x)
        self.target = target
        self.given = given
        self.alpha = alpha
        self.type = type
        self.oot = OneTailOrTwo
        
    def cdf(self,f,x):
        
        
        
        
    def test(self):
        
        if self.type == "u":
            
            u = self.mean - self.target
            if self.oot == "t":
                if u > 0:
                    p = 1 - self.cdf(u)
                else:
                    p = self.cdf(u)
            else:
                p = 2*(1 - self.cdf(u))
                
            return p