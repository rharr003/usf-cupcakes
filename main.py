from flask import Flask, request, redirect, render_template, jsonify
from models import db, Cupcake, connect_app
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = 'Secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rharr003:Dissidia1!@127.0.0.1:5432/cupcakes'
app.config['SQLALCHEMY_ECHO'] = True
connect_app(app)
Bootstrap(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/cupcakes', methods=['GET', 'POST'])
def get_cupcakes():
    if request.method == 'POST':
        r = request.json
        new_cake = Cupcake(flavor=r.get('flavor'), size=r.get('size'), rating=r.get('rating'), image=r.get('image'))
        db.session.add(new_cake)
        db.session.commit()
        return jsonify(cupcake=new_cake.serialize())
    json = [cake.serialize() for cake in Cupcake.query.all()]
    return jsonify(cakes=json)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['GET', 'PATCH', 'DELETE'])
def get_cupcake(cupcake_id):
    if request.method == 'DELETE':
        cupcake = Cupcake.query.get_or_404(cupcake_id)
        db.session.remove(cupcake)
        db.session.commit()
        return jsonify(message='Delete Successful')
    if request.method == 'PATCH':
        db.session.query(Cupcake).filter_by(id=cupcake_id).update(request.json)
        db.session.commit()
        return jsonify(cupcake=Cupcake.query.get(cupcake_id).serialize())
    json = Cupcake.query.get(cupcake_id).serialize()
    return jsonify(cake=json)


app.run(debug=True)

