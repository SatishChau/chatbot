# from nturl2path import url2pathname
# from django import urls
# from telegram import *
# from telegram.ext import *
# import logging

# class button(object):


#     def button(update: Update, context: CallbackContext) -> None:
#         """Parses the CallbackQuery and updates the message text."""
#         query = update.callback_query

#         # CallbackQueries need to be answered, even if no notification to the user is needed
#         # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
#         query.answer()

#         # query.edit_message_text(text=f"Selected option: {query.data}")
#         if query.data == '1':
#             context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to Computer Department")
#             context.bot.send_message(chat_id=update.effective_chat.id, text="Enter /semester")
#         if query.data=='comp_sem_1':
#             context.bot.send_message(chat_id=update.effective_chat.id, urls={"https://drive.google.com/drive/folders/1Ici7ybU6uwf6iWNOEZR4wVVXSoYDW0mp?usp=sharing"})
#         if query.data == '3':
#             context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to Electrical Department")
#             context.bot.send_message(chat_id=update.effective_chat.id, text="Enter /semester")
#         #   query.edit_message_text("Welcome to Computer Department")
#         #   query.message_text("HOD: Chirag Thakar")

#         # query.edit_message_text("Enter /semester")