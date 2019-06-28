from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'GET': 
        pass
if request.method == 'POST':
   name = request.form.get('name')
   post = request.form.get('post')
   creat_post(name, post)

posts = get_posts()

        return render_template('index.html', posts=posts)
