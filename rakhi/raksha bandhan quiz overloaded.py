import subprocess
from tkinter import *
from tkinter import messagebox
import random
import time
from progress.bar import IncrementalBar
from explain_it import explanations


def __init__(self, root):
    self.root = root
    self.root.geometry("1700x800")
    self.root.title("Raksha Bandhan Program")
    self.root.configure(bg="#FFD700")  # Set the background color of the root window


class RakshaBandhanProgram:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1700x800")
        self.root.title("Raksha Bandhan Program")
        self.root.configure(bg="#FF0000")  # Set the background color of the root window
        self.quiz_data = [
            {
                "question": "What is the literal meaning of 'Raksha Bandhan'?",
                "answers": ["Bond of Protection", "Brotherhood Celebration", "Thread of Unity"],
                "correct_answer": "Bond of Protection"

            },
            {
                "question": "Which festival celebrates the bond between siblings?",
                "answers": ["Diwali", "Raksha Bandhan", "Navratri"],
                "correct_answer": "Raksha Bandhan"
            },
            {
                "question": "Which item is traditionally tied on the brother's wrist?",
                "answers": ["Bracelet", "Necklace", "Rakhi"],
                "correct_answer": "Rakhi"

            },
            {
                "question": "What is the significance of Raksha Bandhan?",
                "answers": ["Symbolizes love and protection between siblings", "Celebrates harvest season",
                            "Honors teachers"],
                "correct_answer": "Symbolizes love and protection between siblings",

            },
            {
                "question": "In which month is Raksha Bandhan usually celebrated?",
                "answers": ["August", "April", "October"],
                "correct_answer": "August",
            },
            {
                "question": "What is the other name for Raksha Bandhan in India?",
                "answers": ["Makar Sankranti", "Karva Chauth", "Rakhi Purnima"],
                "correct_answer": "Rakhi Purnima",

            },
            {
                "question": "What do sisters typically wish for their brothers on Raksha Bandhan?",
                "answers": ["Long and healthy life", "Wealth and success", "Happiness and joy"],
                "correct_answer": "Long and healthy life"
            },
            {
                "question": "What do brothers typically promise their sisters on Raksha Bandhan?",
                "answers": ["Protection and support", "Cooking delicious meals", "Buying gifts"],
                "correct_answer": "Protection and support"
            },
            {
                "question": "Which Indian mythological story is associated with Raksha Bandhan?",
                "answers": ["Krishna and Draupadi", "Ramayana", "Mahabharata"],
                "correct_answer": "Krishna and Draupadi"
            },
            {
                "question": "Which famous poet wrote a poem dedicated to Raksha Bandhan?",
                "answers": ["Rabindranath Tagore", "Sarojini Naidu", "Pablo Neruda"],
                "correct_answer": "Rabindranath Tagore"
            },
            {
                "question": "What is 'Lumba Rakhi'?",
                "answers": ["A type of rakhi tied by sisters-in-law on their brothers-in-law", "A special sweet",
                            "A type of dance"],
                "correct_answer": "A type of rakhi tied by sisters-in-law on their brothers-in-law"
            },
            {
                "question": "What is 'Jhoolan Leela' associated with Raksha Bandhan?",
                "answers": ["Swinging of Lord Krishna and Radha", "Lighting lamps", "Singing bhajans"],
                "correct_answer": "Swinging of Lord Krishna and Radha"
            },
            {
                "question": "Which historical event is connected to Raksha Bandhan and Emperor Humayun?",
                "answers": ["Protection of Rani Karnavati by Humayun", "Battle of Plassey", "Treaty of Versailles"],
                "correct_answer": "Protection of Rani Karnavati by Humayun"
            },
            {
                "question": "What is the main ingredient used to make traditional sweets during Raksha Bandhan?",
                "answers": ["Milk and sugar", "Flour and water", "Rice and vegetables"],
                "correct_answer": "Milk and sugar"
            },
            {
                "question": "The festival falls in the month of?",
                "answers": ["Shravan", "Kartika", "Chaitra"],
                "correct_answer": "Shravan"
            }
        ]

        self.current_question_index = 0
        self.user_answers = []

        self.topframe = Frame(self.root, bg="#FF0000", width=800, height=50)  # Set the background color of the frame
        self.topframe.pack(side=TOP)

        self.leftframe = Frame(self.root, width=400, height=500,
                               bg="#FF0000")  # Set the background color of the frame
        self.leftframe.pack(side=LEFT)

        self.rightframe = Frame(self.root, width=900, height=500,
                                bg="#FF0000")  # Set the background color of the frame
        self.rightframe.pack(side=RIGHT)

        self.main_lbl = Label(self.topframe, font=('Calibri', 25, 'bold'), text="Raksha Bandhan Program", fg="#FF6347",
                              anchor=W)
        self.main_lbl.grid(row=0, column=0)

        self.send_wishes_btn = Button(self.leftframe, font=('Arial', 16, 'bold'), text="Send Wishes", bg="#FF6347",
                                      fg="#FFFFFF", bd=3, padx=10, pady=10, width=12, command=self.send_wishes)
        self.send_wishes_btn.grid(row=2, column=1, padx=10, pady=10)

        self.generate_card_btn = Button(self.leftframe, font=('Arial', 16, 'bold'), text="Generate Card", bg="#FF6347",
                                        fg="#FFFFFF", bd=3, padx=10, pady=10, width=12, command=self.generate_card)
        self.generate_card_btn.grid(row=3, column=1, padx=10, pady=10)

        self.start_quiz_btn = Button(self.leftframe, font=('Arial', 16, 'bold'), text="Start Quiz", bg="#FF6347",
                                     fg="#FFFFFF", bd=3, padx=10, pady=10, width=12, command=self.start_quiz)
        self.start_quiz_btn.grid(row=4, column=1, padx=10, pady=10)

        self.exit_btn = Button(self.leftframe, font=('Arial', 16, 'bold'), text="Exit", bg="#FF6347",
                               fg="#FFFFFF", bd=3, padx=10, pady=10, width=12, command=root.quit)
        self.exit_btn.grid(row=5, column=1, padx=10, pady=10)

        self.result_label = Label(self.rightframe, font=('Calibri', 20, 'bold'), text="Evaluation", anchor=W)
        self.result_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        self.timer_label = Label(self.rightframe, font=('Calibri', 16), text="", anchor=W)
        self.timer_label.grid(row=0, column=1, padx=20, pady=20, sticky="e")
        self.total_time_start = None  # Initialize total time start variable
        self.total_time_elapsed = 0  # Initialize total time elapsed variable

        self.prev_btn = Button(self.rightframe, font=('Calibri', 14), text="Previous", width=10,
                               state=DISABLED, command=self.prev_question)  # Set initial state to DISABLED
        self.prev_btn.grid(row=len(self.quiz_data[self.current_question_index]["answers"]) + 2, column=1, padx=20,
                           pady=5, sticky="e")

        self.result_text = Text(self.rightframe, font=('Arial', 14), height=20,
                                width=60)  # Update font for better readability
        self.result_text.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.option_buttons = []  # List to hold option buttons

        self.explanation_cache = {}  # Initialize explanation_cache here
        self.times_consumed = []  # Store time consumed for each question

        self.quiz_data = self.shuffle_questions()
        self.current_question_index = 0
        self.user_answers = []

        self.progress_bar = IncrementalBar("Progress", max=len(self.quiz_data))
        self.timer_start = None
        self.canvas = Canvas(self.root, width=1700, height=800)
        self.canvas.pack()
        self.gradient_colors = ["#FFD700", "#FF6347", "#87CEEB", "#32CD32", "#FF1493"]  # Define the gradient colors
        self.gradient_index = 0
        self.update_gradient_background()

    def update_gradient_background(self):
        self.canvas.delete("all")
        gradient_color = self.gradient_colors[self.gradient_index]
        self.canvas.create_rectangle(0, 0, 1700, 800, fill=gradient_color, outline="")

        self.draw_pattern_design()

        self.gradient_index = (self.gradient_index + 1) % len(self.gradient_colors)
        self.root.after(5000, self.update_gradient_background)

    def draw_pattern_design(self):
        for x in range(0, 1700, 50):
            for y in range(0, 800, 50):
                self.draw_star(x, y)

    def draw_star(self, x, y):
        colors = ["white", "red", "blue", "green", "yellow", "orange"]  # Define colors for stars
        color = random.choice(colors)
        size = random.randint(10, 30)  # Randomize the size of stars
        self.canvas.create_polygon(x, y + size, x + size, y, x + size * 2, y + size, x + size, y + size * 2, fill=color,
                                   outline="")

    def send_wishes(self):
        messagebox.showinfo("Wishes Sent", "Happy Raksha Bandhan! Wishes sent successfully.")
        # After the user clicks "OK", import and execute hearttry.py
        try:
            subprocess.run(["python3", "hearttry.py"])  # Adjust the command as needed
        except Exception as e:
            print("Error:", e)

    def generate_card(self):
        messagebox.showinfo("Card Generated", "Rakhi card generated successfully.")
        # After the user clicks "OK", import and execute rakhidesign.py
        try:
            import rakhidesign
        except Exception as e:
            print("Error:", e)

    def shuffle_questions(self):
        shuffled_data = list(self.quiz_data)
        random.shuffle(shuffled_data)
        return shuffled_data

    def start_quiz(self):
        self.current_question_index = 0
        self.user_answers = []
        self.result_text.delete("1.0", "end")  # Clear result box
        self.total_time_start = time.time()  # Start the total time timer
        self.show_question()

        # Enable the previous button after starting the quiz
        self.prev_btn.config(state=NORMAL)

    def select_option(self, option_index):
        # Disable option buttons
        for button in self.option_buttons:
            button.config(state=DISABLED)

        selected_answer = self.quiz_data[self.current_question_index]["answers"][option_index]
        correct_answer = self.quiz_data[self.current_question_index]["correct_answer"]
        self.user_answers.append(selected_answer)

        # Calculate and store time taken for the current question
        elapsed_time = int(time.time() - self.timer_start) if self.timer_start else 0
        self.times_consumed.append(elapsed_time)

        # Show the correct answer if the selected option is incorrect
        if selected_answer != correct_answer:
            self.result_text.insert("end", f"\nCorrect Answer: {correct_answer}")

        # Show correctness of selected option
        is_correct = "Correct" if selected_answer == correct_answer else "Incorrect"
        self.result_text.insert("end", f"\nSelected answer: {selected_answer} ({is_correct})")

        # Reset the timer for the current question
        self.timer_start = None

        # Move to the next question after 2 seconds
        self.root.after(2000, self.next_question)

    # Inside the show_question method
    def show_question(self):
        if self.current_question_index < len(self.quiz_data):
            question_data = self.quiz_data[self.current_question_index]
            question_text = f"Q{self.current_question_index + 1}: {question_data['question']}"
            self.result_text.delete("1.0", "end")
            self.result_text.insert("1.0", question_text)
            # Update total time elapsed label
            self.update_total_time_elapsed()

            # Update timer label
            if self.timer_start is None:
                self.timer_start = time.time()
            else:
                elapsed_time = int(time.time() - self.timer_start)
                self.timer_label.config(text=f"Time: {elapsed_time} seconds")

            # Remove the previous option buttons, if any
            for button in self.option_buttons:
                button.destroy()
            self.option_buttons = []

            # Calculate the maximum width required for the options
            max_option_width = max([len(option) for option in question_data["answers"]])

            # Create option buttons for the current question
            for i, option in enumerate(question_data["answers"]):
                option_button = Button(self.rightframe, font=('Calibri', 14), text=option, width=max_option_width + 5,
                                       command=lambda i=i: self.select_option(i))
                option_button.grid(row=i + 2, column=0, padx=20, pady=5, sticky="w")
                self.option_buttons.append(option_button)

            explanation_button = Button(self.rightframe, font=('Calibri', 14), text="Show Explanation",
                                        command=self.show_explanation)
            explanation_button.grid(row=len(question_data["answers"]) + 2, column=0, padx=20, pady=5, sticky="w")
            self.option_buttons.append(explanation_button)

            # Add the "Back" button and enable it
            self.back_btn = Button(self.rightframe, font=('Calibri', 14), text="Back", width=10, state=DISABLED,
                                   command=self.show_question)
            self.back_btn.grid(row=1, column=1, padx=20, pady=5, sticky="e")
            self.option_buttons.append(self.back_btn)
        else:
            self.timer_start = None
            self.result_text.delete("1.0", "end")
            correct_count = sum(1 for user_ans, question_data in zip(self.user_answers, self.quiz_data) if
                                user_ans == question_data["correct_answer"])
            total_questions = len(self.quiz_data)
            result_text = f"Quiz completed!\nYour Score: {correct_count}/{total_questions}"

            # Display time taken for each question
            for i, time_consumed in enumerate(self.times_consumed):
                result_text += f"\nQ{i + 1} Time: {time_consumed} seconds"
            self.result_text.insert("1.0", result_text)

            # Remove the previous option buttons, if any
            for button in self.option_buttons:
                button.destroy()

            self.result_label.config(text="Result")  # Change label text to "Result"

    def show_explanation(self):
        if self.current_question_index < len(self.quiz_data):
            question = self.quiz_data[self.current_question_index]["question"]
            explanation = explanations.get(question, "Explanation not found.")
            self.result_text.delete("1.0", "end")
            self.result_text.insert("1.0", explanation)
            # Enable the "Back" button and disable the "Show Explanation" button
            self.option_buttons[-1].config(state=NORMAL)  # Enable Back button
            self.option_buttons[-2].config(state=DISABLED)  # Disable Show Explanation button
            self.prev_btn.config(state=DISABLED)  # Disable "Previous" button while showing explanation

    def prev_question(self):
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.show_question()
            self.prev_btn.config(state=NORMAL)  # Enable "Previous" button on any question other than the first one
        else:
            self.prev_btn.config(state=DISABLED)  # Disable "Previous" button on the first question
            self.show_question()

    def next_question(self):
        if self.current_question_index < len(self.quiz_data) - 1:
            self.current_question_index += 1
            self.show_question()
            self.prev_btn.config(state=NORMAL)  # Enable "Previous" button when not on the first question
        else:
            self.show_results()

    def show_results(self):
        result_text = "Quiz completed!\n\n"
        correct_count = sum(1 for user_ans, question_data in zip(self.user_answers, self.quiz_data) if
                            user_ans == question_data["correct_answer"])
        total_questions = len(self.quiz_data)

        result_text += f"Your Score: {correct_count}/{total_questions}\n\n"
        # Update total time elapsed label
        self.update_total_time_elapsed()

        for i, (question, time_consumed) in enumerate(zip(self.quiz_data, self.times_consumed)):
            result_text += f"Q{i + 1}: {question['question']} - Time: {time_consumed} seconds\n"

        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", result_text)

        # Remove the previous option buttons, if any
        for button in self.option_buttons:
            button.destroy()

        # Disable the previous button when showing the result
        self.prev_btn.config(state=DISABLED)

        self.result_label.config(text="Result")  # Change label text to "Result"

        # Add the "Back" button in the result view and disable it
        self.back_btn = Button(self.rightframe, font=('Calibri', 14), text="Back", width=10, state=DISABLED,
                               command=self.show_question)
        self.back_btn.grid(row=1, column=1, padx=20, pady=5, sticky="e")
        self.option_buttons.append(self.back_btn)

    def update_total_time_elapsed(self):
        if self.total_time_start:
            self.total_time_elapsed = int(time.time() - self.total_time_start)
            self.timer_label.config(text=f"Total Time: {self.total_time_elapsed} seconds")

    def main(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = Tk()
    app = RakshaBandhanProgram(root)
    app.main()
