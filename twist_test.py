import random
import matplotlib.pyplot as plt

# hist = input("Describe your level of experience with Python (beginner, intermediate, advanced, expert): ")
# hist = 'expert'
grade_list = []
grade_dict = {}
count = 0

def quiz_range(hist):
    """Determine the advantage a student has for the success in the course
    :param hist: A students prior history with coding
    :return first_score: The lower bounded score for assignments based on a student's history
    """
    if hist == 'beginner':
        first_score = 0
    if hist == 'intermediate':
        first_score = 30
    if hist == 'advanced':
        first_score = 60
    if hist == 'expert':
        first_score = 80
    return first_score


def quizzes(num_quiz, first_score):
    """Predict the grade for the students total quiz scores throughout the course
    :param num_quiz: Total number of quizzes in the course
    :param first_score: Given the history of the student, the first_score predicts a lower bound for quiz grades
    """
    num_quiz_range = num_quiz + 1
    quiz_list = []
    for quizzes in range(1, num_quiz_range):
        reading_adv = random.uniform(0, .2)
        quiz_raw = random.uniform(first_score, 100)
        quiz_1 = (quiz_raw * reading_adv) + quiz_raw
        if quiz_1 >= 100:
            quiz_grade = 100
        elif quiz_1 < 100:
            quiz_2 = random.uniform(quiz_1, 100)
            quiz_grade = (quiz_1 + quiz_2) / 2
        quiz_list.append(quiz_grade)
    final_quiz_grade = (sum(quiz_list)/num_quiz)/100
    return final_quiz_grade


def assignment_range(hist):
    """Determine the advantage a student has for the success in the course
        :param hist: A students prior history with coding
        :return lower_score: The lower bounded score for assignments based on a student's history
        """
    if hist == 'beginner':
        lower_score = 40
    if hist == 'intermediate':
        lower_score = 60
    if hist == 'advanced':
        lower_score = 75
    if hist == 'expert':
        lower_score = 85
    return lower_score


def participation(num_classes):
    """Predict the grade for the students total participation in class
    :param num_classes: Total number of classes to participate in
    """
    part_total = 0
    total_classes = num_classes + 1
    for c in range(0, total_classes):
        part = random.uniform(0, 10)
        part_total += part
    part_total = part_total/(num_classes * 10)
    return part_total


# Create a function that randomly determines the outcome of group assignments
def group_assign(hist, num_g_assign, lower_score):
    """Predict the grade for the student's grades on the group assignments
    :param hist: A students prior history with coding
    :param num_g_assign: Total number of group assignments
    :param lower_score: Given the history of the student, the lower_score predicts a lower bound for quiz grades
    """

    # They should have an advantage based on their prior experience and the other students will be completely random


# Create a function that randomly determines the outcome of indiviudal assignments
def ind_assign(num_i_assign, lower_score):
    """Predict the grade for the student's individual assignments
    :param num_i_assign: Total number of individual assignments
    :param lower_score: Given the history of the student, the lower_score predicts a lower bound for quiz grades
    """
    # They should have an advantage if they have had prior experience
    num_assign = num_i_assign + 1
    ind_score = 0
    for hw in range(1, num_assign):
        hw_raw = random.uniform(lower_score, 100)
        ind_score = ind_score + hw_raw
    final_ind_grade = (ind_score / num_i_assign) / 100
    return final_ind_grade

# Create a function that randomly determines the final project grade
def final_proj():
    """Predict the grade for the student's final project

    """
    # This could be completely random since we are working on it now?

# Create a function that adds all the grades up into one for a final probability
def grade(hist, part_points, quiz_points, ind_points): # add parameters for the group/ind assignments and final
    """Use all of the following information and the weight of each grade to determine the final grade
        for the student in this course. Will they pass the course?
    :param hist: A students prior history with coding
    :param part_points: The total participation points calculated
    :param quiz_points: The total quiz points calculated
    """
    final_participation = part_points * .10
    final_quizzes = quiz_points * .15
    final_ind_assign = ind_points * .2763  # (10.53% per assignment (3) and 5.25% for the first ind assignment) * 75
    # final_group_points = group_points * .3159  # (10.53% per assignment (4) * 75
    # final_assign = final_points * .1578  # (10.53% * 2 for the 2/1 weight per assignment) * 75

    total_points = final_participation + final_quizzes + final_ind_assign # + final_assign
    total_points = round(total_points * 100, 2)

    # if 100 <= total_points >= 93:
    #     print("As a/an {}, your final grade is an A, and you have passed the course.".format(hist))
    # elif 92.9 <= total_points >= 90:
    #     print("As a/an {}, your final grade is an A-, and you have passed the course.".format(hist))
    # elif 89.9 <= total_points >=87:
    #     print("As a/an {}, your final grade is a B+, and you have passed the course.".format(hist))
    # elif 86.9 <= total_points >= 83:
    #     print("As a/an {}, your final grade is a B, and you have passed the course.".format(hist))
    # elif 82.9 <= total_points >= 80:
    #     print("As a/an {}, your final grade is a B-, and you have passed the course.".format(hist))
    # elif 79.9 <= total_points >= 77:
    #     print("As a/an {}, your final grade is a C+, and you have passed the course.".format(hist))
    # elif 76.9 <= total_points >= 73:
    #     print("As a/an {}, your final grade is a C, and you have passed the course.".format(hist))
    # elif 72.9 <= total_points >= 70:
    #     print("As a/an {}, your final grade is a C-, and you have passed the course.".format(hist))
    # elif 69.9 <= total_points >= 65:
    #     print("As a/an {}, your final grade is a D, and you have NOT passed the course.".format(hist))
    # elif total_points <= 65:
    #     print("As a/an {}, your final grade is an F, and you have NOT passed the course.".format(hist))
    return total_points


def run_program(hist, count):
    """Use this function to run all of the previous functions in the program.
    :param hist: A students prior history with coding
    :return stats: Statistics on each run that we are producing.
        # What is the student's final grade based on their history, do they pass the course?
    """
    first_score = int(quiz_range(hist))
    total_quiz = quizzes(8, first_score)
    total_part = participation(16)

    assign_range = assignment_range(hist)
    ind_points = ind_assign(4, assign_range)

    grade_percent = float(grade(hist, total_part, total_quiz, ind_points))

    grade_list.append(grade_percent)


def analyze_students(num_exp, num_adv, num_int, num_beg):
    """Run the program as many times as needed to get the desired results.
    :param num_exp: Total number of expert students
    :param num_adv: Total number of advanced students
    :param num_int: Total number of intermediate students
    :param num_beg: Total number of beginner students
    """
    for tests in range(num_exp):
        run_program('expert', count)
    for tests in range(num_adv):
        run_program('advanced', count)
    for tests in range(num_int):
        run_program('intermediate', count)
    for tests in range(num_beg):
        run_program('beginner', count)


def graph(grade_dict):
    """Create a graph based on the number of times we analyze the students and their total grades.
    :param grade_dict: A dictionary filled with the grades and number of times the program is run.
    """
    keys = range(100)
    for i in keys:
        grade_dict[i] = grade_list[i]



    lists = sorted(grade_dict.items())
    x, y = zip(*lists)

    plt.plot(x, y)
    plt.show()


analyze_students(100, 0, 0, 0)
graph(grade_dict)

