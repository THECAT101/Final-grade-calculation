input_dic = {}
output_dic = {}
result_dic = {}
def my_final_grade_calculation(PATH):
    ####################################### خواندن فایل تکست و تبدیل آن به لیست
    f = open(PATH, "r")
    text = f.readlines()
    input_lst = []
    for line in text:
        line = line.strip()
        input_lst.append(line.split(","))

    ####################################### محاسبه کوییز
    for i in input_lst:
        temp_quiz = []
        temp_quiz = i[1:7]
        temp_quiz = [int(x) for x in temp_quiz]

        ################################## حذف پایین ترین نمرات
        low1 = min(temp_quiz)
        temp_quiz.remove(low1)
        low2 = min(temp_quiz)
        temp_quiz.remove(low2)

        ################################## میانگین کوییز
        total_quiz = 0
        avg_quiz = 0
        for j in temp_quiz:
            total_quiz += j
        avg_quiz = total_quiz / 4
        output_dic[i[0]] = avg_quiz / 4

    ####################################### محاسبه تکالیف
    for i in input_lst:
        temp_homework = []
        temp_homework = i[7:11]
        temp_homework = [int(x) for x in temp_homework]

        ################################## حذف پایین ترین نمرات
        low1 = min(temp_homework)
        temp_homework.remove(low1)

        ################################## میانگین تکالیف
        total_homework = 0
        avg_homework = 0
        for j in temp_homework:
            total_homework += j
        avg_homework = total_homework / 3
        output_dic[i[0]] += avg_homework / 4

    ####################################### محاسبه میانترم
    for i in input_lst:
        temp_midterm = int(i[11])
        output_dic[i[0]] += temp_midterm / 4

    ####################################### محاسبه پایانترم
    for i in input_lst:
        temp_final = int(i[12])
        output_dic[i[0]] += temp_final / 4

    ####################################### تشخیص قبولی
    for i in output_dic:
        if output_dic[i] >= 60:
            result_dic[i] = "pass"
        else:
            result_dic[i] = "fail"
    print(output_dic)
    print(result_dic)

####################################### اجرا
PATH = "C:/Users/Vision LAPTOP/Desktop/file.txt"
my_final_grade_calculation(PATH)