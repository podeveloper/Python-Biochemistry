import random
import sys

class Flashcards:
    def __init__(self, file_path):
        self.cards = self.load_questions_and_answers(file_path)
        self.lessons = self.extract_lessons()
        random.shuffle(self.cards)

    def load_questions_and_answers(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        cards = [tuple(line.strip().split('|')) for line in lines]
        return cards

    def extract_lessons(self):
        return list(set(card[0] for card in self.cards))

    def start_flashcards(self):
        try:
            print("Choose a lesson:")
            for i, lesson in enumerate(self.lessons, start=1):
                print(f"{i}-{lesson}")
            print(f"{len(self.lessons) + 1}-All Lessons")

            choice = input("Enter the number of the lesson you want to study: ")

            if choice.isdigit() and 1 <= int(choice) <= len(self.lessons) + 1:
                if int(choice) == len(self.lessons) + 1:
                    filtered_cards = self.cards
                else:
                    selected_lesson = self.lessons[int(choice) - 1]
                    filtered_cards = [card for card in self.cards if card[0] == selected_lesson]

                for card in filtered_cards:
                    print(f"Question: {card[1]}")
                    input("")
                    print(f"Answer: {card[2]}")
                    print("-" * 40)  # Separator line
                    input("")
                    
            else:
                print("Invalid choice. Please enter a valid number.")

        except KeyboardInterrupt:
            print("\nExiting the program.")

if __name__ == "__main__":
    file_path = "questions_and_answers.txt"  # Adjust the file path accordingly

    flashcards_app = Flashcards(file_path)
    flashcards_app.start_flashcards()