from flask import Flask ,request,jsonify

app=Flask(__name__)

#定义一个post接口，接收数据
@app.route('/receive_data',methods=['post'])
   
def receive_data():
    #从请求中获取json数据
    data=request.get_json()

    print(f"接收的数据:{data}")

    #返回一个确认响应
    return jsonify({"message":"successfully","received_data":data}),200

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)

#给天璇提供
# http://192.168.101.124:5000/receive_data  

