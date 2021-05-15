# ==========================================================
# CREATOR : Mahesa Atmawidya Negara Ekha Salawangi
# DATE CREATED : 20 JUNE 2020
# ABOUT : Simple Chatbot Itenas
# ==========================================================


from flask import Flask,render_template,url_for,redirect
from forms import chatForm
from jalan import jalanBot

kata = []
user = []
bentuk = []
input_data = []
kata_user = "Kamu : "
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
perintah = ["hapus","delete","batal"]

@app.route('/',methods=['GET','POST'])
def index():
    form = chatForm()
    bot = jalanBot()
    if form.validate_on_submit():
        if form.user_input.data.lower() in perintah:
            global kata
            kata = []
            global user
            user = []
            global bentuk
            bentuk = []
            global input_data
            input_data = []
        else:   
            input_data.append(form.user_input.data)
            kata.append(bot.runBot(form.user_input.data))
            final_user = [[kata_user],[form.user_input.data]]
            user.append(final_user)
            bentuk = zip(kata,user)
    return render_template("index.html",kata=kata,form=form,user=user,bentuk=bentuk,data=input_data)

if __name__ == "__main__":
    app.run(debug=True)
