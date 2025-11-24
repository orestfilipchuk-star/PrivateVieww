from flask import Flask, render_template, request
import requests

app = Flask(__name__)

movies = ["Страна Саша", "Чистый лист (2024)", "«One Hundred Years Ahead»"]

@app.route("/")
def home():
    return render_template("choose_movie.html", movies=movies)

@app.route("/choose_seat", methods=["POST"])
def choose_seat():
    movie = request.form.get("movie")
    return render_template("choose_seat.html", movie=movie)

@app.route("/submit_booking", methods=["POST"])
def submit_booking():
    email = request.form.get("email")
    telegram_tag = request.form.get("telegram")
    seat = request.form.get("seat")
    movie = request.form.get("movie")

    bot_token = "8524671718:AAFbhDCJdy2Sc8hzvuOOCTozMAaKUSwGvvs"
    chat_id = 8015916535

    message = f"Новая бронь:\nФильм: {movie}\nМесто: {seat}\nEmail: {email}\nTelegram: {telegram_tag}"

    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        response = requests.post(url, data={"chat_id": chat_id, "text": message})
        print("Статус Telegram:", response.status_code, response.text)
    except Exception as e:
        print("Ошибка отправки в Telegram:", e)

    return "Бронь принята!"

@app.route("/hours")
def hours():
    return render_template("hours.html")


if __name__ == "__main__":
    app.run(debug=True)
