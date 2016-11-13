from flask import Flask,make_response,request,url_for,redirect,jsonify
import json,people
from jsonformat import obj2dict

app = Flask(__name__)


@app.route('/getData')
def hello_world():
    res={"code":1,'data':""};
    username = request.cookies.get('username',None)
    if not username:
        return redirect(url_for('unlogin'))
    else:
        a = {"name": "", "age": 25}
        a["name"] = username;
        a['hobby']=['篮球','乒乓球']
        res['data']=a
        return json.dumps(res)

@app.route('/login')
def login():
    res = {"code": 1, 'data': "登陆成功"};
    resp = make_response(json.dumps(res))
    resp.set_cookie('username', 'zhangsan')
    return resp


@app.route('/logout')
def logout():
    res = {"code": 1, 'data': "退出成功"};
    resp = make_response(json.dumps(res))
    resp.set_cookie('username', "")
    return resp

@app.route("/unlogin")
def unlogin():
    res = {"code": -1, 'data': ""}
    return json.dumps(res)

@app.route("/")
def sample():
    p=people.people('张三',23)
    res={"code": 1, 'data':''}
    pe=people.peopleex()
    pe.p=p
    pe.ex="hellp"
    res['data']=pe
    return json.dumps(res,default=obj2dict)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
