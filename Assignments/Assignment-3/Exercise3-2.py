try:
    hrs = input("Enter Hours:")
    h = float(hrs)
    rate = input("Enter Rate:")
    r = float(rate)
    
except:
    print("Error, please enter numeric input")
    quit()


regpay = h*r
overpay = (h-40)*(1.5-1)*r

if h <= 40:
    print(regpay)
else:
    print(regpay+overpay)