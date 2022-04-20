import discord
from base import load_FAQ_data
import re
import spacy
nlp = spacy.load("en_core_web_sm")

intents, responses = load_FAQ_data()


class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        # if bot is mentioned in message content (returns bool)
        if self.user in message.mentions:
            # get the utterance and generate the response
            # change question to lowercase, replace the @ mention with nothing, Take off the starting and ending white spaces
            utterance = message.content.replace(
                "<@!369651366622396427>", "").replace("<@369651366622396427>", "").rstrip().lstrip()

            response = "Sorry, I don't know the answer to that!"
            for i in range(len(intents)):
                x = re.search(intents[i], utterance)
                if x:
                    response = responses[i]
                    break
            # Responds to hello, bye and what is up
            if utterance == "hello" or utterance == "hi" or utterance == "hey":
                response = "Moooooo :smile:"
            if utterance == "bye" or utterance == "goodbye":
                response = "Moo :pensive:"
            if utterance == "what is up?":
                response = "Moothing :cow:"
            ch = client.get_channel(934974777767104522)
            await ch.send(f"```{message.author}\n{utterance}\n\nAnswer: {response}```")
            #{time.asctime( time.localtime(time.time()))}
            print()
            doc = nlp(utterance)

        array = []
        for matches in doc.ents:
            array.append(matches.text)

        if response == "Sorry, I don't know the answer to that!":
            if not len(array) == 0:
                response = f"Sorry i dont know understand what you mean by {array[0]}. Ask questions about only cows please."
            else:
                response = f"Sorry i dont know understand what you mean by that. Ask questions about only cows please."
            # send the response
            await message.channel.send(response)


            # await message.send(me, )
client = MyClient()

client.run("KEY")
