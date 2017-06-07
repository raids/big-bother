from flask import Flask, render_template
import boto3
from collections import defaultdict
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def lambda_handler(event=None, context=None):
    return render_template('search.html')

# @app.route('/search', methods=['GET', 'POST'])
# def search():
#     if request.method == 'POST' and form.validate_on_submit():
#         return redirect((url_for('search_results', query=form.search.data)))  # or what you want
#     return render_template('search.html', form=form)

# def find_person():
#     # lookup user in index

if __name__ == '__main__':
    app.run(debug=True)
