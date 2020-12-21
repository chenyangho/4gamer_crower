import tkinter as tk  # 使用Tkinter前需要先匯入

# 第1步，例項化object，建立視窗window
window = tk.Tk()

# 第2步，給視窗的視覺化起名字
window.title('My Window')

# 第3步，設定視窗的大小(長 * 寬)
window.geometry('600x400')  # 這裡的乘是小x

# 第4步，在圖形介面上建立一個標籤label用以顯示並放置
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

frame = tk.Frame(window, bg="black")
frame.pack(side=tk.LEFT, fill=tk.BOTH)

# 第6步，定義觸發函式功能
def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):     # 如果選中第一個選項，未選中第二個選項
        l.config(text='I love only Python ')
    elif (var1.get() == 0) & (var2.get() == 1):   # 如果選中第二個選項，未選中第一個選項
        l.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):   # 如果兩個選項都未選中
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')             # 如果兩個選項都選中

# 第5步，定義兩個Checkbutton選項並放置
var1 = tk.IntVar()  # 定義var1和var2整型變數用來存放選擇行為返回值
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()
var7 = tk.IntVar()
var8 = tk.IntVar()
c1 = tk.Checkbutton(frame, height=2, text='遊戲資訊', variable=var1, onvalue=1, offvalue=0, command=print_selection)    # 傳值原理類似於radiobutton部件
c1.pack()
c2 = tk.Checkbutton(frame, height=2, text='硬體新聞', variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()
c3 = tk.Checkbutton(frame, height=2, text='影劇動漫', variable=var3, onvalue=1, offvalue=0, command=print_selection)
c3.pack()
c4 = tk.Checkbutton(frame, height=2, text='玩具周邊', variable=var4, onvalue=1, offvalue=0, command=print_selection)
c4.pack()
c5 = tk.Checkbutton(frame, height=2, text='電子競技', variable=var5, onvalue=1, offvalue=0, command=print_selection)
c5.pack()
c6 = tk.Checkbutton(frame, height=2, text='深度專題', variable=var6, onvalue=1, offvalue=0, command=print_selection)
c6.pack()
c7 = tk.Checkbutton(frame, height=2, text='實況直播', variable=var7, onvalue=1, offvalue=0, command=print_selection)
c7.pack()
c8 = tk.Checkbutton(frame, height=2, text='展覽活動', variable=var8, onvalue=1, offvalue=0, command=print_selection)
c8.pack()
# 第7步，主視窗迴圈顯示
window.mainloop()