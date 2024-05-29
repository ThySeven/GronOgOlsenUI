from flask import Flask, send_file, render_template_string

app = Flask(__name__)

# Updated route to serve the HTML page
@app.route('/')
def index():
    return render_template_string(open('index.html').read())

# Route to serve the image
@app.route('/image')
def show_image():
    return send_file('go.png', mimetype='image/png')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)