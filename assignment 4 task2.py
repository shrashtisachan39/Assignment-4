a=input("enter text to write to the file:")
a1=a + "\n"
print("data successfully written to output.txt.")
file1 =open('output.txt','w')
file1.write(a1)
file1.close()

b=input("\nenter additional text to append:")
print("data successfully appended.")
print("\nfinal content of output.txt")

file1 =open('output.txt','a')
file1.write(b)
file1.close()

file1=open('output.txt','r')
reading=file1.read()
print(reading)
file1.close()