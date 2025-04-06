from flask import Flask,render_template,request
import requests


app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    if request.method == 'POST':
        city_name=request.form['name']
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=1bab63e3689b6f06e58553b2bb95a1ab&units=metric"
        
        response = requests.get(url.format(city_name)).json()
        
        temp = response['main']['temp']
        weather = response['weather'][0]['description']
        temp_min = response['main']['temp_min']
        temp_max= response['main']['temp_max']
        return render_template("index.html" ,temp=temp,weather=weather,temp_max=temp_max,temp_min=temp_min)
    else:
        return render_template("index.html")
        
        

@app.route("/about")
def about():
    return render_template("about.html")


    

if __name__ == "__main__":
    app.run(debug=True)