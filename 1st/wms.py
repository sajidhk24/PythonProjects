from tkinter import *
from tkinter import messagebox
import tempfile
import os

root = Tk()
root.title('Tussle Enterprises')
root.geometry('1280x720')
bg_color = 'light blue'


# =====================variables===================
Bread = IntVar()
Wine = IntVar()
Rice = IntVar()
Gal = IntVar()
Total = IntVar()

Bread_rate = IntVar()
Wine_rate = IntVar()
Rice_rate = IntVar()
Gal_rate = IntVar()
Total_rate = IntVar()

cb = StringVar()
cw = StringVar()
cr = StringVar()
cg = StringVar()
total_cost = StringVar()

br = StringVar()
wr = StringVar()
rr = StringVar()
gr = StringVar()

# ===========Function===============
def total():
    if Bread.get() == 0 and Wine.get() == 0 and Rice.get() == 0 and Gal.get() == 0:
        messagebox.showerror('Error', 'Please select number of quantity')
    else:
        b = Bread.get()
        w = Wine.get()
        r = Rice.get()
        g = Gal.get()

        br = Bread_rate.get()
        wr = Wine_rate.get()
        rr = Rice_rate.get()
        gr = Gal_rate.get()
        # br = Bread_rate.get()

        t = float(b * int(br) + w * int(wr) + r * int(rr) + g * int(gr))
        Total.set(b + w + r + g)
        total_cost.set('Rs' + str(round(t, 2)))

        cb.set('Rs: ' + str(round(b * br, 2)))
        cw.set('Rs: ' + str(round(w * wr, 2)))
        cr.set('Rs: ' + str(round(r * rr, 2)))
        cg.set('Rs: ' + str(round(g * gr, 2)))


def receipt():
    textarea.delete(1.0, END)
    textarea.insert(END, ' Items\tQuantity of Items\t Rate of Items\t Cost of Items\n')
    textarea.insert(END, f'\nBread\t\t{Bread.get()}\t {br.get()}\t {cb.get()}\n')
    textarea.insert(END, f'\n\nWine\t\t{Wine.get()}\t {wr.get()}\t {cw.get()}\n')
    textarea.insert(END, f'\n\nRice\t\t{Rice.get()}\t {rr.get()}\t {cr.get()}\n')
    textarea.insert(END, f'\n\nMilk\t\t{Gal.get()}\t  {gr.get()}\t {cg.get()}\n')
    textarea.insert(END, f"\n\n================================")
    textarea.insert(END, f'\nTotal Price\t\t {Total.get()}\t {total_cost.get()}')
    textarea.insert(END, f"\n================================")


def printout():
    # text_file = open("test.txt", "r")
    # content = text_file.read()
    # my_text_box.insert(END, content)
    # text_file.close()

    text_file = open("test.txt", "w")
    text_file.write("\t \t \t Tussle Enterprises \n ")
    # text_file.write("\t \t \t GST NUMBER; 009334323 \n \n ")
    # text_file.close()
    text_file.write(textarea.get(1.0, END))
    text_file.close()

    # q = textarea.get('1.0', 'end-1c')
    # filename = tempfile.mktemp('bill.txt')
    # open(filename, 'w').write(q)
    # os.startfile(filename, 'Print')


def reset():
    textarea.delete(1.0, END)
    Bread.set(0)
    Wine.set(0)
    Rice.set(0)
    Gal.set(0)
    Total.set(0)

    cb.set('')
    cw.set('')
    cr.set('')
    cg.set('')
    total_cost.set('')

    textarea.delete(1.0, END)
    Bread_rate.set(0)
    Wine_rate.set(0)
    Rice_rate.set(0)
    Gal_rate.set(0)

    br.set('')
    wr.set('')
    rr.set('')
    gr.set('')


def exit():
    if messagebox.askyesno('Exit', 'Do you really want to exit?'):
        root.destroy()


title = Label(root, pady=5, text="Tussle Enterprises", bd=12, bg=bg_color, fg='black',
              font=('times new roman', 40, 'bold'), relief=GROOVE, justify=CENTER)
title.pack(fill=X)


# ===============Product Details=================
F1 = LabelFrame(root, text='Product Details', font=('times new roman', 26, 'bold',), fg='Purple', bg=bg_color, bd=15,
                relief=RIDGE)
F1.place(x=5, y=90, width=800, height=500)


# =====================Heading==========================
item = Label(F1, text='Items', font=('times new roman', 20, 'bold', 'underline'), fg='black', bg=bg_color)
item.grid(row=0, column=0, padx=20, pady=15)

n = Label(F1, text='Quantity of Items', font=('times new roman', 20, 'bold', 'underline'), fg='black', bg=bg_color)
n.grid(row=0, column=1, padx=30, pady=15)

m = Label(F1, text = "Rate", font=('times new roman', 20, 'bold', 'underline'), fg= 'black', bg= bg_color)
m.grid(row=0, column=2, padx=30, pady=15)

cost = Label(F1, text='Cost of Items', font=('times new roman', 20, 'bold', 'underline'), fg='black', bg=bg_color)
cost.grid(row=0, column=3, padx=30, pady=15)

# ===============Product============

bread = Label(F1, text='Bread', font=('times new roman', 20, 'bold'), fg='green', bg=bg_color)
bread.grid(row=1, column=0, padx=20, pady=15)
b_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=Bread, justify=CENTER)
b_txt.grid(row=1, column=1, padx=20, pady=15)
b_rate = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=br, justify=CENTER)
b_rate.grid(row=1, column=3, padx=20, pady=15)
cb_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=cb, justify=CENTER)
cb_txt.grid(row=1, column=2, padx=20, pady=15)
# cb_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=cb, justify=CENTER)
# cb_txt.grid(row=1, column=2, padx=20, pady=15)


wine = Label(F1, text='Wine', font=('times new roman', 20, 'bold'), fg='green', bg=bg_color)
wine.grid(row=2, column=0, padx=20, pady=15)
w_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=Wine, justify=CENTER)
w_txt.grid(row=2, column=1, padx=20, pady=15)
cw_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=cw, justify=CENTER)
cw_txt.grid(row=2, column=2, padx=20, pady=15)
w_rate = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=wr, justify=CENTER)
w_rate.grid(row=2, column=3, padx=20, pady=15)

rice = Label(F1, text='Rice', font=('times new roman', 20, 'bold'), fg='green', bg=bg_color)
rice.grid(row=3, column=0, padx=20, pady=15)
r_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=Rice, justify=CENTER)
r_txt.grid(row=3, column=1, padx=20, pady=15)
cr_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=cr, justify=CENTER)
cr_txt.grid(row=3, column=2, padx=20, pady=15)
r_rate = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=rr, justify=CENTER)
r_rate.grid(row=3, column=3, padx=20, pady=15)

gal = Label(F1, text='Milk', font=('times new roman', 20, 'bold'), fg='green', bg=bg_color)
gal.grid(row=4, column=0, padx=20, pady=15)
g_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=Gal, justify=CENTER)
g_txt.grid(row=4, column=1, padx=20, pady=15)
cg_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=cg, justify=CENTER)
cg_txt.grid(row=4, column=2, padx=20, pady=15)
gal_rate = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=gr, justify=CENTER)
gal_rate.grid(row=4, column=3, padx=20, pady=15)

t = Label(F1, text='Total', font=('times new roman', 20, 'bold'), fg='green', bg=bg_color)
t.grid(row=5, column=0, padx=20, pady=15)
t_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=Total, justify=CENTER)
t_txt.grid(row=5, column=1, padx=20, pady=15)

totalcost_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=total_cost, justify=CENTER)
totalcost_txt.grid(row=5, column=3, padx=20, pady=15)


# =====================Bill area====================
F2 = Frame(root, relief=GROOVE, bd=10)
F2.place(x=820, y=90, width=430, height=500)

bill_title = Label(F2, text='Receipt', font='arial 15 bold', bd=7, relief=GROOVE).pack(fill=Y)

scrol_y = Scrollbar(F2, orient=VERTICAL)
scrol_y.pack(side=RIGHT, fill=Y)

textarea = Text(F2, font='arial 15', yscrollcommand=scrol_y.set)
textarea.pack(fill=BOTH)
scrol_y.config(command=textarea.yview)


# =====================Buttons========================
F3 = Frame(root, bg=bg_color, bd=15, relief=RIDGE)
F3.place(x=5, y=590, width=1270, height=120)

btn1 = Button(F3, text='Total', font='arial 25 bold', padx=5, pady=5, bg='white', fg='black', width=10, command=total)
btn1.grid(row=0, column=0, padx=20, pady=10)

btn2 = Button(F3, text='Receipt', font='arial 25 bold', padx=5, pady=5, bg='white', fg='black', width=10,
              command=receipt)
btn2.grid(row=0, column=1, padx=10, pady=10)

btn3 = Button(F3, text='Print', font='arial 25 bold', padx=5, pady=5, bg='white', fg='black', width=10,
              command=printout)
btn3.grid(row=0, column=2, padx=10, pady=10)

btn4 = Button(F3, text='Reset', font='arial 25 bold', padx=5, pady=5, bg='white', fg='black', width=10, command=reset)
btn4.grid(row=0, column=3, padx=10, pady=10)

btn5 = Button(F3, text='Exit', font='arial 25 bold', padx=5, pady=5, bg='white', fg='black', width=10, command=exit)
btn5.grid(row=0, column=4, padx=10, pady=10)

root.mainloop()