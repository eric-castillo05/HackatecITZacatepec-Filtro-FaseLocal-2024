from typing import Final
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler, ConversationHandler, CallbackContext, MessageHandler, filters
)


TOKEN: Final = '7129178553:AAFDoe-Mx-SdZy47bQwRJkzuOs7rUs-xYRc'
BOT_USERNAME: Final = '@NetRunnersITZ'

# Crea una instancia de la conexión a Redis

import redis

r = redis.Redis(
  host='redis-10364.c325.us-east-1-4.ec2.cloud.redislabs.com',
  port=10364,
  password='9oxEjbS4slyRNmxknio5Ryi8UaasqLYC')
TOKEN: Final = '7129178553:AAFDoe-Mx-SdZy47bQwRJkzuOs7rUs-xYRc'
BOT_USERNAME: Final = '@NetRunnersITZ'

# Estados de la conversación
SEXO,EDAD,FUMADOR,DEDOS_AMARILLOS,ANSIEDAD, PRESION_GRUPO,ENFERMEDAD_CRONICA,FATIGA,ALERGIA,SIBILANCIAS,CONSUMO_ALCOHOL,TOS,DIFICULTAD_RESPIRAR,\
DIFICULTAD_TRAGAR,DOLOR_PECHO,CANCER_PULMON = range(16)


# Comandos
async def start_command(update: Update, context: CallbackContext) -> int:
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='yes')],
        [InlineKeyboardButton("No", callback_data='no')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('¿Estas listo?', reply_markup=reply_markup)
    if start_command == 'no':
        return ConversationHandler.END
    else:
        return SEXO

async def sexo(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Masculino", callback_data='yes')],
        [InlineKeyboardButton("Femenino", callback_data='no')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Cual es tu sexo?", reply_markup=reply_markup)
    return EDAD

async def edad(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = []
    age = 20
    while age <= 99:
        row = []
        for _ in range(3):
            if age > 99:
                break
            row.append(InlineKeyboardButton(str(age), callback_data=str(age)))
            age += 1
        keyboard.append(row)

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="Selecciona tu edad:", reply_markup=reply_markup)
    return FUMADOR



async def fumador(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='yes')],
        [InlineKeyboardButton("No", callback_data='no')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Fumas?", reply_markup=reply_markup)
    return DEDOS_AMARILLOS

async def dedos_amarillos(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='yes')],
        [InlineKeyboardButton("No", callback_data='no')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Tienes dedos amarillos?", reply_markup=reply_markup)
    return ANSIEDAD

async def ansiedad(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='yes')],
        [InlineKeyboardButton("No", callback_data='no')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Tienes Ansiedad?", reply_markup=reply_markup)
    return PRESION_GRUPO

async def presion_grupo(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='yes')],
        [InlineKeyboardButton("No", callback_data='no')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Tienes presion de grupo?", reply_markup=reply_markup)
    return ENFERMEDAD_CRONICA

async def enfermedad_cronica(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='yes')],
        [InlineKeyboardButton("No", callback_data='no')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Tienes alguna enfermedad cronica?", reply_markup=reply_markup)
    return FATIGA

async def fatiga(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='yes')],
        [InlineKeyboardButton("No", callback_data='no')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Tienes Fatiga?", reply_markup=reply_markup)
    return ALERGIA

async def alergia(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='yes')],
        [InlineKeyboardButton("No", callback_data='no')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Tienes Alergia?", reply_markup=reply_markup)
    return SIBILANCIAS

async def sibilancias(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='yes')],
        [InlineKeyboardButton("No", callback_data='no')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Tienes Sibilancia?", reply_markup=reply_markup)
    return CONSUMO_ALCOHOL

async def consumo_alcohol(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='yes')],
        [InlineKeyboardButton("No", callback_data='no')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Consumes Alcohol?", reply_markup=reply_markup)
    return TOS

async def tos(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='yes')],
        [InlineKeyboardButton("No", callback_data='no')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Tienes Tos?", reply_markup=reply_markup)
    return DIFICULTAD_RESPIRAR

async def dificultad_respirar(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='yes')],
        [InlineKeyboardButton("No", callback_data='no')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Tienes dificultad para respirar?", reply_markup=reply_markup)
    return DIFICULTAD_TRAGAR

async def dificultad_tragar(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='yes')],
        [InlineKeyboardButton("No", callback_data='no')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Tienes dificultad para tragar?", reply_markup=reply_markup)
    return DOLOR_PECHO

async def dolor_pecho(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='yes')],
        [InlineKeyboardButton("No", callback_data='no')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Tienes Dolor de Pecho?", reply_markup=reply_markup)
    return CANCER_PULMON

async def cancer_pulmon(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    text  = update.message.text
    await update.message.reply_text(f"Lo siento, te vas a morir.")
    return ConversationHandler.END



# Función para cancelar la conversación
async def cancel(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text('Conversación cancelada.')
    return ConversationHandler.END

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start_command)],
        states={
            SEXO: [CallbackQueryHandler(sexo)],
            EDAD: [CallbackQueryHandler(edad)],
            FUMADOR: [CallbackQueryHandler(fumador)],
            DEDOS_AMARILLOS: [CallbackQueryHandler(dedos_amarillos)],
            ANSIEDAD: [CallbackQueryHandler(ansiedad)],
            PRESION_GRUPO: [CallbackQueryHandler(presion_grupo)],
            ENFERMEDAD_CRONICA: [CallbackQueryHandler(enfermedad_cronica)],
            FATIGA: [CallbackQueryHandler(fatiga)],
            ALERGIA: [CallbackQueryHandler(alergia)],
            SIBILANCIAS: [CallbackQueryHandler(sibilancias)],
            CONSUMO_ALCOHOL: [CallbackQueryHandler(consumo_alcohol)],
            TOS: [CallbackQueryHandler(tos)],
            DIFICULTAD_RESPIRAR: [CallbackQueryHandler(dificultad_respirar)],
            DIFICULTAD_TRAGAR: [CallbackQueryHandler(dificultad_tragar)],
            DOLOR_PECHO: [CallbackQueryHandler(dolor_pecho)],
            CANCER_PULMON: [MessageHandler(filters.TEXT & ~filters.COMMAND, cancer_pulmon)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    app.add_handler(conv_handler)

    # Iniciar el bot
    print('Arrancando...')
    app.run_polling()