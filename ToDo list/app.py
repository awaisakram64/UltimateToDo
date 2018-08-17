from flask import Flask,render_template, jsonify,make_response,redirect
from flask.globals import request
from flask import abort
from flask_pymongo import PyMongo
from bson.json_util import dumps
import pymongo
import datetime as dt




app = Flask(__name__)
app.config['MONGO_DBNAME']='my_todo_list'
app.config['MONGO_URI']="mongodb://awais:awais64@ds121652.mlab.com:21652/my_todo_list"
mongo = PyMongo(app)
c = pymongo.MongoClient()

#Global Var

login = False
loginCred = []

'''
Signup 
'''
@app.route('/todo/signup',methods=['POST'])
def Signup():
    users = mongo.db.users
    if not request.json:
        abort(404)
    content = request.get_json()
    auth = {
        "id":users.count()+1,
        "name":content.get('name'),
        "username": content.get('username'),
        "password": content.get('password')
        }     
    if users.find({"username":auth["username"]})==None:
        users.insert(auth)
        return auth['name']+" is  Successfully Added"
    else:
        return "already exist"
    #all = dumps(users.find({"username":auth["username"]}))
    #return jsonify({"a":all})

'''
@app.route('/todo/api/v1.0/tasks/<int:task_id>')
def get_by_value(task_id):
    task = [task for task in tasks if task['id']==task_id]
    if len(task)==0:
        abort(404)
    return jsonify({'tasks':task})
'''

@app.route('/todo/login',methods=['POST'])
def Login():
    loginCred=[]
    login = False
    users = mongo.db.users
    if not request.json:
        abort(404)
    content = request.get_json()
    auth = {
            "username": content.get('username'),
            "password": content.get('password')
        }
    #all = dumps(users.find({"username":auth["username"],"password":auth["password"]}))
    rec = users.find({"username":auth["username"],"password":auth["password"]})
    if rec==[] or rec=={} or not rec:
        return "username or password not correct"
    else:
        login = True
        loginCred.append([{'id':i['id'],'username':i['username'],'password':i['password'],'name':i['name']} for i in rec])
        return jsonify({'users':loginCred})
    #return users.find({"username":auth["username"],"password":auth["password"]}).get('username')
    #return jsonify({'Users':all}),201    


@app.route('/todo/api/v1.0/tasks',methods=['POST'])
def addtask():
    '''if login == False:
        return "Login to add task"'''
    num = 1 
    todo = mongo.db.todo
    if not request.json:
        abort(404)
    content = request.get_json()
    cou = sum([1 for i in todo.find({'userid':num})])
    send  = {
        "taskid": cou+1,
    "userid": num,
    "title": content.get('title'),
    "note": content.get('note'),
    "setdate": dt.datetime.now(),
    "duedate": content.get('duedate'),
    "done": False
        }
    todo.insert(send),201
    d = []
    d.append([{"taskid":i['taskid'],"userid": num,"title": i['title'],"note":i["note"],"setdate":i["setdate"],"duedate": i['duedate']} for i in todo.find({'userid':num})]) 
    return jsonify(d)
 
@app.route('/todo/api/v1.0/tasks')
def getAllTask():
    num = 1
    todo = mongo.db.todo
    d = []
    d.append([{"taskid":i['taskid'],"userid": num,"title": i['title'],"note":i["note"],"setdate":i["setdate"],"duedate": i['duedate']} for i in todo.find({'userid':num})]) 
    return jsonify(d)

@app.route('/todo/api/v1.0/tasks/<int:tsk>')
def oneTask(tsk):
    num = 1
    todo = mongo.db.todo
    d = []    
    d.append([{"taskid":i['taskid'],"userid": num,"title": i['title'],"note":i["note"],"setdate":i["setdate"],"duedate": i['duedate']} for i in todo.find({'userid':num})if i['taskid']==tsk]) 
    return jsonify(d)

@app.route('/todo/api/v1.0/tasks/<int:tsk>',methods=['PUT']) 
def upadteTask(tsk):
    num = 1 
    todo = mongo.db.todo
    if not request.json:
        abort(404)
    content = request.get_json()
    todo.update({'userid':num,'taskid':tsk},{'$set':content})
    return "Successfully Updated"

@app.route('/todo/api/v1.0/tasks/<int:tsk>',methods=['DELETE']) 
def delete(tsk):
    num = 1
    todo = mongo.db.todo
    if not request.json:
        abort(404)
    content = request.get_json()
    todo.delete_one({'userid':num,'taskid':tsk})
    return "Successfully Deleted"

    
app.run(debug=True)