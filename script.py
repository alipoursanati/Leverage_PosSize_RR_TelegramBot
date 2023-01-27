# By: Ali Rajabpour-Sanati
# ali.poursanati@gmail.com

import telegram
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Enter your details for calculating position")
    entry = float(update.message.text)
    stop_loss = float(update.message.text)
    targets = list(map(float, update.message.text.split(",")))
    wallet_size = float(update.message.text)
    risk_percent = int(update.message.text)
    risk = (entry - stop_loss) * (risk_percent/100)
    reward = targets[0] - entry
    if reward/risk < 1.5:
        update.message.reply_text("Error: Risk/reward ratio is less than 1.5")
    else:
        position_size = (wallet_size * (risk_percent/100)) / risk
        leverage = int(position_size / wallet_size * 100)
        update.message.reply_text("Position size: {} \n Leverage: {}".format(position_size, leverage))

def main():
    updater = Updater("TOKEN", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
