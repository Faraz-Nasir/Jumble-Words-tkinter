from tkinter import *
import random,sqlite3

conn=sqlite3.connect('Jumbled_Words.db')
c=conn.cursor()


entry_page=Tk()
entry_page.title("JumbleUp!")
entry_page.resizable(0,0)
entry_page.geometry('400x400')

Jumble_up=Label(entry_page,text="JumbleUp!",font=("Helvetica","40","bold"))

Jumble_up.pack(pady=20)

def start_game():
    entry_page.destroy()

    global game_window,word_list
    game_window=Tk()
    game_window.title("JumbleUp!")
    game_window.resizable(0,0)
    game_window.geometry('600x600')



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

    global answer_entry,i,question_label,score,check_score_label

    check_score_label=Label(game_window,text=f"Score:-  {score}")
    check_score_label.grid(row=0,column=0)

    conn=sqlite3.connect('Jumbled_Words.db')
    c=conn.cursor()
    c.execute('SELECT * FROM words WHERE ID='+str(i))
    record=c.fetchall()
    print(record[0][1])
    question_label=Label(game_window,text=jumble(record[0][1]),font=("Helvetica",40,"bold"))
    question_label.grid(row=1,column=0,pady=40,sticky=W)


    answer_entry=Entry(game_window,width=20,font=("Helvetica",20))
    answer_entry.grid(row=2,column=0,pady=20)
    global btn_answer,my_answer_label,btn_answer
    btn_answer=Button(game_window,text="Submit",font=("Helvetica",15,"bold"),command=answer)
    btn_answer.grid(row=3,column=0)

    nxt_round = Button(game_window, text="Next", font=("Helvetica", 15, "bold"),command=next)
    nxt_round.grid(row=3, column=0,sticky=E)

    exit_btn=Button(game_window,text="Exit",font=("Helvetica",15,"bold"),command=game_window.destroy)
    exit_btn.grid(row=3,column=1)

    my_answer_label = Label(game_window, text="", font=("Helvetica", 20))
    my_answer_label.grid(row=4, column=0)
def answer():

    if(len(answer_entry.get())==0):
        print("Write Something First")
    else:
        global my_answer_label,score,check_score_label,btn_answer

        btn_answer.config(state=DISABLED)
        answer_submitted=answer_entry.get()
        answer_submitted=str.title(answer_submitted)


        conn=sqlite3.connect('Jumbled_Words.db')
        c=conn.cursor()
        c.execute('SELECT * FROM words WHERE ID='+str(i))
        answerlist=c.fetchall()


        answer=answerlist[0][1]
        answer=str.title(answer)

        if(answer_submitted==answer):
            btn_answer.config(bg="green")
            my_answer_label.config(text="Correct")

            score+=1
            check_score_label.config(text=f"Score:-  {score}")
        else:
            btn_answer.config(bg="red")
            my_answer_label.config(text="Wrong")




start_game=Button(entry_page,text="Start Game",font=("Helvetica",20,"italic"),borderwidth=0,command=start_game)
start_game.pack(pady=20)

conn.commit()
conn.close()
entry_page.mainloop()

