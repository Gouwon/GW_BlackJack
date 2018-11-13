## 카드의 구성 카드 52장을 객체, 인스턴스로 만들어내는 곳. 외부에서 변수로 접근하게, @competed variable
### self.name = 
### self.value = 1 ~ 10

def card():
    patterns = ["Spade", "Heart", "Clover", "Diamond"]
    numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]    
    card = []
    print(patterns[0], patterns[1])
    for i in patterns:
        card = card.append(patterns[i])
        print("card in for-loop : ", card)
        return card

# class Card():
#     def __init__(self):    
        
        #     for v in numbers:
        #         self.card = patterns[i] + numbers[v]
        # print(self.card)    
        # print("self.card = ", list(self.card))
    

        

print("card", card())
# cards = []
# cards.append(Card())
# print("cards = ", cards)



"""  
## 강사님, student1.py 참고하여 카드 객체 만들어서 호출하기.
from functools import reduce

g_grades = ['A', 'B', 'C', 'D', 'F']
g_grades.reverse()

class Student:
    grade = ''
    def __init__(self, line):
        name, gender, age, score = line.strip().split(',')
        self.name = name
        self.gender = gender
        self.age = age
        self.score = int(score)

    def __str__(self):
        return "{}**\t{}\t{}\t{}".format(self.name[0], self.gender, self.age, self.grade)

    def make_grade(self):
        if self.score == 100:
            self.grade = 'A+'
        elif self.score < 50:
            self.grade = 'F'
        else:
            self.grade = g_grades[ self.score // 10 - 5 ]

students = []
with open('students.csv', 'r', encoding='utf8') as file:
    for i, line in enumerate(file):
        if i == 0: continue
        students.append( Student(line) )

students.sort(key = lambda stu: stu.score, reverse = True)
m = map(lambda stu: stu.make_grade(), students)
list(m)

def sumfn(x, y):
    if type(x) == int:
        return x + y.score
    else:
        return x.score + y.score

# total = reduce(lambda x, y: (x if type(x) == int else x.score) + y.score, students)
total = reduce(sumfn, students)
avg = total / len(students)
print("총계, 평균>>>", total, avg)

print("이름\t성별\t나이\t학점")
print("----\t----\t----\t----")
for s in students:
    print(s)

print("-----------------------------")
for s in students:
    if s.score >= avg:
        print(s.name, s.score)

=========

cards = []
cards.appen(Card())


        
"""