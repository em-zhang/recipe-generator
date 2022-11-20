from flask import Flask
from ingredient_selection.ingredient_selection import ing_bp as ing_bp

app = Flask(__name__)
app.register_blueprint(ing_bp)
