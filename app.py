from flask import Flask, render_template

from api_client import BigBotherAPIClient

app = Flask(__name__)
api = BigBotherAPIClient()


@app.route('/', methods=['GET'])
def index():
    people = api.list_people()
    return render_template('index.html', people=people)


@app.route('/person/<person_id>', methods=['GET'])
def person(person_id):
    person = api.find_person_by_name(person_id)
    return render_template('person.html', person=person)


if __name__ == '__main__':
    app.run(debug=True)
