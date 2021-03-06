from flask import Flask, request, render_template, jsonify, Response
import pandas as pd

app = Flask(__name__)

@app.route('/')
def tweet():
    return render_template('index.html')

@app.route('/analyze')
def analyze():

	sample = pd.read_csv('tweets.csv').sample(n = 1)
	tweet = sample['tweet'].iloc[0]
	score = round(sample['risky'].iloc[0], 2)

	if score > 0.5:
		return render_template('risky.html',twitter = tweet,scores = score)
	else:
		return render_template('frisky.html',twitter = tweet, scores = score)

if __name__ == '__main__':
	app.run(host = "0.0.0.0", port = 80)