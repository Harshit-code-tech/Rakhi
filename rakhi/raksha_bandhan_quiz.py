import random
import time
from progress.bar import IncrementalBar

import wikipedia



class Question:
    def __init__(self, prompt, answer, choices=None, explanation=None, difficulty="Easy"):
        self.prompt = prompt
        self.answer = answer
        self.choices = choices
        self.explanation = explanation
        self.difficulty = difficulty




# Define the questions and answers
questions = [
    Question(
        "What is the literal meaning of 'Raksha Bandhan'?",
        "Bond of Protection",
        choices=["Bond of Protection", "Brotherhood Celebration", "Thread of Unity"],
        difficulty="Easy"
    ),
    Question(
        "Which festival celebrates the bond between siblings?",
        "Raksha Bandhan",
        choices=["Diwali", "Raksha Bandhan", "Navratri"],
        difficulty="Easy"
    ),
    Question(
        "Which item is traditionally tied on the brother's wrist?",
        "Rakhi",
        choices=["Bracelet", "Necklace", "Rakhi"],
        difficulty="Easy"
    ),
    Question(
        "What is the significance of Raksha Bandhan?",
        "Symbolizes love and protection between siblings",
        choices=["Symbolizes love and protection between siblings", "Celebrates harvest season", "Honors teachers"],
        difficulty="Easy"
    ),
    Question(
        "In which month is Raksha Bandhan usually celebrated?",
        "August",
        choices=["August", "April", "October"],
        difficulty="Easy"
    ),
    Question(
        "What is the other name for Raksha Bandhan in India?",
        "Rakhi Purnima",
        choices=["Makar Sankranti", "Karva Chauth", "Rakhi Purnima"],
        difficulty="Medium"
    ),
    Question(
        "What do sisters typically wish for their brothers on Raksha Bandhan?",
        "Long and healthy life",
        choices=["Long and healthy life", "Wealth and success", "Happiness and joy"],
        difficulty="Easy"
    ),
    Question(
        "What do brothers typically promise their sisters on Raksha Bandhan?",
        "Protection and support",
        choices=["Cooking delicious meals", "Protection and support", "Buying gifts"],
        difficulty="Easy"
    ),
    Question(
        "Which Indian mythological story is associated with Raksha Bandhan?",
        "Krishna and Draupadi",
        choices=["Ramayana", "Mahabharata", "Krishna and Draupadi"],
        difficulty="Medium"
    ),
    Question(
        "Which famous poet wrote a poem dedicated to Raksha Bandhan?",
        "Rabindranath Tagore",
        choices=["Rabindranath Tagore", "Sarojini Naidu", "Pablo Neruda"],
        difficulty="Hard"
    ),
    Question(
        "What is 'Lumba Rakhi'?",
        "A type of rakhi tied by sisters-in-law on their brothers-in-law",
        choices=["A special sweet", "A type of dance", "A type of rakhi tied by sisters-in-law on their brothers-in-law"],
        difficulty="Medium"
    ),
    Question(
        "What is 'Jhoolan Leela' associated with Raksha Bandhan?",
        "Swinging of Lord Krishna and Radha",
        choices=["Lighting lamps", "Singing bhajans", "Swinging of Lord Krishna and Radha"],
        difficulty="Medium"
    ),
    Question(
        "Which historical event is connected to Raksha Bandhan and Emperor Humayun?",
        "Protection of Rani Karnavati by Humayun",
        choices=["Battle of Plassey", "Treaty of Versailles", "Protection of Rani Karnavati by Humayun"],
        difficulty="Hard"
    ),
    Question(
        "What is the main ingredient used to make traditional sweets during Raksha Bandhan?",
        "Milk and sugar",
        choices=["Flour and water", "Rice and vegetables", "Milk and sugar"],
        difficulty="Easy"
    ),
    Question(
        "The festival falls in the month of?",
        "Shravan",
        choices=["Kartika", "Chaitra", "Shravan"],
        difficulty="Hard"
    ),
]


# Password for accessing the quiz
PASSWORD = "rakhi2023"
MAX_ATTEMPTS = 5
# Password for accessing the quiz
PASSWORD = "rakhi2023"
MAX_ATTEMPTS = 5
explanation_cache = {}


def ask_question(question, question_number):
    print(f"{question_number}) Difficulty: {question.difficulty}")
    print(question.prompt)
    if question.choices:
        for i, choice in enumerate(question.choices):
            print(f"{i + 1}. {choice}")

        start_time = time.time()
        while True:
            try:
                user_choice = int(input("Enter your choice (1, 2, 3, ...): ")) - 1
                elapsed_time = time.time() - start_time
                print(f"Time taken: {elapsed_time:.2f} seconds")

                if 0 <= user_choice < len(question.choices):
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        user_answer = question.choices[user_choice]
    else:
        user_answer = input().strip()
    return user_answer.lower(), elapsed_time


def run_quiz(questions):
    score = 0
    total_time = 0
    time_per_question = []
    random.shuffle(questions)
    progress_bar = IncrementalBar("Progress", max=len(questions))

    for i, question in enumerate(questions, start=1):
        print("\n" + "=" * 40)
        print("\n" + "=" * len(question.prompt))
        user_answer, time_taken = ask_question(question, i)
        total_time += time_taken
        time_per_question.append(time_taken)

        if user_answer.lower() == question.answer.lower():
            print("Correct!")
            score += 1
            provide_explanation(question.answer)
        else:
            print("Incorrect. The correct answer is:", question.answer)
            provide_explanation(question.answer)

        time.sleep(2)  # Pause before the next question
        progress_bar.next()
        print("\n" + "=" * 40)

    progress_bar.finish()
    print("\nQuiz completed! You scored", score, "out of", len(questions))
    print("Total time taken:", total_time)
    for i, time_taken in enumerate(time_per_question, start=1):
        print(f"Time taken for Question {i}: {time_taken:.2f} seconds")


def provide_explanation(topic):
    if topic in explanation_cache:
        print("\nExplanation (from cache):")
        print(explanation_cache[topic])
    else:
        try:
            page_summary = wikipedia.summary(topic)
            explanation_cache[topic] = page_summary
            print("\nExplanation:")
            print(page_summary)
        except wikipedia.exceptions.DisambiguationError as e:
            print("\nExplanation: The topic is ambiguous. Please check on Wikipedia for more information.")
        except wikipedia.exceptions.PageError as e:
            print("\nExplanation: No detailed information found on Wikipedia.")



def main():
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        password = input("Enter the password to start the quiz: ")
        if password == PASSWORD:
            print("\nWelcome to the Raksha Bandhan Quiz!")
            print("Test your knowledge about this special festival.\n")
            run_quiz(questions)
            break
        else:
            attempts += 1
            remaining_attempts = MAX_ATTEMPTS - attempts
            if remaining_attempts > 0:
                print("Incorrect password. You have", remaining_attempts, "attempts left.\n")
            else:
                print("Maximum attempts reached. Exiting the program.\n")
                break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nQuiz interrupted. Exiting the program.")
    except Exception as e:
        print("An error occurred:", e)