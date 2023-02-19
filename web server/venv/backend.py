from flask import Flask,render_template,redirect,request


# import pickle
app = Flask(__name__)




@app.route('/dd')
def download_file():
    import json
    with open('/home/ab21/mysite/p.json', 'r') as f:
        data = json.load(f)
    return data


@app.route('/ll',methods=['POST'])

def update_json():
    import json
    data=request.get_json(force=True)
    with open('/home/ab21/mysite/p.json','r') as file:
        before=json.load(file)
    before.update(data)


    with open('/home/ab21/mysite/p.json','w') as f:
        json.dump(before,f)

    return "success"

@app.route('/<username>')
def redirection(username=None):
    import json
    with open('/home/ab21/mysite/p.json', 'r') as forest:
        data=json.load(forest)

    y='ab21.pythonanywhere.com/' + username
    for x in data:
        if(data[x]==y):
            ve=x
    return redirect(ve)



@app.route('/')
def hell0_world():


    return render_template("index.html")


# @app.route('/<username>')
# def jiji2(username=None):



#     return redirect("https://www.youtube.com/")



if(__name__=="__main__"):
    app.run()
