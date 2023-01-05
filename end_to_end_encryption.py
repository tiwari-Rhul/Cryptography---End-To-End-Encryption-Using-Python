# python module for one-timepad
import onetimepad
# python module to create GUI		
from tkinter import *

		
root = Tk()
root.title("End-To-End Encryption")
root.geometry("500x100")

def encryptMessage():					
	pt = e1.get()

	# inbuilt function to encrypt a message
	ct = onetimepad.encrypt(pt, 'random')
	e2.insert(0, ct)

def decryptMessage():					
	ct1 = e3.get()

	# inbuilt function to decrypt a message
	pt1 = onetimepad.decrypt(ct1, 'random')
	e4.insert(0, pt1)
	
# creating labels and positioning them on the grid
label1 = Label(root, text ='Enter Text')			
label1.grid(row = 10, column = 1)
label2 = Label(root, text ='Encrypted')
label2.grid(row = 11, column = 1)
l3 = Label(root, text ="Encrypted Text")
l3.grid(row = 10, column = 10)
l4 = Label(root, text ="Decrypted")
l4.grid(row = 11, column = 10)

# creating entries and positioning them on the grid
e1 = Entry(root)
e1.grid(row = 10, column = 2)
e2 = Entry(root)
e2.grid(row = 11, column = 2)
e3 = Entry(root)
e3.grid(row = 10, column = 11)
e4 = Entry(root)
e4.grid(row = 11, column = 11)

# creating encryption button to produce the output
ent = Button(root, text = "Encrypt", bg ="red", fg ="white", command = encryptMessage)
ent.grid(row = 15, column = 2)

# creating decryption button to produce the output
b2 = Button(root, text = "Decrypt", bg ="green", fg ="white", command = decryptMessage)
b2.grid(row = 15, column = 11)


root.mainloop()
