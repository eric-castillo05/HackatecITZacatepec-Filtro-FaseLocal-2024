from typing import Final
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler, ConversationHandler, CallbackContext, MessageHandler, filters)
import redis
import joblib 
import pandas as pd
import uuid

data = {}

TOKEN: Final = '7129178553:AAFDoe-Mx-SdZy47bQwRJkzuOs7rUs-xYRc'
BOT_USERNAME: Final = '@NetRunnersITZ'

model = joblib.load('models\model.joblib')
r = redis.Redis(
  host='redis-10364.c325.us-east-1-4.ec2.cloud.redislabs.com',
  port=10364,
  password='9oxEjbS4slyRNmxknio5Ryi8UaasqLYC')

# Temas
SEXO,EDAD,FUMADOR,DEDOS_AMARILLOS,ANSIEDAD, PRESION_GRUPO,ENFERMEDAD_CRONICA,FATIGA,ALERGIA,SIBILANCIAS,CONSUMO_ALCOHOL,TOS,DIFICULTAD_RESPIRAR,\
DIFICULTAD_TRAGAR,DOLOR_PECHO,CANCER_PULMON = range(16)


# Comandos
async def start_command(update: Update, context: CallbackContext) -> int:
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='yes')],
        [InlineKeyboardButton("No", callback_data='no')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Empezar encuesta', reply_markup=reply_markup)
    return SEXO

async def sexo(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    answer = query.data  
    if answer == 'no':
        await query.answer()
        await query.edit_message_text("Has cancelado la conversación.")
        return ConversationHandler.END
    else:
        await query.answer()
        keyboard = [
            [InlineKeyboardButton("Masculino", callback_data='2')],
            [InlineKeyboardButton("Femenino", callback_data='1')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="¿Cuál es tu sexo?", reply_markup=reply_markup)
        return EDAD

async def edad(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    answer = query.data
    data['Sexo'] = int(answer)
    await query.answer()
    
    # Display the keyboard for selecting age
    keyboard = []
    age = 15
    while age <= 95:
        row = []
        for _ in range(3):
            if age > 99:
                break
            row.append(InlineKeyboardButton(str(age), callback_data=str(age)))
            age += 1
        keyboard.append(row)

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="Selecciona tu edad:", reply_markup=reply_markup)
    
    # Return the FUMADOR state to continue the conversation flow
    return FUMADOR


async def fumador(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    answer = query.data
    data['Edad'] = int(answer)  
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='2')],
        [InlineKeyboardButton("No", callback_data='1')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Fumas?", reply_markup=reply_markup)
    return DEDOS_AMARILLOS


async def dedos_amarillos(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    answer = query.data
    data['Fumador'] = int (answer)
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='2')],
        [InlineKeyboardButton("No", callback_data='1')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Tienes dedos amarillos?", reply_markup=reply_markup)
    return ANSIEDAD

# Repeat this pattern for other functions


async def ansiedad(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    answer = query.data
    data['dedos amarillos'] = int(answer)
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='2')],
        [InlineKeyboardButton("No", callback_data='1')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Tienes Ansiedad?", reply_markup=reply_markup)
    return PRESION_GRUPO

async def presion_grupo(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    answer = query.data
    data['Ansiedad'] = int(answer)
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='2')],
        [InlineKeyboardButton("No", callback_data='1')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Tienes presion de grupo?", reply_markup=reply_markup)
    return ENFERMEDAD_CRONICA

async def enfermedad_cronica(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    answer = query.data
    data['presion de grupo'] = int(answer)
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='2')],
        [InlineKeyboardButton("No", callback_data='1')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Tienes alguna enfermedad cronica?", reply_markup=reply_markup)
    return FATIGA

async def fatiga(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    answer = query.data
    data['enfermedad cronica'] = int(answer)
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='2')],
        [InlineKeyboardButton("No", callback_data='1')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Tienes Fatiga?", reply_markup=reply_markup)
    return ALERGIA

async def alergia(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    answer = query.data
    data['fatiga'] = int(answer)
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='2')],
        [InlineKeyboardButton("No", callback_data='1')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Tienes Alergia?", reply_markup=reply_markup)
    return SIBILANCIAS

async def sibilancias(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    answer = query.data
    data['Alergia'] = int(answer)
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='2')],
        [InlineKeyboardButton("No", callback_data='1')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Tienes Sibilancia?", reply_markup=reply_markup)
    return CONSUMO_ALCOHOL

async def consumo_alcohol(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    answer = query.data
    data['Sibilancias'] = int(answer)
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='2')],
        [InlineKeyboardButton("No", callback_data='1')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Consumes Alcohol?", reply_markup=reply_markup)
    return TOS

async def tos(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    answer = query.data
    data['Consumo Alcohol'] = int(answer)
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='2')],
        [InlineKeyboardButton("No", callback_data='1')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Tienes Tos?", reply_markup=reply_markup)
    return DIFICULTAD_RESPIRAR

async def dificultad_respirar(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    answer = query.data
    data['Tos'] = int(answer)
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='2')],
        [InlineKeyboardButton("No", callback_data='1')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Tienes dificultad para respirar?", reply_markup=reply_markup)
    return DIFICULTAD_TRAGAR

async def dificultad_tragar(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    answer = query.data
    data['Dificultad respirar'] = int(answer)
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='2')],
        [InlineKeyboardButton("No", callback_data='1')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Tienes dificultad para tragar?", reply_markup=reply_markup)
    return DOLOR_PECHO

async def dolor_pecho(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    answer = query.data
    data['Dificultad tragar'] = int(answer)
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí", callback_data='2')],
        [InlineKeyboardButton("No", callback_data='1')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="¿Tienes Dolor de Pecho?", reply_markup=reply_markup)
    return CANCER_PULMON

async def cancer_pulmon(update: Update, context: CallbackContext) -> int:
    query = update.callback_query  
    answer = query.data
    data['Dolor en pecho'] = int(answer)
    df = pd.DataFrame([data])
    print(df.head())

    nreg = str(uuid.uuid4())

    columns_to_convert = ['Sexo', 'Edad']
    for column in df.columns:
        if column not in columns_to_convert:
            df[column] = df[column].map({1: False, 2: True}) 

    prediction = model.predict(df)
    cancer_pulmon_prediction = "No" if prediction[0] == 1 else "Si"
    # Store data in Redis
    r.hset(nreg, "sexo", data['Sexo'])
    r.hset(nreg, "edad", data['Edad'])
    r.hset(nreg, "fumador", int(data['Fumador']))  
    r.hset(nreg, "dedos_amarillos", int(data['dedos amarillos']))  
    r.hset(nreg, "ansiedad", int(data['Ansiedad']))  
    r.hset(nreg, "presion_de_grupo", int(data['presion de grupo']))  
    r.hset(nreg, "enfermedad_cronica", int(data['enfermedad cronica']))  
    r.hset(nreg, "fatiga", int(data['fatiga']))  
    r.hset(nreg, "alergia", int(data['Alergia']))  
    r.hset(nreg, "sibilancias", int(data['Sibilancias']))  
    r.hset(nreg, "consumo_alcohol", int(data['Consumo Alcohol']))  
    r.hset(nreg, "tos", int(data['Tos']))  
    r.hset(nreg, "dificultad_respirar", int(data['Dificultad respirar']))  
    r.hset(nreg, "dificultad_tragar", int(data['Dificultad tragar']))  
    r.hset(nreg, "dolor_en_pecho", int(data['Dolor en pecho']))  
    r.hset(nreg, "cancer_pulmon", int(prediction[0]))

    # Send prediction as a reply
    await query.message.reply_text(f"{cancer_pulmon_prediction} eres propenso a tener cancer de pulmon")
    await query.message.reply_text(f"DISCLAIMER: Este es un modelo de machine learning, por lo tanto, esta respuesta no debe ser considerada como una predicción real. Te recomiendo que consultes a un médico para obtener asesoramiento específico y preciso.")

    return ConversationHandler.END



   
async def cancel(update: Update, context: CallbackContext) -> int:
    if update.message:
        await update.message.reply_text('Conversación cancelada.')
    elif update.callback_query:
        await update.callback_query.message.reply_text('Conversación cancelada.')
    else:
        pass
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
            CANCER_PULMON: [CallbackQueryHandler(cancer_pulmon)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    app.add_handler(conv_handler)

    # Iniciar el bot
    print('Arrancando...')
    app.run_polling()