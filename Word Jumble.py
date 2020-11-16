from tkinter import *
from PIL import Image,ImageTk
import random,sqlite3

conn=sqlite3.connect('Jumbled_Words.db')
c=conn.cursor()

entry_page=Tk()
entry_page.title("JumbleUp!")
entry_page.geometry('400x400')
entry_page.resizable(0,0)

canvas=Canvas(entry_page,width=400,height=400)
Image1=ImageTk.PhotoImage(Image.open("C:\\Users\\faraz\\PycharmProjects\\Tkinter\\JumbleWordGame\\Background 1.png"))
canvas.create_image(0,0,anchor=NW,image=Image1)
canvas.grid(row=0,column=0)




frame_test=Frame(entry_page)
frame_test.grid(row=0,column=0)
#frame_test.attributes("-alpha",0.3)



def start_game():
    entry_page.destroy()

    global game_window,word_list
    game_window=Tk()
    game_window.title("JumbleUp!")
    game_window.resizable(0,0)

    game_window.geometry('600x600')

    jumble_title_img=Image.open("C:\\Users\\faraz\\PycharmProjects\\Tkinter\\JumbleWordGame\\Title.png")
    jumble_title_img=ImageTk.PhotoImage(jumble_title_img)

    second_canvas=Canvas(game_window,width=600,height=600)
    Image2=ImageTk.PhotoImage(Image.open("C:\\Users\\faraz\\PycharmProjects\\Tkinter\\JumbleWordGame\\Background 2.png"))
    second_canvas.create_image(0,0,anchor=NW,image=Image2)
    second_canvas.grid(row=0,column=0)

    jumble_title_label = Label(game_window, image=jumble_title_img,bg="black")
    jumble_title_label.grid(row=0, column=0, sticky=NW,pady=10,padx=10)

    question_answer_window_design()
    game_window.mainloop()

def jumble(word):
    length=len(word)
    y=0
    rand=random.sample(range(length),length)
    my_jumble=" "
    while(y!=length):
        my_jumble+=word[rand[y]]
        y+=1
    return my_jumble
global i,score
i=0
score=0

def next():
    global i,question_label,my_answer_label

    my_answer_label.destroy()
    my_answer_label2 = Label(game_window, text="", font=("Helvetica", 20))
    my_answer_label2.grid(row=4, column=0)
    my_answer_label2.config(text=" ")
    i+=1
    question_label.destroy()
    question_answer_window_design()

def question_answer_window_design():

    global answer_entry,i,question_label,score,check_score_label,game_window

    check_score_label=Label(game_window,text=f"Score:-  {score}")
    check_score_label.grid(row=0,column=0)

    conn=sqlite3.connect('Jumbled_Words.db')
    c=conn.cursor()
    c.execute('SELECT * FROM words WHERE ID='+str(i))
    record=c.fetchall()
    print(record[0][1])
    question_label=Label(game_window,text=jumble(record[0][1]),font=("Bungee Shade",30,"bold"),bg="black",fg="white")
    question_label.grid(row=0,column=0,sticky=N,pady=(125,0))


    answer_entry=Entry(game_window,width=20,bg="grey",font=("Helvetica",20))
    answer_entry.grid(row=0,column=0,pady=(10,0))
    global btn_answer,my_answer_label

    submit_img=ImageTk.PhotoImage(Image.open("C:\\Users\\faraz\\PycharmProjects\\Tkinter\\JumbleWordGame\\Submit.png"))

    #submit_img=submit_img.resize((100,100),Image.ANTIALIAS)
    #submit_img=ImageTk.PhotoImage(submit_img)

    btn_answer=Button(game_window,image=submit_img,bg="black",command=answer,borderwidth=0)
    btn_answer.photo=submit_img
    #MAKE IT A HABIT TO ANCHOR PHOTOS TO BUTTONS,LABELS LIKE ABOVE
    #OTHERWISE  IT WILL CREATE A LOT OF ISSUES

    btn_answer.grid(row=0,column=0,sticky=S,pady=(0,200))

    nxt_round = Button(game_window, text="Next>", font=("Helvetica", 15, "bold",),command=next,fg="yellow",bg="black",borderwidth=0)
    nxt_round.grid(row=0, column=0,sticky=NE,pady=15,padx=15)

    exit_img=ImageTk.PhotoImage(Image.open("C:\\Users\\faraz\\PycharmProjects\\Tkinter\\JumbleWordGame\\Exit.png"))

    exit_btn=Button(game_window,image=exit_img,bg="black",command=game_window.destroy,borderwidth=0)
    exit_btn.photo=exit_img

    exit_btn.grid(row=0,column=0,sticky=S,pady=(0,130))

    my_answer_label = Label(game_window, text="", font=("Helvetica", 20))
    my_answer_label.grid(row=4, column=0)
def answer():

    if(len(answer_entry.get())==0):
        print("Write Something First")
    else:

        global my_answer_label,score,check_score_label,btn_answer

        answer_submitted=answer_entry.get()
        answer_entry.delete(0, END)
        answer_submitted=str.title(answer_submitted)


        conn=sqlite3.connect('Jumbled_Words.db')
        c=conn.cursor()
        c.execute('SELECT * FROM words WHERE ID='+str(i))
        answerlist=c.fetchall()


        answer=answerlist[0][1]
        answer=str.title(answer)

        if(answer_submitted==answer):
            correct_tick_image=PhotoImage(file="C:\\Users\\faraz\\PycharmProjects\\Tkinter\\JumbleWordGame\\{activeState.name} (Right).png")
            btn_answer.config(image="")#THIS IS TO DELETE PREVIOUS IMAGE
            btn_answer.config(image=correct_tick_image,bg="black")
            btn_answer.photo=correct_tick_image


            score+=1
            check_score_label.config(text=f"Score:-  {score}")
        else:
            btn_answer.config(image="")
            cross_image=PhotoImage(file="C:\\Users\\faraz\\PycharmProjects\\Tkinter\\JumbleWordGame\\wrong.png")
            btn_answer.config(image=cross_image,bg="black")
            btn_answer.photo=cross_image
            my_answer_label.config(text="Wrong")

jumble_up_img=Image.open("C:\\Users\\faraz\\PycharmProjects\\Tkinter\\JumbleWordGame\\Icon.png")
jumble_up_img=ImageTk.PhotoImage(jumble_up_img)
Jumble_up=Label(frame_test,image=jumble_up_img)
Jumble_up.pack(pady=(5,30))

get_started_img=Image.open("C:\\Users\\faraz\\PycharmProjects\\Tkinter\\JumbleWordGame\\Get Started.png")
get_started_img=ImageTk.PhotoImage(get_started_img)

start_game=Button(frame_test,image=get_started_img,borderwidth=0,command=start_game)
start_game.pack(pady=(0,20))

conn.commit()
conn.close()
entry_page.mainloop()

