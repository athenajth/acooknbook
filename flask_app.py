
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
from processing import cake_flour, main_get_ingredient_recipes

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
                        <p>The result of {result}</p>
                        <p><a href="/">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(result=result)

    return '''
        <html>
            <body>
                {errors}
                <p>Enter grams of cake flour to be converted to APF + cornstarch:</p>
                <form method="post" action=".">
                    <p><input name="form_ingredient" /></p>
                    <p><input type="submit" value="Do calculation" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)

