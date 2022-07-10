from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.fzyp1yn.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')



@app.route("/mars", methods=["POST"])
def web_mars_post():
    # index.html_function save_order()에서 자료를 받아서
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']
    price_receive = request.form['price_give']

    # DB에 저장하기기
    doc = {
        'name':name_receive,
        'address':address_receive,
        'size':size_receive,
        'price': price_receive
    }
    db.mars.insert_one(doc)


    # 처리 완료된 사실을 Index.html_function save_order()_success: function (response)에 보내기
    return jsonify({'msg': '주문 완료!'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    # DB에서 주문정보 가져오기
    order_list = list(db.mars.find({}, {'_id': False}))
    # 주문정보를 order에 넣어서 index_html에 연결하기
    return jsonify({'order': order_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)