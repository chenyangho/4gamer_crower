import tkinter as tk  # 使用Tkinter前需要先匯入

# 第1步，例項化object，建立視窗window
window = tk.Tk()

# 第2步，給視窗的視覺化起名字
window.title('My Window')

# 第3步，設定視窗的大小(長 * 寬)
window.geometry('600x400')  # 這裡的乘是小x

# 第4步，在圖形介面上建立一個標籤label用以顯示並放置
l = tk.Label(window, bg='sky blue', width=100, height=2, text='歡迎！請勾選想要的新聞＆輸入終止日期')
l.pack()

frame = tk.Frame(window)
frame.pack(side=tk.LEFT, fill=tk.BOTH)

# 第6步，定義觸發函式功能
print_array = []
check_array = [1, 1, 1, 1, 1, 1, 1, 1]
def print_selection():
	if var1.get() == 1:
		if check_array[0] == 1:
			print_array.append("0")
			check_array[0] = 0
		else:
			print_array.remove("0")
			check_array[0] = 1
	elif var2.get() == 1:
		if check_array[1] == 1:
			print_array.append("1")
			check_array[1] = 0
		else:
			print_array.remove("1")
			check_array[1] = 1
	elif var3.get() == 1:
		if check_array[2] == 1:
			print_array.append("2")
			check_array[2] = 0
		else:
			print_array.remove("2")
			check_array[2] = 1
	elif var4.get() == 1:
		if check_array[3] == 1:
			print_array.append("3")
			check_array[3] = 0
		else:
			print_array.remove("3")
			check_array[3] = 1
	elif var5.get() == 1:
		if check_array[4] == 1:
			print_array.append("4")
			check_array[4] = 0
		else:
			print_array.remove("4")
			check_array[4] = 1
	elif var6.get() == 1:
		if check_array[5] == 1:
			print_array.append("5")
			check_array[5] = 0
		else:
			print_array.remove("5")
			check_array[5] = 1
	elif var7.get() == 1:
		if check_array[6] == 1:
			print_array.append("6")
			check_array[6] = 0
		else:
			print_array.remove("6")
			check_array[6] = 1
	elif var8.get() == 1:	
		if check_array[7] == 1:
			print_array.append("7")
			check_array[7] = 0
		else:
			print_array.remove("7")
			check_array[7] = 1
	l.config(text=print_array)

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