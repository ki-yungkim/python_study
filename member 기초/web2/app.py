from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html', msg='메인페이지')

if __name__ == '__main__':
    app.run()

    