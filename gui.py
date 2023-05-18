from chatgpt import ChatGPT
import tkinter as tk
from PIL import ImageTk, Image


def chatbot_selection(n):
    if n=="ChatBot_dummy":
        chatbot = ChatBot_dummy()
    if n=="ChatGPT":
        chatbot = ChatGPT()
    
    chatbot.start()
    return chatbot


def main():
    # Crear un chatbot
    #chatbot = chatbot_selection("ChatBot_dummy")
    chatbot = chatbot_selection("ChatGPT")


    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title('ER-GPT')
    ventana.geometry('500x800')
    ventana.configure(bg='#FFFFFF')

    # Crear el marco principal
    marco_principal = tk.Frame(ventana, bg="#E1E1E1")
    marco_principal.pack(fill=tk.BOTH, expand=True)

    # Panel de sistema
    marco_sistema = tk.Frame(marco_principal, bg="#E1E1E1", height=5)
    marco_sistema.pack(fill=tk.BOTH, expand=False)
    title_sistema= tk.Label(marco_sistema, text="SYSTEM", wraplength=250, bg="#333333",  fg="white", padx=10, pady=5, font=("Arial", 11))
    title_sistema.pack(fill=tk.BOTH, pady=(5,0), padx=(2, 17))
    mensaje_sistema= tk.Label(marco_sistema, text="", wraplength=350, bg="#999999", padx=10, pady=5, font=("Arial", 11), height=5)
    mensaje_sistema.pack(fill=tk.BOTH, pady=(0,5), padx=(2, 17))
    

    # Crear canvas conversacion
    canvas = tk.Canvas(marco_principal, bg="#333333")
    canvas.pack(fill=tk.BOTH, expand=True)
    #canvas.pack_propagate(0)
    #canvas.config(width=300, height=500)

    marco_conversacion = tk.Frame(canvas, bg="#333333")
    marco_conversacion.pack(fill=tk.BOTH, expand=True)
    canvas.create_window( (canvas.winfo_width()/ 2, canvas.winfo_height()/2), window=marco_conversacion, anchor="nw", width=480)

    # Configurar el marco para que ocupe todo el ancho del canvas
    marco_conversacion.columnconfigure(0, weight=1)

    #scrollbar
    scrollbar = tk.Scrollbar(canvas, orient=tk.VERTICAL)
    scrollbar.config(command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.config(yscrollcommand=scrollbar.set)

    def scroll(event):
        canvas.yview_scroll(-1*(event.delta//120), "units")

    canvas.bind_all("<MouseWheel>", scroll)


    # Cargar imagen del icono del chatbot y del usuario
    image_chatbot = Image.open("images/chatbot.png")
    image_chatbot = image_chatbot.resize((50, 50))
    icon_chatbot = ImageTk.PhotoImage(image_chatbot)

    image_user = Image.open("images/user.png")
    image_user = image_user.resize((50, 50))
    icon_user = ImageTk.PhotoImage(image_user)


    # Crear el campo de entrada de texto
    entrada_texto = tk.Entry(marco_principal, bd=0, bg="#F1F0F0", fg="#333", font=("Arial", 12))
    entrada_texto.pack(fill=tk.X, pady=(10, 10), padx=20, ipady=10)


    def enviar_mensaje(event=None):
        mensaje_usuario = entrada_texto.get()
        if mensaje_usuario:

            # Crear el marco del usuario
            marco_usuario = tk.Frame(marco_conversacion,  bg="#333333")
            marco_usuario.pack(padx=10, pady=5, anchor="e", fill=tk.BOTH)
            # Crear una etiqueta para mostrar el nombre de usuario
            #nombre_usuario_label = tk.Label(marco_usuario, text="Tú", font=("Arial", 11, "bold"), bg="#DCF8C6", fg="#333")
            #nombre_usuario_label.pack(anchor="e", pady=5)

            #mensaje_usuario_bocadillo = tk.Frame(marco_usuario, bg="#DCF8C6")
            #mensaje_usuario_bocadillo.pack(padx=10, pady=5, anchor="e")
            mensaje_usuario_label= tk.Label(marco_usuario, text=mensaje_usuario, wraplength=250, bg="#DCF8C6", padx=10, pady=5, font=("Arial", 11), anchor="e")
            mensaje_usuario_label.pack(anchor="e", pady=5)
            entrada_texto.delete(0, tk.END)
            # Hacer scroll hasta el final de la ventana
            marco_principal.update_idletasks()

            # Crear una etiqueta para mostrar la imagen del usuario
            imagen_usuario_label = tk.Label(marco_usuario, image=icon_user, bg="#E1E1E1")
            imagen_usuario_label.image = icon_user
            imagen_usuario_label.pack(side=tk.RIGHT)


            #marco_principal.yview_moveto(1)
            # Esperar un momento antes de enviar la respuesta del chatbot
            ventana.after(10, enviar_respuesta_chatbot, mensaje_usuario)
            

    def enviar_respuesta_chatbot(mensaje_usuario):
        mensaje_chatbot, system_chatbot = chatbot.response(mensaje_usuario) #"Hola, soy un chatbot y he recibido tu mensaje"

        # Mensaje SYSTEM
        mensaje_sistema.config(text=system_chatbot)

        # Crear el marco del chatbot
        marco_chatbot = tk.Frame(marco_conversacion, bg="#333333")
        marco_chatbot.pack(padx=10, pady=(10, 5), anchor="w")
        mensaje_chatbot_label = tk.Label(marco_chatbot, text=mensaje_chatbot, wraplength=250, bg="#F1F0F0", padx=10, pady=5, font=("Arial", 11), anchor="w")
        mensaje_chatbot_label.pack(anchor="w", pady=5)
        # Crear una etiqueta para mostrar la imagen del chatbot
        imagen_chatbot_label = tk.Label(marco_chatbot, image=icon_chatbot, bg="#E1E1E1")
        imagen_chatbot_label.image = icon_chatbot
        imagen_chatbot_label.pack(side=tk.LEFT)

    
    #Crear el botón de enviar
    boton_enviar = tk.Button(marco_principal, text="Enviar", bg="#007AFF", fg="#FFF", font=("Arial", 12, "bold"), bd=0, command=enviar_mensaje)
    boton_enviar.pack(pady=(0, 10), padx=10, anchor="e")


    # Asociar la tecla Enter con la función responder
    entrada_texto.bind('<Return>', enviar_mensaje)

    #Ejecutar la ventana
    ventana.mainloop()


class ChatBot_dummy():

    def start(self):
        pass

    def response(self, mensaje_usuario):
        return "Soy un chatbot y te escucho. Tu mensaje ha sido el siguiente: " + mensaje_usuario, "SYSTEM MESSAGE"
    
    


if __name__ == "__main__":
    main()
