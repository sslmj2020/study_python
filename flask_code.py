from flask import Flask
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    img=Image.open('mama.jpg',"rb")
    return img
    
if __name__ == '__main__':
    app.run()

