
import os

def sort(list):
    for i in range(len(list)):
        conut = True
        for j in range(len(list)):
            if len(list) > j+1 and list[j] > list[j+1]:
                c = list[j+1]
                list[j+1] = list[j]
                list[j] = c
                conut = False
        if conut:
            break
        
    return list

def sort1(list,list1):
    for i in range(len(list)):
        conut = True
        for j in range(len(list)):
            if len(list) > j+1 and list[j] > list[j+1]:
                c = list1[j+1]
                list1[j+1] = list1[j]
                list1[j] = c
                c = list[j+1]
                list[j+1] = list[j]
                list[j] = c
                conut = False
        if conut:
            break

    print("排序完毕！")
        
    return list1

def strandstr(str1,str2):
    conut = 0
    for i in range(len(str2)):
        if str2[i] in str1 and conut < len(str1):
            conut += 1
    return conut

def strlist(strlist,list,str1):
    a = []
    b = []
    for i in range(len(strlist)):
        if strandstr(strlist[i],str1) != 0:
            a.append(strandstr(strlist[i],str1))
            b.append(list[i])

    print("相似度计算完毕！")
    
    return sort1(a,b)

def lena(str):
    a = len(str)
    for i in range(len(str)):
        if ord(str[i])>200:
            a += 1
    return a

def mapa(str,number):
    return number - lena(str)

def good(str):
    for i in range(len(str)):
        if str[i] == "\\":
            str = str[:i] + "/" + str[i + 1:]
    return str

def acc(lujing = os.getcwd(),name = True):
    try:
        list = os.listdir(lujing)
        list2 = list[:]
        list1 = len(list)
        for i in range(list1):
            try:
                if os.path.exists(lujing + "\\" + list[i]) and os.path.isdir(lujing + "\\" + list[i]):
                    c = list[:]
                    vv = acc(lujing + "\\" + c[i],name = False)
                    for j in vv[0]:
                        list.append(j)
                    for j in vv[1]:
                        list2.append(j)

                list[i] = list[i] + mapa(list[i],50) * " " + good(lujing + "/" + list[i])

            except IndexError:
                pass
    except:
        pass



    print(os.path.basename(lujing),"获取完毕！")
            

    v = 0
    while v < len(list):
        if list[v][:11] == "desktop.ini":
            del list[v]
            del list2[v]
            break
        v += 1

    print("处理噪音完毕！")

    return [list,list2]


def sou(lujing,guanjianci):
    list = acc(lujing)
    aaaaa = list[1][:]
    list = list[0][:]
    
    c = strlist(aaaaa,list,guanjianci)
    c.reverse()

    print("分析完毕！")

    return c

from tkinter import *
import time

class App():
  def __init__(self):
    App.window = Tk()

  def const_say(self, text):
    App.say_text = Label(App.window,text = text)
    App.say_text.pack()

  def say(self, x, y, text):
    App.say_text2 = Label(App.window,text = text)
    App.say_text2.place(x = x, y = y, anchor = NW)

  def windows(self, l, w):
    App.window.geometry(str(w) + "x" + str(l))

  def button(self, text, a):
    App.B = Button(App.window, text = text, command = a)
    App.B.pack()

  def button2(self, text, a, x, y):
    App.B2 = Button(App.window, text = text, command = a)
    App.B2.place(x = x, y = y, anchor = NW)

  def input_str(self, text, f):
    App.inputstr = Entry(App.window)
    App.inputstr.pack()

    b1 = Button(App.window, text = text, command = f)
    b1.pack()

  def input_str2(self, text, f):

    App.inputstr2 = Entry(App.window)
    App.inputstr2.pack()

    b2 = Button(App.window, text = text, command = f)
    b2.pack()

    
  def input_text(self, text, f):
    App.inputtext = Text(App.window, width = 100, heigh = 30)
    App.inputtext.pack()

    b3 = Button(App.window, text = text, command = f)
    b3.pack()

  def input_text2(self):
    App.inputtext2 = Text(App.window, width = 225, heigh = 30)
    App.inputtext2.pack()



  

a = App()

a.windows(500,1050)

a.window.title("搜索")

def b():
    global name
    name = a.inputstr.get()

    try:
        if e != "":
            print("搜索中……")
            c = sou(name,e)
            a.inputtext2.delete(0.0,"end")
            for i in range(len(c)):
                if c[i] != "":
                    a.inputtext2.insert("insert",c[i]+"\n")
            print("搜索完毕！")
    except NameError:
        pass

def d():
    global e
    e = a.inputstr2.get()
    try:
        if name != "":
            print("搜索中……")
            c = sou(name,e)
            a.inputtext2.delete(0.0,"end")
            for i in range(len(c)):
                a.inputtext2.insert("insert",c[i]+"\n")
            print("搜索完毕！")
    except NameError:
        pass

    

    

a.say(0, 0, "请输入文件路径：")
a.input_str("确定", b)
a.input_str2("确定", d)
a.input_text2()

a.window.mainloop()         
