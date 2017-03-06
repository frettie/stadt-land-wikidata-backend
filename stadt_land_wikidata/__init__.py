from flask import Flask

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import stadt_land_wikidata.views


if __name__ == "__main__":
    app.run()