import tkinter as tk

def on_click(key):
    if key == "=":
        try:
            result = str(eval(display.get())) # eval-ით გამოვთვალოთ ჩვენი მოცემული მონაცემები
            display.delete(0, tk.END)
            display.insert(tk.END, result) # ჩვენი შედეგი ჩავსვათ ჩვენს 
        except Exception: #try ბლოკი ცდილობს eval()-ით გამოთვალოს გამოსახულება.თუ მოხდა შეცდომა, გამოიყენება except ბლოკი.
            display.delete(0, tk.END) # თუ ჩვენი მოცემული მონაცემები არასწორია, ჩავსვათ ჩვენი ჯუმპერში შეცდომა
    elif key == "C":
        display.delete(0, tk.END) # "c" დაჭერის შემთხვევაში კალკულატორში ჩაწერილი ყვწლა რიცხბი წაიშლება
    else:
        display.insert(tk.END, key) # ამას ვიყენებთ რომ ციფრები ჩავსვათ შესაყვან ველში, END-ით ციფრებს ვსვავთ ბოლოში და key არის თითოეული ღილაკის მნიშვნელობა

# შევქმნათ ფანჯარა
root = tk.Tk() #ეს ქმნის ფანჯარას
root.title("Group 3's calculator") # დავარქვათ ფანჯარას სახელი (სათაური)
root.resizable(False, False) # ფანჯარის ზომის შეცვლა შეუძლებელი გავხადეთ

display = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right") #display ცვლაში: ტექსტის შეყვანის ველი,ტექსტის font (დიზაინი)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10) #grid-ით გავზარდით ველის ზოლებს და სვეტებს

# buttons list-ით შევქმენით ღილაკები
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+" ,"."
]

row = 1 #საწყისი პოზიციები ღილაკების განსათავსებლად
col = 0 #საწყისი პოზიციები ღილაკების განსათავსებლად

for btn_text in buttons: #გადაუვლის buttons სიას
    button = tk.Button( # ქმნის ღილაკს
        root,
        text=btn_text, #
        font=("Arial", 18),
        width=4,#გაუწერს ზომას
        height=2,
        command=lambda key=btn_text: on_click(key)#lambda-ს მიზანია, რომ თითოეულ ღილაკს თავისი მნიშვნელობა გადაეცეს. მაგ: 1,2,3 ა.შ
    )
    button.grid(row=row, column=col, padx=5, pady=5) #grid-ით გავზარდით ღილაკების ზოლებს და სვეტებს

    col += 1 #სვეტის ინდექსი იზრდება 1-ით
    if col > 3: #თუ სვეტების რაოდენობა მეტია  3-ზე, მაშინ სვეტების რაოდენობა ნული გამოდის
        col = 0
        row += 1

root.mainloop() # mainloop საჭიროა რომ ფანჯრის გახსნის თანავე ის არ დდაიხუროს