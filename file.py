''' f = open("new.txt","w")
#print(f)
f.write("This is new file ")
f.flush()
f.write(str(f))
f.flush()
details =This is string 
with multi lines
Writing
    new line
f.write(details)
f.close() '''

#f = open("new.txt","r")
#data = f.read()
#print (data)
#f.close()

f = open("new.txt","r")
print(f.tell())
#f.seek()
data = f.read(60)
print(f.tell())
print (data)
data = f.read(100)
print(data)
print(f.tell())
f.seek(400)
print(f.tell())
f.seek(0)
print(f.readline(28))

#print(f.readlines())

f.close()

f = open("new.txt","w")
f.write(" ")
f.close()
