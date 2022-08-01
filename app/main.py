from flask import Flask, render_template, jsonify
import json
import os
app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))
@app.route("/books")
def api():
    with open('../data.json', 'r') as file:
        data = json.load(file)
        return jsonify(data)

@app.route('/add',methods=['get','post'])
def addBook():
    checker = False
    try:
        bookName = request.form['book']
        urlLink = request.form['url']
        ideas = request.form['idea']
        print(bookName)
    except KeyError:
        print("Can't find value")
    else:
        with open('../data.json', 'r') as file:
            data = json.load(file)
            updateFile = data
            with open('../data.json', 'w') as file2:
                updateFile[bookName] ={"url": urlLink,"description":ideas,"Idea":[]}
                data= updateFile
                json.dump(data, file2, indent=4)
                checker=True

    return render_template('addBook.html',isSuccess=checker)

@app.route("/")
def main():
    with open('../data.json', 'r') as file:
        data = json.load(file)
        key =list(data.keys())
        length = len(data.keys())
        print(length)
        print(key)
    return render_template("home.html", datas=data, keys=key,longArray=length)

@app.route("/book/<name>")
def home(name):
    with open('../data.json', 'r') as file:
        data = json.load(file)
        return render_template("index.html",datas=data[name]['Idea'],line=name,image=data[name]['url'])



@app.route('/handle/<de>',methods=['get','post'])
def handleInput(de):
    input = request.form['idea']
    with open('../data.json', 'r') as file:
        data = json.load(file)
        updateFile = data[de]['Idea']
        with open('../data.json', 'w') as file2:
            updateFile.append(input)
            data[de]['Idea'] = updateFile
            json.dump(data, file2, indent=4)



    return home(de)



@app.route("/data")
def uploadData():
    with open('../data.json', 'r') as file:
        data = json.load(file)
        return jsonify(data)
