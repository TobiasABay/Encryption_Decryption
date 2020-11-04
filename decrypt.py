import tkinter as tk
from tkinter import *
from cryptography.fernet import Fernet

key = b'mQMcJ0z9Eq8hYXPVVG3ueKrxt7teYuSEa-0qGyZPgbY='
cipher_suite = Fernet(key)



root= tk.Tk()

canvas1 = tk.Canvas(root, width = 1000, height = 500,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Encryption')
label1.config(font=('helvetica', 14))
canvas1.create_window(500, 25, window=label1)

label2 = tk.Label(root, text='Type your password for encrypt it: ')
label2.config(font=('helvetica', 10))
canvas1.create_window(500, 95, window=label2)

#Name of the Encryption box
entry1 = tk.Entry (root) 
canvas1.create_window(500, 120, window=entry1)

    
label3 = tk.Label(root, text='Decryption')
label3.config(font=('helvetica', 14))
canvas1.create_window(500, 200, window=label3)

label4 = tk.Label(root, text='Type your encryption for decrypt it: ')
label4.config(font=('helvetica', 10))
canvas1.create_window(500, 220, window=label4)

#Name of the decryption box
entry2 = tk.Entry (root, width=120) 
canvas1.create_window(500, 245, window=entry2)

label_subject = tk.Label(root, text='Type your subject: ')
label_subject.config(font=('helvetica', 10))
canvas1.create_window(500, 45, window=label_subject)

#Name of the subject
entry_subject = tk.Entry (root) 
canvas1.create_window(500, 70, window=entry_subject)

def encryption ():
    x1 = entry1.get()

    ciphered_text = cipher_suite.encrypt(bytes(x1, encoding='utf8'))

    label5 = tk.Label(root, text= 'Your encryption is: ',font=('helvetica', 8))
    canvas1.create_window(500, 140, window=label5)
            
    label6 = tk.Label(root, text= str(ciphered_text),font=('helvetica', 10, 'bold'))
    canvas1.create_window(500, 160, window=label6)

    return ciphered_text


def decrypt ():
    x2 = entry2.get()

    ciphered_text_2 = bytes(x2, encoding='utf8')
    unciphered_text = (cipher_suite.decrypt(ciphered_text_2))

    label7 = tk.Label(root, text= 'Your password is: ',font=('helvetica', 8))
    canvas1.create_window(500, 265, window=label7)
            
    label8 = tk.Label(root, text= unciphered_text,font=('helvetica', 10, 'bold'))
    canvas1.create_window(500, 285, window=label8)

    return unciphered_text

def encrypt():
    ciphered_text = encryption()
    entry2.insert(END, str(ciphered_text))

def clearFunc():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry_subject.delete(0,END)

def open_txt():
    output_subject = entry_subject.get()
    
    ciphered_text = encryption()
    encrypted_text = str(ciphered_text) 

    with open("encryption_codes", "a") as file_object:
        file_object.write("-----------------------------------------------------------------------------------------------------------------")
        file_object.write("\n")
        file_object.write(output_subject + " " +  "|" + " " + encrypted_text)
        file_object.write("\n")
        file_object.write("-----------------------------------------------------------------------------------------------------------------")
        file_object.write("\n")
        file_object.write("\n")
    

button2 = tk.Button(text='Decrypt!', command=decrypt, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(900, 245, window=button2)

button3 = tk.Button(text='Encrypt!', command=encrypt, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(600, 120, window=button3)

button4 = tk.Button(text='Clear!', command=clearFunc, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(25, 15, window=button4)

button5 = tk.Button(text='Write to document', command=open_txt, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(110, 15, window=button5)


root.mainloop()