import requests

BOT_TOKEN = '8037392842:AAGnCUOyl3x73ROhLLLo1D7pHUvOUT5vXEI'
CHAT_ID = '-4607134797'
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

def send_telegram_image(image_path):
    """Gửi hình ảnh đến Telegram bot"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    with open(image_path, 'rb') as image_file:
        files = {
            "photo": image_file
        }
        data = {
            "chat_id": CHAT_ID
        }
        try:
            response = requests.post(url, data=data, files=files)
            if response.status_code == 200:
                print("Hình ảnh đã được gửi thành công!")
            else:
                print(f"Lỗi khi gửi hình ảnh: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Lỗi kết nối: {e}")

if __name__ == "__main__":
    # Example usage
    send_telegram_message("Hello from the bot!")
    send_telegram_image("C:/Users/G15/Desktop/FireDetectionSystem-main/output/fire_detected.jpg")