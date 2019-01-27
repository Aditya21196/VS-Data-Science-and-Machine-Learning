from flask import Flask ,render_template, jsonify
import random
import numpy as np
from sklearn.svm import SVC
import pickle

app = Flask(__name__)

train_inputs = []
train_outputs = []



@app.route('/')
def index():
    return render_template('trainModel.html')


@app.route('/reportBlack/<params>')
def repBlack(params):
    
    # Obtain color
    r,g,b = params.split("-")
    out = 0

    # add to training data
    train_inputs.append([r,g,b])
    train_outputs.append(out)

    # obtain a new color
    new_color = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    # send back new random color
    return jsonify(new_color)

@app.route('/reportWhite/<params>')
def repWhite(params):
    
    # Obtain color
    r,g,b = params.split("-")
    out = 1

    # add to training data
    train_inputs.append([r,g,b])
    train_outputs.append(out)

    # obtain a new color
    new_color = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    # send back new random color
    return jsonify(new_color)

@app.route('/testModel')
def testModel():
    return render_template('testModel.html')

@app.route('/train')
def train():
    # train model
    svm_clf = SVC()
    x_train = np.array(train_inputs)
    y_train = np.array(train_outputs)
    svm_clf.fit(x_train,y_train)

    # save model
    with open("model.pickle","wb") as f:
        pickle.dump(svm_clf,f)

    return jsonify(["Model Trained on " + str(len(y_train)) + " entries."])

@app.route('/predict/<params>')
def predict(params):
    r,g,b = [int(x) for x in params.split("-")]

    # load model
    with open("model.pickle","rb") as f:
        svm_clf = pickle.load(f)
    
    out = svm_clf.predict(np.array([[r,g,b]]))[0]
    out = int(out)

    return jsonify(list([out]))


if __name__ == "__main__":
    app.run(host = "0.0.0.0",port = "5000",debug = True)