from distutils.log import debug
from unittest import result
from flask import Flask, jsonify, request, render_template
import Svm_Prediction

app = Flask(__name__)

res = ""

@app.route("/")
def welcome_page():
    return render_template("index.html")

@app.route("/model", methods=['POST'])
def receive_text():
    try:
        global res
#    request_data = request.get_json()
        request_data = request.form["pred_text"]

    # modeli çağırıp predict ettir.
        result = Svm_Prediction.get_predict(request_data)
        print("received {}".format(result))
        return render_template('index.html', res = result[0])
    except Exception as e:
        return "{}".format(e)
app.run(port=5000, debug=True)