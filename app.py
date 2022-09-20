from flask import Flask, request, render_template, url_for, redirect
import qrcode

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route('/QR_Code_Generater')
def home():
    return render_template('index.html')


@app.route('/converted', methods=['POST'])
def convert():
    text = request.form['test']
    show(text)
    return render_template('converted.html')


# @app.route('/show')
# def show():
#     qr.add_data(text)
#     qr.make(fit=True)
#
#     img = qr.make_image(fill_color="black", back_color="white")
#     url = ".\static\images\image.png"
#     img.save(url)
#     return url

def show(text):
    img = qrcode.make(text)
    url = f".\static\imagvgvvn bves\image.png"
    img.save(url)


if __name__ == "__main__":
    app.run(debug=True)
