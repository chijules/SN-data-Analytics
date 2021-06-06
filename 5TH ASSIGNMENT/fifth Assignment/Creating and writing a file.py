file1=open("myfile.txt", "w")
num=int(input("please enter 2 to get the multiplication table:"))
for i in range(1,13):
    print(num,"x", i, "=", num*i)
file1.close()