from flask import Flask ,request,jsonify

api=Flask(__name__)
#基于flask框架，使用Python编写的服务器应用程序，验证第三方接口能否正常收到天璇推送的数据
#定义一个post接口，用来接收json数据，服务器接受的数据会打印到控制台
@api.route('/receive_data',methods=['post'])
   
def receive_data():
    #从请求中获取json数据
    data=request.get_json()

    print(f"接收的数据:{data}")

    #返回一个确认响应
    return jsonify({"message":"successfully","received_data":data}),200

if __name__=='__main__':
    api.run(debug=True,host='0.0.0.0',port=5000)

#给天璇提供
# http://192.168.101.124:5000/receive_data  

