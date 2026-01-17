from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('bitcoinprice.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_text = ""

    if request.method == 'POST':
        
        a = float(request.form['open_close'])
        b = float(request.form['low_high'])
        c = int(request.form['quarter_end'])
        d = float(request.form['price_change'])

        cus_input = np.array([[a, b, c, d]])
        result = model.predict(cus_input)
        prediction = int(round(result[0]))

        if prediction == 1:
            prediction_text = "📈 Bitcoin price will go UP"
        else:
            prediction_text = "📉 Bitcoin price will go DOWN"

    return render_template('index.html', prediction=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
