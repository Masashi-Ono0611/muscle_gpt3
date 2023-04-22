import os
import openai
from flask import Flask, render_template, request

# OpenAI APIキーを設定
openai.api_key = "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"

# Flaskアプリケーションを初期化
app = Flask(__name__)

# ルートページへのルーティング
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 入力フォームからデータを受け取る
        gender = request.form['gender']
        height = request.form['height']
        weight = request.form['weight']
        training_years = request.form['training_years']
        target_muscle = request.form['target_muscle']
        problem = request.form['problem']

        # OpenAIのGPT-3 APIを使用してアドバイスを生成する
        prompt = "Your question: " + f"{gender}, {height} cm, {weight} kg, {training_years} years of experience, target muscle: {target_muscle}, issue: {problem}. What training routine or advice would you recommend?"
        response = openai.Completion.create(
            engine='text-davinci-002',
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        # 生成されたアドバイスを抽出する
        advice = response.choices[0].text.strip()

        # アドバイスを表示するためにレンダリングする
        return render_template('index.html', advice=advice)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=False)
