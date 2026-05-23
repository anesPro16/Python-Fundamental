# Exam Apps

def get_valid_option(pesan_input):
	while True:
		option_list = ["A", "B", "C", "D"]
		option = input(pesan_input).upper()
		if option in option_list:
			return option
		else:
			print("option is not valid!!")

def get_question():

	ori_question = []
	with open("question_data.txt", "r") as file:
		for line in file:
			ori_question.append(line.strip())
	return ori_question

def create_question():
	ori_question = get_question()

	import random
	random.shuffle(ori_question)

	exam_question = []

	for i in range(10):
		question = ori_question[i]
		data = question.split("|")

		question = data[0]
		option_answer = data[1]

		answer = option_answer.split(",")
		correct_answer = answer[0]

		random.shuffle(answer)

		exam_question.append({
			"question": question,
			"answer": answer,
			"correct_answer": correct_answer,
		})

	return exam_question

def app_main():
	exam_question = create_question()
	option = ["A", "B", "C", "D"]

	correct_answer = 0
	wrong_answer = 0

	for i in range(len(exam_question)):
		question = exam_question[i]
		print(f"Question {i+1}. {question['question']} ")
		print("Answer: ")

		for j in range(len(question["answer"])):
			answer = question["answer"][j]
			print(option[j], ".", answer)

		input_user = get_valid_option("Choose answer (A,B,C,D) : ")
		input_user_index = option.index(input_user)
		ori_input_user = question["answer"][input_user_index]

		if ori_input_user == question["correct_answer"]:
			print("Correct Answer")
			correct_answer += 1
		else:
			print("Wrong Answer")
			wrong_answer += 1

	print("Result Exam")
	print(f"Correct Answer = {correct_answer}")
	print(f"Wrong Answer = {wrong_answer}")
	print(f"Result Exam = {correct_answer / (correct_answer + wrong_answer) * 100} %")

app_main()
