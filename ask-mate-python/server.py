from flask import Flask, render_template, request, redirect, url_for
import time
import data_manager

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', time=time.time())

@app.route('/question_list/', methods=['GET', 'POST'])
def question_data():
    question_data = data_manager.get_data()
    for i in range(len(question_data)):
        question_data[i] = question_data[i][:-1]
    return render_template('question_list.html', question_data = question_data)

@app.route('/question_list/add/', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        title = request.form['Title']
        message = request.form['Message']
        question_data = data_manager.get_data()
        ID = str(int(question_data[-1][0]) + 1)
        Time = 'nothing'
        new_question = []
        new_question.append(ID)
        new_question.append(Time)
        new_question.append(0)
        new_question.append(0)
        new_question.append(title)
        new_question.append(message)
        new_question.append('')
        question_data.append(new_question)
        data_manager.push_data(question_data)
        return redirect('/question_list/')
    return render_template('add_edit_page.html')


@app.route('/question_list/<question_id>')
def display_question(question_id):
    answer = []
    question_data = data_manager.get_data()
    answer_data = data_manager.get_data_answer()
    for i in question_data:
        if i[0] == question_id:
            question = i
            break
    for i in answer_data:
        if i[3] == question_id:
            answer.append(i)
    return render_template('question_page.html', question= question, answer=answer)

@app.route('/question_list/<question_id>/edit')
def edit_question(question_id, title, message):
    if request.method == 'POST':
        question_data = data_manager.get_data()
        title = request.form['Title']
        message = request.form['Message']
        data_manager.push_data(question_data)
        return redirect(f'/question_list/{question_id}')
    return render_template('add_edit_page.html', question_id=question_id)

@app.route('/question_page/<question_id>/new-answer', methods=['GET', 'POST'])
def route_new_answer(question_id=None):
    saved_answer=[]
    if request.method == 'POST':
        saved_answer.append(request.form['note'])
        data_manager.save_answer(saved_answer,question_id)
        return redirect(f'/question/{question_id}')
    return render_template('new-answer.html', question_id=question_id)


if __name__ == "__main__":
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True,
    )