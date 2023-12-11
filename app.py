from flask import Flask, render_template, request
import google.generativeai as genai 
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    if request.method == 'POST':
        # Get input from the form
        user_input = request.form['user_input']

    genai.configure(api_key="your api key")

    defaults = {
    'model': 'models/text-bison-001',
    'temperature': 0.7,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
    'max_output_tokens': 1024,
    'stop_sequences': [],
    'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":"BLOCK_LOW_AND_ABOVE"},{"category":"HARM_CATEGORY_TOXICITY","threshold":"BLOCK_LOW_AND_ABOVE"},{"category":"HARM_CATEGORY_VIOLENCE","threshold":"BLOCK_MEDIUM_AND_ABOVE"},{"category":"HARM_CATEGORY_SEXUAL","threshold":"BLOCK_MEDIUM_AND_ABOVE"},{"category":"HARM_CATEGORY_MEDICAL","threshold":"BLOCK_MEDIUM_AND_ABOVE"},{"category":"HARM_CATEGORY_DANGEROUS","threshold":"BLOCK_MEDIUM_AND_ABOVE"}],
    }

    prompt = user_input
    # f""""""

    response = genai.generate_text(
    **defaults,
    prompt=prompt
    )

    return render_template('predict.html', user_input=user_input, response = response.result)


# @app.route('/predict',methods = ["POST"])
# def show_answer():
   

# @app.route('/predict', methods=['POST'])
# def predict():
#     if request.method == 'POST':
#         user_input = request.form['userInput']
#         prediction = predict_from_model(user_input)
#         return render_template('index.html', user_input=user_input, prediction=prediction)
    



# print(response.result)




if __name__ == '__main__':
    app.run(debug=True)
