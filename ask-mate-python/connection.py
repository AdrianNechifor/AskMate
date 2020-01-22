
import csv

def read_question():
    with open("sample_data/question.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',', quotechar = '"')
        list_to_return = []
        for row in csv_reader:
            list_to_return.append(row)
        return list_to_return[1:]

def write_question(matrix_of_questions):
    new_matrix_of_questions = []
    new_matrix_of_questions.append([['id','submission_time','view_number','vote_number','title','message','image']])
    for i in matrix_of_questions:
        new_matrix_of_questions.append(i)
    with open('sample_data/question.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in new_matrix_of_questions:
            writer.writerow(i)

def read_answer():
    with open("sample_data/answer.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',', quotechar = '"')
        list_to_return = []
        for row in csv_reader:
            list_to_return.append(row)
        return list_to_return[1:]

def write_answer(matrix_of_answers):
    new_matrix_of_answers = []
    new_matrix_of_answers.append([['id','submission_time','question_id','message','image']])
    for i in matrix_of_answers:
        new_matrix_of_answers.append(i)
    with open('sample_data/answer.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in new_matrix_of_answers:
            writer.writerow(i)