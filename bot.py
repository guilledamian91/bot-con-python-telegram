from telegram import Update, ParseMode, Poll, InputMediaPhoto, InputMediaVideo, InlineKeyboardMarkup, InputTextMessageContent
from telegram import InputMediaAudio, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InlineQueryResultGame
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler, ConversationHandler, CallbackQueryHandler, InlineQueryHandler
import time

TOKEN = "5900542355:AAHH4Is8XmgI8kGhK9ECLVGzPGA93QmQMkM"
CHATID = "1775952424"
DIRECCION = "C:\\Users\\guill\\Desktop\\bots con pyhton\\"
USER, CORREO = range(2)
OPINION, NO = range(2)


# def echo(update:Updater, context:CallbackContext):
#     print(update.message.chat.id)
    
    # inputPhoto= InputMediaPhoto(open(DIRECCION + "bot.png","rb"))
    # inputVideo = InputMediaVideo(open(DIRECCION + "gatito.mp4", "rb"))
    # inputAudio = InputMediaAudio(open(DIRECCION + "maullido_de_un_gato.mp3","rb"))
    
    # update.message.reply_media_group([inputPhoto,inputVideo])
    
    # update.message.reply_poll("¿Te gusta el grupo?", ["si","no","nose"], 
    #     is_anonymous = False, allows_multiple_answers=True, type=Poll.QUIZ, correct_option_id = 0,
    #     explanation="Casi adivinas", open_period=100)
    
    # LAT= -34.6037389
    # LON= -58.3815704
    # update.message.reply_text("Espera ya te envio mi ubicacion...")
    # time.sleep(5)
    # i= update.message.reply_text("Esta es mi ubicacion")
    # time.sleep(5)
    # update.message.reply_location(LAT,LON,f"{i}",reply_to_message_id=update.message.message_id)
    
    
    # update.message.reply_animation(open("C:\\Users\\guill\\Desktop\\bots con pyhton\\gato.gif","rb"),
    #     reply_to_message_id=update.message.message_id,caption="Holi")
    
    # update.message.reply_document(open("C:\\Users\\guill\\Desktop\\bots con pyhton\\cv.pdf","rb"),
    #     caption= "pdf de CV",thumb=open("C:\\Users\\guill\\Desktop\\bots con pyhton\\bot.png","rb"))
    
    #update.message.reply_video(open("C:\\Users\\guill\\Desktop\\bots con pyhton\\gatito.mp4","rb"),
    #reply_to_message_id=update.message.message_id,caption="Video Gracioso")
    
    
    # update.message.reply_audio(open("C:\\Users\\guill\\Desktop\\bots con pyhton\\maullido_de_un_gato.mp3",'rb'), 
    #   title="gato",reply_to_message_id=update.message.message_id, caption="Audio de un gato", 
    #   thumb=open("C:\\Users\\guill\\Desktop\\bots con pyhton\\gato.png","rb"))
    
    
    
    #update.message.reply_audio("https://www.elongsound.com/images/mp3/maullido_de_un_gato.mp3", 
    #   title="gato",reply_to_message_id=update.message.message_id, caption="Audio de un gato")
    
    
    # update.message.reply_text("<a href= 'https://www.youtube.com/channel/UC5SgHQm5RYY-KvxwDYxZUTw'>Guillermo</a>",parse_mode=ParseMode.HTML, reply_to_message_id=update.message.message_id)
    #update.message.reply_photo("https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/800px-Python.svg.png",
    #     reply_to_message_id=update.message.message_id, caption="imagen de lenguaje pyhton")

    #update.message.reply_photo(open("C:\\Users\\guill\\Desktop\\bots con pyhton\\bot.png", "rb"),
    #       reply_to_message_id=update.message.message_id)


# def notificaciones(update:Update, context:CallbackContext):
#     if update.message == None:
#         update.edited_message.reply_text("Has editado tu mensaje")
#     else:
#         update.message.reply_text("Recibi tu mensaje sin editar", reply_to_message_id = update.message.message_id)

# def AddUsers(update:Updater,callback:CallbackContext):
#     update.message.reply_text(f"Bienvenido al grupo @{update.message.new_chat_members[0].first_name}")

# def TiempoSaludo(context):
#     context.bot.send_message(chat_id = context.job.context, text="te saludo desde mi funcion tiemposaludo")

# def saludar(update:Update,context:CallbackContext):
#     context.job_queue.run_repeating(TiempoSaludo, int(context.args[0], context= update.message.chat_id))
#     update.message.reply_text(f"te saludo desde arg {context.args}")

# def IniciarCAllback(update,callback):
#     update.message.reply_text("Hola, ¿Como es tu usuario?")
    
#     return USER

# def UserCAllback(update,callback):
#     update.message.reply_text(f"hola {update.message.text}, ¿Como es tu correo?")
    
#     return CORREO

# def CorreoCAllback(update,callback):
#     update.message.reply_text("Correo recibido de forma exitosa:)")
    
#     return ConversationHandler.END

# def ErrorCAllback(update,callback):
    # update.message.reply_text("Algo salió mal, prueba nuevamente :(")
    
# def admin(update,callback_context):
#     callback_context.bot.promote_chat_member(update.message.chat_id, update.message.from_user.id, can_change_info=True, can_delete_messages=True, can_invite_users=True,
#         can_restrict_members=True, can_pin_messages=True, can_promote_members=True)
    
# def actualizar(update, callback_context):
#     chat_id = update.message.chat.id
#     bot = callback_context.bot
#     bot.set_chat_title(chat_id,"Este es el titulo de botinstructor")
#     bot.set_chat_description(chat_id, "Espero que hagas muchos bots amigos")
    
#     photo = open("bot.png","rb")
#     bot.set_chat_photo(chat_id, photo)

# def fijarComentario(update, callback_context):
#     message = update.message.reply_to_message
#     callback_context.bot.pin_chat_message(message.chat.id, message.message_id)

# def pregunta (update: Update, context:CallbackContext):
#     buttons = [[
#         KeyboardButton("Me gustó mucho"),
#         KeyboardButton("No me gustó")
#     ]]
    
#     keyboardMarkup = ReplyKeyboardMarkup(buttons, one_time_keyboard=True)
    
#     update.message.reply_text("¿Te gustó nuestro producto?", reply_markup= keyboardMarkup)
    
# def enlace (update: Update, context:CallbackContext):
#     buttons =[[
#         InlineKeyboardButton("Zapatos", url= "https://www.mercadolibre.com.ar/")
#     ],
#     [
#         InlineKeyboardButton("Remeras", url= "https://www.mercadolibre.com.ar/")   
#     ]]
    
#     ReplyKeyboardMarkup = InlineKeyboardMarkup(buttons)
    
#     update.message.reply_text("¿Que productos quieres ver?", reply_markup=ReplyKeyboardMarkup)

# def producto (update: Update, context:CallbackContext):
#     buttons =[[
#         InlineKeyboardButton("Si",callback_data="Si quiero")
#     ],
#     [
#         InlineKeyboardButton("No",callback_data="La proxima")   
#     ]]
    
#     ReplyKeyboardMarkup = InlineKeyboardMarkup(buttons)
    
#     update.message.reply_text("¿Quieres agregar productos?", reply_markup=ReplyKeyboardMarkup)

# def repuesta (update:Update, context:CallbackContext):
#     consulta= update.callback_query
#     consulta.answer("Perfecto, recibi la orden")
#     consulta.edit_message_text(f"Hemos recibido tu respuesta como: {consulta.data}")

# def opinion (update: Update, context:CallbackContext):
#     buttons =[[
#         InlineKeyboardButton("Bien",callback_data="Buena")
#     ],
#     [
#         InlineKeyboardButton("Mal",callback_data="Mala")   
#     ]]
    
#     ReplyKeyboardMarkup = InlineKeyboardMarkup(buttons)
    
#     update.message.reply_text("¿Como fue tu experiencia en el grupo?", reply_markup=ReplyKeyboardMarkup)  
#     return OPINION
# def si(update:Update, context:CallbackContext):
#     consulta= update.callback_query
#     consulta.answer()
#     consulta.edit_message_text("Muchas gracias por tu opinion")
#     return ConversationHandler.END
# def no(update:Update, context:CallbackContext):
#     consulta = update.callback_query
#     consulta.answer()
    
#     buttons =[
#         [
#             InlineKeyboardButton("Falta de contenido", callback_data= "mal"),
#             InlineKeyboardButton("Mucha falta de respeto", callback_data= "falta de respeto"),
#         ],
#         [
#             InlineKeyboardButton("Otro motivo", callback_data= "otro motivo"),
#         ]
#     ]
    
#     KeyboardMarkup = InlineKeyboardMarkup(buttons)
#     consulta.edit_message_text("Lo sentimos mucho, ¿cual fue la razon?", reply_markup =KeyboardMarkup )
#     return NO
# def motivo(update:Update, context:CallbackContext):
    # consulta= update.callback_query
    # consulta.answer()
    # consulta.edit_message_text("Gracias por colaborar")
    # return ConversationHandler.END

# def miBotEnLinea(update, callback):
#     query= update.inline_query.query
#     if query == "":
#         query = "Vacio"
 
#     resultados = [
#         InlineQueryResultArticle("1","Mayusculas", InputTextMessageContent(query.upper()), 
#                 description="Convierto todo en masyuscula"),
#         InlineQueryResultArticle("2","Negrita", InputTextMessageContent(f"*{query}*", parse_mode= ParseMode.MARKDOWN_V2)),
#         InlineQueryResultArticle("3","Cursiva", InputTextMessageContent(f"_{query}_", parse_mode= ParseMode.MARKDOWN_V2)),
#         InlineQueryResultArticle("4","Subrayado", InputTextMessageContent(f"<u>{query}</u>", parse_mode= ParseMode.HTML)),
#     ]
#     update.inline_query.answer(resultados, is_personal = False)     

# def baneo(update, callback_context):
    
#     insultos=["boludo", "pelotudo"]
#     message_text= update.message.text
    
#     if any(insulto in message_text.lower() for insulto in insultos):
#         if callback_context.chat_data.get(update.message.from_user.id) == True:
#             update.message.reply_text("Por favor te avise que no pongas esas palabras, te voy a explusar", reply_to_message_id= update.message.message_id)
#             callback_context.bot.ban_chat_member(update.message.chat.id, update.message.from_user.id)
#         else:
#             callback_context.chat_data[update.message.from_user.id] = True
#             update.message.reply_text("Primer aviso no pongas malas plabras sino seras baneado y explusado del grupo",reply_to_message_id=update.message.message_id)
        
def start(update: Update, context:CallbackContext):
    update.message.reply_game("destructor")

def inlineQuery (update: Update, context: CallbackContext):
    results=[
        InlineQueryResultGame(1,"destructor")
    ]
    update.inline_query.answer(results)
    
    
def main():
    
    updater = Updater(TOKEN)
    
    dispatcher = updater.dispatcher
    
    # dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    
    # dispatcher.add_handler(MessageHandler(filters=Filters.text & ~ Filters.update.edited_message, callback= notificaciones))
    
    # dispatcher.add_handler(MessageHandler(filters= Filters.status_update.new_chat_members, callback=AddUsers))
    
    # updater.bot.send_message(CHATID, "bienvenido a mi chat")
    
    # dispatcher.add_handler(CommandHandler("saludo",saludar))
    
    # entry_point = [
    #     CommandHandler("Iniciar",IniciarCAllback)
    # ]
    # state = {
    #     USER:[
    #         MessageHandler(filters= Filters.text, callback= UserCAllback)
    #         ],
    #     CORREO:[
    #         MessageHandler(filters= Filters.regex(r"^([a-z0-9_\.-]+)@([a-z0-9_\.-]+)\.([a-z0-9_\.-]+)$"), callback= CorreoCAllback)
    #         ]
    # }
    
    # errorUsuario= [
    #     MessageHandler(filters= Filters.text, callback= ErrorCAllback)
    #         ]
    
    # dispatcher.add_handler(ConversationHandler(entry_point ,state, errorUsuario))
    
    # dispatcher.add_handler(CommandHandler('admin',callback= admin))
    
    # dispatcher.add_handler(CommandHandler('Actualizar',callback= actualizar))
    
    # dispatcher.add_handler(CommandHandler("fijar",callback= fijarComentario))
    
    # dispatcher.add_handler(CommandHandler("Empezar", pregunta))
    
    # dispatcher.add_handler(CommandHandler("productos", enlace))
    
    # dispatcher.add_handler(CommandHandler("productos", producto))
    # dispatcher.add_handler(CallbackQueryHandler(repuesta))
    
    # entry= [CommandHandler("opinion", opinion)]
    # states={
    #     OPINION: [
    #         CallbackQueryHandler(si, pattern= r'^Buena$'),
    #         CallbackQueryHandler(no, pattern= r'^Mala$')
    #     ],
    #     NO:[
    #         CallbackQueryHandler(motivo)
    #     ]
    # }
    
    # fallback=[]
    
    # dispatcher.add_handler(ConversationHandler(entry, states, fallback))
    
    # dispatcher.add_handler(InlineQueryHandler(miBotEnLinea))
    
    # dispatcher.add_handler(MessageHandler(filters=Filters.text, callback= baneo ))
    
    dispatcher.add_handler(CommandHandler("start",start))
    dispatcher.add_handler(InlineQueryHandler(inlineQuery))
    
    updater.start_polling()
    
    updater.idle()
    
if __name__== "__main__":
    main()