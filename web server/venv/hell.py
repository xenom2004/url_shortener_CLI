from flask import Flask,render_template,redirect
import pickle
app = Flask(__name__)

@app.route('/')
def hell0_world():
    # c={'www.pythonanywhere.com':'paw'}
   
    # with open('bin_file.bin','rb') as f:   
    #     g=pickle.load(f)
    # g.update(c)
    # with open('bin_file.bin','wb') as f:
    #     pickle.dump(g,f)

    return render_template("index.html")

@app.route('/blog')
def jiji():

    return 'hello there :'
@app.route('/<username>/<int:post_id>')
def jiji2(username=None,post_id=None):
    post_id=post_id+1


    return render_template("index.html",name=username,no=post_id)

s='/s'    
@app.route(s)
def redirection():
    return redirect('https://stackoverflow.com/questions/14343812/redirecting-to-url-in-flask')     


