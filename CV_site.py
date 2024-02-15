from flask import Flask, render_template,redirect
app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/profile", code=302)

@app.route('/profile')
def profile():
    return render_template('CV_Nam.html')

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
