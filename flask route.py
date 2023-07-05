from flask import Flask, request, jsonify
from translator import fr2eng, eng2fr

app = Flask(__name__)

@app.route('/french_to_english', methods=['POST'])
def translate_french_to_english():
    text = request.json['text']
    translated_text = fr2eng(text)
    return jsonify({'translated_text': translated_text})

@app.route('/english_to_french', methods=['POST'])
def translate_english_to_french():
    text = request.json['text']
    translated_text = eng2fr(text)
    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run()
    #it's not runing because i had a problem with the hands on lap on coursera in flask one so i am seeing it youtube and it's too big knowldge 
