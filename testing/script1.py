from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return render_tempaltes('home.html')

@app.route('/about/')
def about():
    return "about page"

if __name__ == "__main__":
    app.run()
