from flask import Flask, request, json
from flask import jsonify
import main
import HelperLibrary.helperLibrary as helperLib
app = Flask(__name__)

""" Function for checking API is running or not"""
@app.route('/')
def index():
	return "Hello TDM"


""" Function for Masking, Cloning and generating data based on SSN number."""
@app.route('/clone_json', methods=['POST'])
def tdm_api_genrate():
	content_type = request.headers.get('Content-Type')
	if (content_type == 'application/json'):
		data = json.loads(request.data)
		print(data['database'], data['type'], data['rows'])
		databse_name, database_connect, script_type, no_of_rows, columns_array = data['database'], data['database-connect'], data['type'], data['rows'], data['mask-columns']
		helperLib.print_msg("INFO", "API Called successfully")
		json_df = main.tdm_api_genrate(databse_name, database_connect, script_type, no_of_rows, columns_array, outbound_folder_path)
		return jsonify(status="Success", Message=json_df)
	else:
		helperLib.print_msg("ERROR", "")
		return jsonify(status="Failure", Message="")


if __name__ == '__main__':
	app.run(debug=True, host='127.0.0.1', port=8080)
	inbound_folder_path, outbound_folder_path = main.logger()

