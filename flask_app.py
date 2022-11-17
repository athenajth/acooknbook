
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
from processing import cake_flour

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        grams_cake = None
        try:
            grams_cake = float(request.form["grams_cake"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["grams_cake"])

        if grams_cake is not None:
            result = cake_flour(grams_cake)
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
                    <p><input name="grams_cake" /></p>
                    <p><input type="submit" value="Do calculation" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)

