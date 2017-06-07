from flask import Flask, render_template

from api_client import BigBotherAPIClient

app = Flask(__name__)
api = BigBotherAPIClient()


@app.route('/', methods=['GET', 'POST'])
def index():
    people = api.list_people()
    return render_template('index.html', people=people)


if __name__ == '__main__':
    app.run(debug=True)
