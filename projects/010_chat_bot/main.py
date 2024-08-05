# 1. Import necessary functionality
from difflib import SequenceMatcher
from datetime import datetime


# 2. Create a ChatBot class
class ChatBot:

    # 3. Initialize the class
    def __init__(self, name: str, responses: dict[str, str]) -> None:
        self.name = name
        self.responses = responses  # Store predefined responses

    # 4. Create a function to check the similarity of the user input to the predefined responses
    @staticmethod
    def calculate_similarity(input_sentence: str, response_sentence: str) -> float:
        sequence: SequenceMatcher = SequenceMatcher(a=input_sentence, b=response_sentence)
        return sequence.ratio()

    # 5. Create a function that grabs the best response
    def get_best_response(self, user_input: str) -> tuple[str, float]:
        highest_similarity: float = 0.0
        best_match: str = 'Sorry, I didn\'t understand that.'  # Will only trigger if there's a 0% match

        # 6. Iterate over all predefined responses
        for response in self.responses:
            # 7. Calculate similarity between user input and predefined response
            similarity: float = self.calculate_similarity(user_input, response)
            # 8. Update the highest similarity and best match if current similarity is higher
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match = self.responses[response]

        return best_match, highest_similarity

    # 9. Create the main function of the class
    def run(self) -> None:
        print(f'Hello! My name is {self.name}, how can I help you today?')
        while True:
            user_input: str = input('You: ')
            response, similarity = self.get_best_response(user_input)

            # 10. In case the user asks for the time
            if response == 'GET_TIME':
                response = f'The time is: {datetime.now():%H:%M}'

            print(f'{self.name}: {response} (Similarity: {similarity:.2%})')


# 11. Create a main entry point
def main() -> None:
    responses: dict[str, str] = {
        'hello': 'Hello! How are you today?',
        'how are you': 'Great, thanks! What about you?',
        'what time is it': 'GET_TIME',
        'bye': 'Goodbye! Have a great day!'
    }

    # 12. Create a ChatBot instance and start chatting
    chatbot: ChatBot = ChatBot(name='Bob', responses=responses)
    chatbot.run()


# 13. Run the script
if __name__ == '__main__':
    main()

"""
Homework:
1. Add more responses.
2. Add a way to exit the program through the chat.
3. Add some cool features, like checking for the weather forecast.
4. Make it so that if the accuracy falls below 50%, it returns a default response.

"""
