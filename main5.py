file = open('Condigal.txt','r')
print(file.read())
file.close()

file = open('Condigal.txt','r')
print("\n Read in Parts \n")
print(file.read(8))
file.close()

file = open('Condigal.txt','a')
file.write(" Hi! I am Penguin and I am 1yr old.")
file.close()