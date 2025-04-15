#https://web.telegram.org/k/#@usthfiredetect_bot
#send_telegram_message(message)
BOT_TOKEN = '8037392842:AAGnCUOyl3x73ROhLLLo1D7pHUvOUT5vXEI'
CHAT_ID = '1020640942'
message= "ABC"


def send_telegram_message(message):
    """Gửi tin nhắn đến Telegram bot"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("Tin nhắn đã được gửi thành công!")
        else:
            print(f"Lỗi khi gửi tin nhắn: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Lỗi kết nối: {e}")
