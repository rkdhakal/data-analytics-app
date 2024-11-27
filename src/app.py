from flask import Flask
import analysis

app = Flask(__name__)

@app.route('/')
def index():
    result = analysis.run_analysis()
    response = (
        f"Average Height (Male): {result['avg_height_male']}<br>"
        f"Average Height (Female): {result['avg_height_female']}<br>"
        f"Average Weight (Male): {result['avg_weight_male']}<br>"
        f"Average Weight (Female): {result['avg_weight_female']}"
    )
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
