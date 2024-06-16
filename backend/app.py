from objects.territory.shool import Shool
import json
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from pprint import pprint
app = Flask(__name__)

CORS(app)


@app.route('/', methods=['GET'])
def ping():
    return 'Hello World'


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status": "ok"}), 200


@app.route('/get_object', methods=['POST'])
def get_object():
    data = request.get_json()

    shool = Shool(data)
    shool.total_rebuild()
    # bulding.create_object_main_bulding()
    light_position = {'x': 18, 'y': 18, 'z': 18}
    with open('example_responce.json', 'w') as json_file:
        json.dump(shool.objects, json_file, indent=4)
    return jsonify({"result": shool.objects}), 200


@app.route('/get-rendered-object', methods=['GET'])
def get_rendered_object():
    json_data = request.args.get('json')
    processed_data = {}
    if json_data:
        data = json.loads(json_data)
        for key, value in data.items():
            if isinstance(value, list):
                processed_data[key] = value
                continue
            try:
                # Try converting the value to an integer
                processed_data[key] = int(value)
            except ValueError:
                try:
                    # Try converting the value to a float
                    processed_data[key] = float(value)
                except ValueError:
                    # If conversion fails, keep the original value
                    processed_data[key] = value
    else:
        return 'No JSON data received'

    print(processed_data)
    light_position = {'x': 18, 'y': 18, 'z': 18}
    try:
        shool = Shool(processed_data)
        shool.total_rebuild()
        result = render_template('index.html', objects=shool.objects, light_position=light_position)
    except:
        result = 'Не удалось подобрать оптимальное расположение, попробуйте с другими параметрами'

    # bulding.create_object_main_bulding()

    # with open('example_responce.json', 'w') as json_file:
    #     json.dump(shool.objects, json_file, indent=4)
    return result


@app.route('/render')
def index():
    with open('example_request.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    print(data)
    shool = Shool(data)
    shool.total_rebuild()
    # bulding.create_object_main_bulding()
    light_position = {'x': 18, 'y': 18, 'z': 18}
    with open('example_responce.json', 'w') as json_file:
        json.dump(shool.objects, json_file, indent=4)
    return render_template('index.html', objects=shool.objects, light_position=light_position)

@app.route('/')
def test():
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
    app.run(host='0.0.0.0', port=3000)
