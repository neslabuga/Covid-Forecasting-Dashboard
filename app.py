from flask import Flask, render_template, jsonify, request
from load_graph import generate_covid_deaths_graph, generate_covid_cases_graph

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/visualization')
def visualization():
    return render_template('visualization.html')

@app.route('/home')
def home_page():
    return render_template('index.html')

@app.route('/load_covid_deaths_analysis', methods=['GET'])
def load_covid_deaths_analysis():
    try:
        graph_json = generate_covid_deaths_graph()
        return jsonify({'graph_json': graph_json})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/load_covid_cases_analysis', methods=['GET'])
def load_covid_cases_analysis():
    try:
        model = request.args.get('model')
        horizon = request.args.get('horizon')
        graph_json, data_summary = generate_covid_cases_graph(model, horizon)
        return jsonify({'graph_json': graph_json, 'data_summary': data_summary})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
