import os
import markdown
from flask import Flask
from pathlib import Path


app = Flask(__name__)

@app.route("/")
def readme():
    try:
        with open(os.path.join(Path(os.path.dirname(app.root_path)).parent, "README.md")) as markdown_file:
            content = markdown_file.read()

            return markdown.markdown(content), 200
    except Exception as err:
        return {'message': f'Error occured: {err}',
                'statusCode': 404}, 404
