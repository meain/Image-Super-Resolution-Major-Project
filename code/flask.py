from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def ping():
    return "up"

@app.route('/image_process', methods=['GET', 'POST'])
def parse_request():
    data = request.data
    processed_image_string = process_image(data)
    return processed_image_string
 
if __name__ == "__main__":
    app.run()