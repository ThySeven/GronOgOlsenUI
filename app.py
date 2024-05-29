from flask import Flask, render_template_string, send_file

app = Flask(__name__)

@app.route('/')
def show_forside():
    return render_index_with_image('/static/forside.png')

@app.route('/auctions')
def show_auctions():
    return render_index_with_image('/static/auctions.png')

@app.route('/auction')
def show_auction():
    return render_index_with_image('/static/auction.png')

@app.route('/bydauction')
def show_bydauction():
    return render_index_with_image('/static/bydauction.png')


# Serve static images
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_file(filename, mimetype='image/png')

def render_index_with_image(image_src):
    with open('index.html') as f:
        html_content = f.read()
        return render_template_string(html_content, image_src=image_src)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)