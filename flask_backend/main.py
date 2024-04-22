from flask import render_template
from shoe_api.config import connex_app, basedir
from shoe_shared.services.ShoeService import read_all
from flask_cors import CORS

app = connex_app
app.add_api("swagger.yml")
CORS(app.app)

@app.route("/")
def home():
    return "go to swagger ui to check api"

if __name__ == "__main__":
    print(basedir)
    app.run(host="0.0.0.0", port=8000, debug=True)