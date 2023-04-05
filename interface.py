from flask import Flask,render_template,request,jsonify
import utils
import config
import traceback

app = Flask(__name__)

@app.route('/')
def home():
    #return jsonify({"Result":"This is home page"})
    return render_template('index.html')

@app.route("/predict",methods=['GET','POST'])
def prediction():
    try:
        if request.method == "GET":
            
            data = request.args.get

            print("Data::: ",data)
            age      = int(data('age'))
            bmi      = eval(data('bmi'))
            children = int(data('children'))
            smoker   = data(('smoker'))
            region   = data(('region'))

            model_result = utils.TestModel()

            predict = model_result.result(age,bmi,children,smoker,region)

            #return f"Insurance amount is : {predict}"

            return render_template('index.html',predict = predict)
        else:
            data = request.form.get

            print("Data::: ",data)
            age      = int(data('age'))
            bmi      = eval(data('bmi'))
            children = int(data('children'))
            smoker   = data(('smoker'))
            region   = data(('region'))

            model_result = utils.TestModel()

            predict = model_result.result(age,bmi,children,smoker,region)

            #return f"Insurance amount is : {predict}"

            return render_template('index.html',predict = predict) 
    except:
        print("Error occured!!!")
        print("Error is : ",traceback.print_exc())
        

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=config.PORT,debug=True)