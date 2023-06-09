import pandas as pd

class Answer:
    def __init__(self, author_name: str, author_surname: str, work_num: int, variant: int, exercise: int) -> None:
        self.answer = None
        self.author_name = author_name
        self.author_surname = author_surname 
        self.work_num = work_num
        self.variant = variant
        self.exercise = exercise

    def fill(self, **data) -> None:
        self.answer = pd.DataFrame()
        self.answer['Фамилия, Имя'] = [f"{self.author_surname}, {self.author_name}"]
        self.answer['Номер лабораторной работы'] = [self.work_num]
        self.answer['Вариант лабораторной работы'] = [self.variant]
        self.answer['Номер задания лабораторной работы'] = [self.exercise]

        for key, value in data.items():
            self.answer[key] = value
    
    def save(self) -> None:
        if self.answer is None:
            raise Exception("Fill the fields!")
        self.answer.to_csv(
            f"{self.author_surname}_{self.author_name}_ЛБ{self.work_num}_Задание_{self.exercise}.csv",
            index=False
        )