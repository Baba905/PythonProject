from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizUi:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizz")
        self.window.minsize(height= 400, width=400)
        self.window.config(pady=30, padx=30, bg = THEME_COLOR)

        self.score = Label(text="Score : 0", bg= THEME_COLOR, fg="white")
        self.score.grid(column=1,row=0)

        self.question_ui = Canvas(width=350, height=300, bg="white")
        self.question_ui_text = self.question_ui.create_text(175, 150,width=300,text="Some Questions", font=("Arial",20,"italic"))
        self.question_ui.grid(column=0, row =1, columnspan=2, pady=50,padx=50)


        true_button_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_button_image, highlightthickness=0)
        self.true_button.grid(column=0, row=2)
        self.true_button["command"] = self.true_response

        false_button_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_image,highlightthickness=0)
        self.false_button.grid(column=1,row=2)
        self.false_button["command"] = self.false_response

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.question_ui.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_ui.itemconfig(self.question_ui_text, text=q_text)
        else :
            self.question_ui.itemconfig(self.question_ui_text, text="You reach the last question")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_response(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        #self.get_next_question()


    def false_response(self):

        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        #self.get_next_question()


    def give_feedback(self, is_right):
        if is_right:
            self.question_ui.config(bg="green")
        else:
            self.question_ui.config(bg="red")
        self.window.after(1000, self.get_next_question)