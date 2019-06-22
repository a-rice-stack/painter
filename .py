import tkinter

# 이게뭐지

wid = 1
color = "black"

now_color = "검정색"

lastx1, lasty1 = 0, 0


# 기본 설정
window = tkinter.Tk()

window.title("그림판")

window.geometry("800x600+0+0")

window.resizable(0, 0)




# 프레임 설정

canvas = tkinter.Frame(window, width = 500, height = 300, relief = "solid", bd = 1)

canvas.pack(side = "top")

canvas.place(x = 150, y = 10)


label = tkinter.Frame(window, width = 100, height = 50, relief = "solid", bd = 1)

label.pack()

butten = tkinter.Frame(window, width = 15, height = 3, relief = "solid", bd = 0)

butten.pack(side = "bottom")

butten.place(x = 375, y = 400)




# 캔버스 설정

canvas = tkinter.Canvas(canvas, width = 500, height = 300, cursor = "pencil")




# 버튼 설정

butten1 = tkinter.Button(butten, relief = "solid", width = 5, height = 3, text = "검정", repeatdelay=1, repeatinterval=100, activebackground="black").pack()

butten2 = tkinter.Button(butten, relief = "solid", width = 5, height = 3, text = "빨강", repeatdelay=1, repeatinterval=100, activebackground="red").pack()

butten3 = tkinter.Button(butten, relief = "solid", width = 5, height = 3, repeatdelay=1, repeatinterval=100, text = "지우개", activebackground="white").pack()



#라벨 설정

label = tkinter.Label(label, text = "색  =  "  + str(now_color))
label.pack()









window.mainloop()
