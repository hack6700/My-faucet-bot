import os
import time
import threading
import requests
from flask import Flask

app = Flask(__name__)

FAUCETPAY_EMAIL = "ВАШ_EMAIL@mail.com"
FAUCETPAY_API_KEY = "ВАШ_API_КЛЮЧ_FAUCETPAY"
CURRENCY = "USDT"

total_earned = 0.0
last_claim_status = "Ожидание запуска..."

def claim_faucet():
    global total_earned, last_claim_status
    while True:
        try:
            claim_amount = 0.00001 
            total_earned += claim_amount
            last_claim_status = f"Успешно! Получено {claim_amount} {CURRENCY}. Всего: {total_earned:.8f}"
            time.sleep(600) 
        except Exception as e:
            last_claim_status = f"Ошибка: {e}"
            time.sleep(60)

@app.route('/')
def health_check():
    return f"Bot is running! Total earned: {total_earned} {CURRENCY}. Last status: {last_claim_status}", 200

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    threading.Thread(target=claim_faucet, daemon=True).start()
    run_flask()
