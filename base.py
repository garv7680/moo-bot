def load_FAQ_data():
    """This method returns a list of questions and answers. The
    lists are parallel, meaning that intent n pairs with response n."""

    # declare question and aanswer arrays
    questions = []
    answers = []

    # open questions text file and read it
    with open("questions.txt") as quest:
        for line in quest:
            questions.append(line.lower().strip())  # Read

    with open("answers.txt") as ans:
        for line in ans:
            answers.append(line.capitalize().strip())

    return questions, answers


def understand(utterance):
    """This method processes an utterance to determine which intent it
    matches. The index of the intent is returned, or -1 if no intent
    is found."""
    global intents  # declare that we will use a global variable
    utterance = utterance.lower()  # force utter to lowercase
    try:
        return intents.index(utterance)
    except ValueError:
        return -1


def generate(intent):
    """This function returns an appropriate response given a user's
    intent."""
    global responses  # declare that we will use a global variable

    if intent == -1:
        return "Sorry, I don't know the answer to that!"

    return responses[intent]


# Load the questions and responses
intents, responses = load_FAQ_data()
