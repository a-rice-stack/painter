import tkinter

# 이게뭐지

color = "black"

now_color = "검정"

lastx1, lasty1 = 0, 0





# 기본 설정
window = tkinter.Tk()

window.title("그림판")

window.geometry("800x700+0+0")

window.resizable(0, 0)






# 프레임 설정

canvas_frame = tkinter.Frame(window, width = 500, height = 300, relief = "solid", bd = 1)

canvas_frame.pack(side = "top")

canvas_frame.place(x = 150, y = 10)



label = tkinter.Frame(window, width = 100, height = 50, relief = "solid", bd = 1)

label.pack()



butten = tkinter.Frame(window, width = 15, height = 3, relief = "solid", bd = 0)

butten.pack(side = "bottom")

butten.place(x = 375, y = 400)




# 캔버스 설정

canvas = tkinter.Canvas(canvas_frame, width = 500, height = 300, cursor = "pencil")




#색 함수설정

def red():

    global color, now_color

    color = "red"

    now_color = "빨강"

    label.config(text="지금 무슨 색? = " + str(now_color), bg="SystemButtonFace")



def black():

    global color, now_color

    color = "black"

    now_color = "검정"

    label.config(text="지금 무슨 색? = " + str(now_color), bg="SystemButtonFace")



def blue():

    global color, now_color

    color = "blue"

    now_color = "파랑"

    label.config(text="지금 무슨 색? = " + str(now_color), bg="SystemButtonFace")



def eraser():

    global color, now_color

    color = "SystemButtonFace"

    now_color = "지우개"

    label.config(text="지금 무슨 색? = " + str(now_color), bg="SystemButtonFace")


def 초기화():

    canvas.delete("all")



# 버튼 설정

butten1 = tkinter.Button(butten, relief = "solid", width = 5, command = black, height = 2, text = "검정", repeatdelay=1, repeatinterval=100, activebackground="black").pack()

butten2 = tkinter.Button(butten, relief = "solid", width = 5, command = red, height = 2, text = "빨강", repeatdelay=1, repeatinterval=100, activebackground="red").pack()

butten3 = tkinter.Button(butten, relief = "solid", width = 5, command = blue, height = 2, text = "파랑", repeatdelay=1, repeatinterval=100, activebackground="blue").pack()

butten4 = tkinter.Button(butten, relief = "solid", width = 5, command = eraser, height = 2, repeatdelay=1, repeatinterval=100, text = "지우개", activebackground="white").pack()

butten5 = tkinter.Button(butten, relief = "solid", width = 5, command = 초기화, height = 2, text = "초기화", repeatdelay=1, repeatinterval=100, activebackground="white").pack()





#라벨 설정

label = tkinter.Label(label, text = "지금 무슨 색? = "  + str(now_color))

label.pack()




#이건 또 뭐지

def 클릭(event):

    global lastx1, lasty1

    lastx1 = event.x

    lasty1 = event.y

    canvas.create_line(lastx1, lasty1, lastx1+5, lasty1+5, fill = color, width = 5)


def 드랍(event):

    global lastx1, lasty1

    lastx1 = event.x

    lasty1 = event.y

    canvas.create_line(lastx1, lasty1, event.x, event.y, fill = color, width = 5)





#캔버스설정

canvas.bind("<B1-Motion>", 클릭)

canvas.bind("<Button-1>", 드랍)

canvas.pack()










window.mainloop()
