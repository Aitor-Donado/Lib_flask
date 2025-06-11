from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Aquí puedes manejar el envío del formulario
        # Capturar los datos del formulario
        form_data = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'message': request.form.get('message')
        }
        print(form_data)
        return render_template("contact_enviado.html", form_data=form_data)
    else:
        return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)