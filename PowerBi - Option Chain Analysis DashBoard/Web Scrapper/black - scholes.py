import numpy as np
from scipy.stats import norm


#Veriable

r = 0.1
S = 35956 #underlying
K = 35000 #strike
T = 5/7
sigma = 0.01

def blackschole(r,K,T,sigma,type='C'):
    "calculate BS option Price for Call/Put"
    d1 = (np.log(S/K)+(r+sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1-sigma*np.sqrt(T)
    try:
        if type=="C":
            price = S*norm.cdf(d1,0,1) - K*np.exp(-r*T)*norm.cdf(d2,0,1)
        elif type =="P":
            price = K*np.exp(-r*T)*norm.cdf(-d2,0,1) - S*norm.cdf(-d1,0,1)
        return price
    except :
        print("Please check All options Parameters")
print("Option Price is :",blackschole(r,S,T,sigma,type="C"))