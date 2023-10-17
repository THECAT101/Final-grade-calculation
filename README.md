# Final-grade-calculation
input_dic = {}
output_dic = {}
result_dic = {}
def my_final_grade_calculation(PATH):
    ####################################### Read_File
    f = open(PATH, "r")
    text = f.readlines()
    input_lst = []
    for line in text:
        line = line.strip()
        input_lst.append(line.split(","))

    ####################################### Quiz
    for i in input_lst:
        temp_quiz = []
        temp_quiz = i[1:7]
        temp_quiz = [int(x) for x in temp_quiz]

        ################################## Remove_Low
        low1 = min(temp_quiz)
        temp_quiz.remove(low1)
        low2 = min(temp_quiz)
        temp_quiz.remove(low2)

        ################################## Quiz_Avrage
        total_quiz = 0
        avg_quiz = 0
        for j in temp_quiz:
            total_quiz += j
        avg_quiz = total_quiz / 4
        output_dic[i[0]] = avg_quiz / 4

    ####################################### HomeWork
    for i in input_lst:
        temp_homework = []
        temp_homework = i[7:11]
        temp_homework = [int(x) for x in temp_homework]

        ################################## Remove_Low
        low1 = min(temp_homework)
        temp_homework.remove(low1)

        ################################## HomeWork_Avrage
        total_homework = 0
        avg_homework = 0
        for j in temp_homework:
            total_homework += j
        avg_homework = total_homework / 3
        output_dic[i[0]] += avg_homework / 4

    ####################################### Midterm
    for i in input_lst:
        temp_midterm = int(i[11])
        output_dic[i[0]] += temp_midterm / 4

    ####################################### Final
    for i in input_lst:
        temp_final = int(i[12])
        output_dic[i[0]] += temp_final / 4

    ####################################### Pass or Fail
    for i in output_dic:
        if output_dic[i] >= 60:
            result_dic[i] = "pass"
        else:
            result_dic[i] = "fail"
    print(output_dic)
    print(result_dic)

####################################### Run
PATH = "C:/Users/Vision LAPTOP/Desktop/file.txt"
my_final_grade_calculation(PATH)
