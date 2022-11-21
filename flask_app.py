
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
from processing import main_get_ingredient_recipes

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        #grams_cake = None
        form_ingredient = request.form["form_ingredient"]
        #try:
        #    grams_cake = float(request.form["grams_cake"])
        #except:
        #    errors += "<p>{!r} is not a number.</p>\n".format(request.form["grams_cake"])

        if form_ingredient is not None:
            #result = cake_flour(grams_cake)
            result = main_get_ingredient_recipes(form_ingredient)
            return '''
                <html>
                    <body>
                        <p>Recipes with {form_ingredient}: {result}</p>
                        <p><a href="/">Click here to find again</a>
                    </body>
                </html>
            '''.format(form_ingredient=form_ingredient, result=result)

    return '''
        <html>
            <body>
                {errors}
                <p>Enter ingredient to find in the cookbook:</p>
                <form method="post" action=".">
                    <p><input name="form_ingredient" /></p>
                    <p><input type="submit" value="find ingredient" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)

