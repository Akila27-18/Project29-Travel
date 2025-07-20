from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)
destinations = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_destination():
    if request.method == 'POST':
        new_dest = {
            'id': str(uuid.uuid4()),
            'name': request.form['name'],
            'region': request.form['region'],
            'description': request.form['description'],
            'image': request.form['image']
        }
        destinations.append(new_dest)
        return redirect(url_for('list_destinations'))
    return render_template('add.html')

@app.route('/destinations')
def list_destinations():
    region = request.args.get('region')
    if region:
        filtered = [d for d in destinations if d['region'].lower() == region.lower()]
    else:
        filtered = destinations
    return render_template('list.html', destinations=filtered)

@app.route('/destination/<id>')
def destination_detail(id):
    dest = next((d for d in destinations if d['id'] == id), None)
    return render_template('detail.html', dest=dest)

if __name__ == '__main__':
    app.run(debug=True)
