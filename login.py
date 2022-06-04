from flask import Flask, render_template, request
from begin_func import search_begin
from russianserch2 import rus_concrete, rus_2
from full_func import search_full_word

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('mainpage.html')


# поиск по русскому слову (Лиза)
@app.route('/rus_tr')
def rus_tr():
    return render_template('russian.html')


@app.route("/rus_results")
def search_rus():
    word = request.args
    if (word['rw'] != " ") & (word['rw'] != ""):
        if (rus_concrete(word['rw']) != None) & (rus_2(word['rw']) != None):
            return render_template('russian.html', res = rus_concrete(word['rw']), res2 = rus_2(word['rw']), concrete = 'Точные совпадения:', r2 = 'Слова, содержащие ваш запрос:')
        elif (rus_concrete(word['rw']) != None) & (rus_2(word['rw']) == None):
                return render_template('russian.html', res = rus_concrete(word['rw']), concrete = 'Точные совпадения:')
        elif (rus_concrete(word['rw']) == None) & (rus_2(word['rw']) != None):
            return render_template('russian.html', res2 = rus_2(word['rw']), r2 = 'Точных совпадений нет. Слова, содержащие ваш запрос:')
        else:
            return render_template('russian.html', tw = 'Вашего слова нет в словаре')
    else: return render_template('russian.html')


# поиск по табасаранскому слову (Настя К)
@app.route('/tab_tr', methods=['GET'])
def tab_tr():
    return render_template('full_word.html')

@app.route("/full_results")
def search_full():
    args = request.args
    if args['nmfull']:
        if search_full_word(args['nmfull']):
            return render_template('full_word.html', answers=search_full_word(args['nmfull']))
        else:
            return render_template('full_word.html', go_back='Вашего слова нет в словаре')
    else:
        return render_template('full_word.html')


# поиск по части  табасаранского слова (Настя Д)
@app.route('/begins', methods=['GET'])
def login():
    return render_template('login.html')


@app.route("/start_results")
def search_start():
    args = request.args
    if args['nm']:
        if search_begin(args['nm']):
            return render_template('login.html', answers=search_begin(args['nm']))
        else:
            return render_template('login.html', go_back='Вашего слова нет в словаре')
    else:
        return render_template('login.html')



@app.route("/full_text")
def text():
    return render_template('begin_results.html', answers=search_begin(''))


@app.route("/author")
def genco():
    return render_template('genco.html')


if __name__ == '__main__':
    app.run(debug=False)
