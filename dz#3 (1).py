tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
    #'10Б', '9А', '3А', '5Б', '9Е', '7А'
]

def gen_lst(tutor, klass):
    for i in range(len(tutor)):
        tutor2 = tutor[i]
        klass2 = klass[i] if i < len(klass) else None

        yield tutor2, klass2


lst = gen_lst(tutors, klasses)
print(type(lst))
print(next(lst))
print(next(lst))
print(next(lst))
print(next(lst))
print(next(lst))
print(next(lst))
print(next(lst))
