from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

def prediction(x):
    filename = 'model/data/predictor.pkl'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
        pred_value = model.predict([x])
        return pred_value[0]

@app.route('/', methods=['POST', 'GET'])
def index():
    
    pred = 0
    predi = 0
    if request.method == 'POST':
        company = request.form.get('company')
        ram = request.form.get('ram')
        weight = request.form.get('weight')
        typeS = request.form.get('type')
        screen = request.form.get('screen')
        cpu = request.form.get('cpu')
        gpu = request.form.get('gpu')
        os = request.form.get('os')

        feature_list = [int(ram), float(weight)]

        company_list = ['Acer', 'Asus', 'Apple', 'Dell', 'Fujitsu', 'HP', 'Lenovo', 'MSI', 'Other', 'Toshiba']
        type_list = ['2 in 1 Convertible', 'Gaming', 'Netbook', 'Notebook', 'Ultrabook', 'Workstation']
        screen_list = ['Touch Screen', 'IPS panel']
        cpu_list = ['AMD', 'IntelCorei3', 'IntelCorei5', 'IntelCorei7', 'Other']
        gpu_list = ['AMDOther', 'Intel HD Graphics 520', 'Intel HD Graphics 620', 'Intel UHD Graphics 620', 'IntelOther', 'Nvidia GeForce GTX 1050', 'Nvidia GeForce GTX 1060', 'Other']
        os_list = ['Linux', 'MacOS', 'Other', 'Windows']

        def append_features(lst, selected):
            for item in lst:
                feature_list.append(1 if item == selected else 0)

        append_features(company_list, company)
        append_features(type_list, typeS)
        append_features(screen_list, screen)
        append_features(cpu_list, cpu)
        append_features(gpu_list, gpu)
        append_features(os_list, os)

        pred = prediction(feature_list) *330.85
        print(pred)
        print(len(feature_list))

        return render_template('index.html', predi=pred,company=company,ram = ram,weight= weight,typeS = typeS,screen=screen,cpu=cpu,gpu=gpu ,os=os)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
