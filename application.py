from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin

from Summarizer.pipeline.train import TrainingPipeline
from Summarizer.pipeline.prediction_pipeline import SinglePrediction

app = Flask(__name__)
CORS(app)

#localhost:5000
@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

#localhost:prot_number/train
@app.route("/train", methods=['POST'])
@cross_origin()
def train():
    train_pipeline = TrainingPipeline()
    train_pipeline.run_pipeline()
    return render_template('index.html')

#localhost:port_numbner/predict
@app.route('/predict', methods=['GET','POST'])
@cross_origin()
def getsummary():
    if request.method == 'GET':
        return render_template('summary.html')
    else:
        
        input_text = request.form['data']
        single_prediction = SinglePrediction()
        result = single_prediction.predict(input_text)
        return render_template('summary.html',result=result)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)#localhost:8080