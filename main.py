from flask import Flask, render_template, request, send_file, redirect, url_for
from onevoice import vocalize
import summarize
import os
from news import get_news

app = Flask(__name__)

session = {}


@app.route('/', methods=["GET", "POST"])
def index():
  if request.method == "POST":
    topic = request.form.get("topic")
    print(topic)
    source = request.form.get("source")
    articles, text = get_news(topic=topic, source=source)
    print(text)
    session['text'] = text 
    session['source'] = source   
    return redirect(url_for('audio'))
  return render_template("index.html")


@app.route('/audio', methods=["GET", "POST"])
def audio():
    text = session.get('text')
    source = session.get('source')
    summary = summarize.summarize(text)
    base64_data = vocalize(summary, str(source))
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'static/base64.txt')
    with open(file_path, 'w') as f:
      f.write(str(base64_data))
 
    return render_template("audio.html", transcript=summary)



if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)



