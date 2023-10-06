from sys import argv
 
n_green=int(argv[1])
n_red=int(argv[2])
t=int(argv[3])
 
flg=1
 
while True:
    if flg>0:
        if t<=n_green:
            print("green")
            break
        t=t-n_green
    else:
        t=t-n_red
        if t<=n_red:
            print("red")
            break
         
    flg=-flg