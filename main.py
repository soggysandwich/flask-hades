from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/adverts')
def list_adverts():
    advert_list=[
        {'seller': 'seller1', 'product': 'product1', 'price': '100', 'currency': 'usd'},
        {'seller': 'seller2', 'product': 'product2', 'price': '200', 'currency': 'gbp'},
        {'seller': 'seller3', 'product': 'product3', 'price': '2000', 'currency': 'usd'}
    ]
    return render_template('adverts.html', advert_list=advert_list)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
