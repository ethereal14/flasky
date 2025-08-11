from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

def main():
    print("Hello from flasky!")
    app.run(debug=True)


if __name__ == "__main__":
    main()
