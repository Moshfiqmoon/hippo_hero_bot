import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

# Replace with your bot token
BOT_TOKEN = "7291863008:AAHkHDf8EIyavGuSGfsaZTBUd_RLB-F6mBQ"
bot = telebot.TeleBot(BOT_TOKEN)

# Handle the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Welcome message
    welcome_text = (
        "Welcome to **Hippo Hero!** 🦛✨\n\n"
        "Get ready to dive into the world of Hippo Hero, where fun meets innovation and every user becomes a hero! "
        "Join the revolution that's not just about tokens, but about building a powerful, supportive, and adventurous community in the crypto space."
    )

    # Inline keyboard buttons
    keyboard = InlineKeyboardMarkup()
    join_button = InlineKeyboardButton("Join Our Community", url="https://t.me/hippoheroofficial")
    launch_button = InlineKeyboardButton("Launch", url="https://brilliant-biscotti-7e3545.netlify.app")
    keyboard.add(join_button)
    keyboard.add(launch_button)

    image_url = "https://i.ibb.co.com/mzDckTr/star.jpg"  # Replace with your actual image URL

    # Send the message with an image and buttons
    bot.send_photo(
        chat_id=message.chat.id,
        photo=image_url,
        caption=welcome_text,
        parse_mode="Markdown",
        reply_markup=keyboard,
    )

# Start the bot
bot.polling()
