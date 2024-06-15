from objects.territory.shool import Shool
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/get_object', methods=['POST'])
def get_object():
    data = request.get_json()

    shool = Shool(data)
    shool.total_rebuild()
    # bulding.create_object_main_bulding()
    light_position = {'x': 18, 'y': 18, 'z': 18}
    with open('example_responce.json', 'w') as json_file:
        json.dump(shool.objects, json_file, indent=4)
    return jsonify({"message": "JSON received", "data": shool.objects}), 200



@app.route('/')
def index():

    with open('example_request.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    shool = Shool(data)
    shool.total_rebuild()
    # bulding.create_object_main_bulding()
    light_position = {'x': 18, 'y': 18, 'z': 18}
    with open('example_responce.json', 'w') as json_file:
        json.dump(shool.objects, json_file, indent=4)
    return render_template('index.html', objects=shool.objects, light_position=light_position)


if __name__ == '__main__':
    app.run(debug=True)