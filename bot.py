import pyttsx3 #--> pyttsx3 adalah perpustakan koversi text-to-speec dengan python
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


pelayan = pyttsx3.init()
pelayan.setProperty('rate', 150) # ---> untuk mengatur kecepatan txs
pelayan.say("Hello welcome to our restaurant, what would you like to order?")
pelayan.runAndWait()


menu = """

Food Menu :         
1. Fried rice        
2. chikcken noodle   
3. Beef soup         
                                                
Menu minuman :       
1. Boba ica           
2. melon juice        
3. grape juice        
                        
                        
"""
print(menu)
pelayan.say(menu)

pelayan.say("Please enter your order!")
pelayan.runAndWait()

window = tk.Tk() #---vectory atau pembuatan
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("RESTORAN GUBUK")

#frame input
input_frame = ttk.Frame(window)
# penempatan pack
input_frame.pack(padx=10,pady=10,fill="x",expand=True)


#label manu pertama
nama_pembeli = ttk.Label(input_frame,text="Input Nama")
nama_pembeli.pack(padx=10,fill="x",expand=True)

# 2. entry nama depan
PEMBELI = tk.StringVar()
entry_nama = ttk.Entry(input_frame,textvariable=PEMBELI)
entry_nama.pack(padx=10,fill="x",expand=True)

menu_pertama = ttk.Label(input_frame,text="Pilih Menu Makanan")
menu_pertama.pack(padx=10,fill="x",expand=True)

# 2. entry nama depan
NAMA_DEPAN = tk.StringVar()
entry_pertama = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
entry_pertama.pack(padx=10,fill="x",expand=True)

# 3. Label pesanan belakang
menu_kedua = ttk.Label(input_frame,text="Pilih Menu Minuman")
menu_kedua.pack(padx=10,fill="x",expand=True)

# 4 label pesanan
NAMA_BELAKANG = tk.StringVar()
pilih_menu_empat = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
pilih_menu_empat.pack(padx=10,fill="x",expand=True)

# 5. Tombol
def tombol_klick():
    print(NAMA_BELAKANG.get())
    """fungsi ini akan dipanggil oleh tombol"""
    Resi = f"[+]Nama : {PEMBELI.get()},   [+]Makanan: {NAMA_DEPAN.get()},    [+]Minuman: {NAMA_BELAKANG.get()}"

    showinfo(title='RESI PEMBELIAN\t',message=Resi)


tombol_input = ttk.Button(input_frame,text="klik",command=tombol_klick)
tombol_input.pack(fill='x',expand=True,padx=10,pady=10)

window.mainloop()





























