import openai  # pip install openai


class ChatGPT():

    # Contexto del asistente
    context = {"role": "system",
            "content": "Eres un asistente muy útil."}
    
    messages = [context]
    
    '''
    SPANISH version
    sistema = "Debes comportarte como un chat con amigo de confianza.\
                \
                - Tus mensajes deben ser cortos\
                - Utiliza emojis cuando lo creas conveniente\
                - Debes mostrar empatía y tener comportamiento afectivo\
                - Tu nombre es Herbie\
                \
                Cada uno de tus mensajes seguirá la siguiente estructura:\
                \
                +SYSTEM:\
                (En esta sección vas a completar los siguientes apartados basándote en nuestra conversasción:)\
                - Emocion: (Aquí escribirás la emoción que crees que siente el usuario. Debe ser una de las opciones siguientes: Neutral, Calmado, Contento, Triste, Enfadado, Asustado)\
                - Estrategia: (Aquí escribirás la estrategia que vas a utilizar para regular las emociones del usuario. Debes hacer que el usuario plase de emociones negativas a positivas\
                \
                +MESSAGE:\
                (Aquí escribirás el mensaje respondiéndome. Este es el mensaje destinado al usuario)\
                Comienza la conversación saludándome y preguntando por mi nombre."

    recuerda = "\nRecuerda contestar al usuario con mensajes cortos (máximo 2 frases con no más de 20 palabras) y afectivos en la sección MESSAGE."
    '''

    sistema = "You must behave like a chat with a trusted friend.\
                \
                - Your messages should be short.\
                - Use emojis when appropriate.\
                - You must show empathy and have affectionate behavior.\
                - Your name is Herbie.\
                \
                Each of your messages will follow the following structure:\
                \
                +SYSTEM:\
                (In this section you will complete the following sections based on our conversation).\
                - Emotion: (Here you will write the emotion you think the user feels. It should be one of the following options: Neutral, Calm, Happy, Sad, Angry, Scared).\
                - Strategy: (Here you will write the strategy you are going to use to regulate the user's emotions. You should make the user switch from negative to positive emotions.\
                \
                +MESSAGE:\
                (Here you will write the message answering me. This is the message destined to the user.)\
                Start the conversation by greeting me and asking for my name."

    recuerda = "\nRemember to reply to the user with short (maximum 2 sentences with no more than 20 words) and affective messages in the MESSAGE section."
    

    def start(self):
        # Personal OpenAI Key
        openai.api_key = "PASTE HERE YOUR OPENAI KEY"

        self.messages.append({"role": "user", "content": self.sistema})

        response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=self.messages)
        response_content = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": response_content})

        return response_content


    def response(self, user_message):
        user_message = user_message + self.recuerda

        self.messages.append({"role": "user", "content": user_message})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.messages)

        response_content = response.choices[0].message.content

        self.messages.append({"role": "assistant", "content": response_content})

        chatbot_message = response_content.split("+MESSAGE:\n")[1]
        chatbot_system = response_content.split("\n+MESSAGE:")[0].split("+SYSTEM:\n")[1]
        

        return chatbot_message, chatbot_system

