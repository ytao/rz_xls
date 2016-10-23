from flask import Flask,redirect
from flask import render_template
from flask import request
import with_excel as we
import conf as c
import datetime,time
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    mdate=str(time.strftime("%Y-%m-%d", time.localtime()))
    mtime=str(time.strftime("%H:%M", time.localtime()))
    return render_template('index.html',r_date=mdate,r_time=mtime);

@app.route('/record',methods=['GET','POST'])
def record():
    if request.method=='POST':

        for i in c.dic_record.keys():
            try:
                c.dic_record[i]=request.form.get(i)
            except:
                print('在i='+i+'时候出错了')

        # 写入数据
        new_record=we.project_data()
        new_record.testWrite(c.dic_record)
        return render_template('success.html')

if __name__ == '__main__':
    app.debug=True
    # app.debug=True
    app.run(host='0.0.0.0',port=8000)
    # app.run(host='0.0.0.0',port=81)
