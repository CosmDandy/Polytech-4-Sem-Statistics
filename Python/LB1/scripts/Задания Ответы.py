import pandas as pd
import numpy as np


def lab1_task1(path_to_json):
    lb_num = 1
    lb_exercise_num = 1
    all_answers, answer = pd.DataFrame(), pd.DataFrame()
    task = pd.read_json(path_to_json)
    for i, data in enumerate(task['Данные']):
        data = pd.Series(data)

        data_sort = data.sort_values()

        unique = sorted(data.unique())

        freq = pd.Series(data_sort).value_counts().sort_index()
        freq = pd.DataFrame(freq, index=unique, columns=["Частота"]).T

        rel_freq = pd.Series(data_sort).value_counts().sort_index() / len(data_sort)
        rel_freq = pd.DataFrame(rel_freq, index=unique, columns=["Относительная частота"]).T

        emp_func = rel_freq.iloc[0].cumsum()
        emp_func.name = "F*"
        emp_func = pd.DataFrame(emp_func, index=unique).T

        answer['Номер лабораторной работы'] = [lb_num]
        answer['Вариант лабораторной работы'] = [i + 1]
        answer['Номер задания лабораторной работы'] = [lb_exercise_num]

        answer['Вариационный ряд'] = [str(data_sort.tolist())]
        answer['Варианты'] = [str(unique)]
        answer['Частота'] = [str(freq.values.tolist()[0])]
        answer['Относительная частота'] = [str(rel_freq.values.tolist()[0])]
        answer['Эмпирическая функция распределения'] = [str(emp_func.values.tolist()[0])]
        all_answers = pd.concat([all_answers, answer], ignore_index=True)
    return all_answers


def lab1_task2(path_to_json):
    lb_num = 1
    lb_exercise_num = 2
    all_answers, answer = pd.DataFrame(), pd.DataFrame()
    task = pd.read_json(path_to_json)
    for i, data in enumerate(task['Данные']):
        data = pd.Series(data)

        data_sort = data.sort_values()

        unique = sorted(data.unique())

        freq = pd.Series(data_sort).value_counts().sort_index()
        freq = pd.DataFrame(freq, index=unique, columns=["Частота"]).T

        rel_freq = pd.Series(data_sort).value_counts().sort_index() / len(data_sort)
        rel_freq = pd.DataFrame(rel_freq, index=unique, columns=["Относительная частота"]).T

        emp_func = rel_freq.iloc[0].cumsum()
        emp_func.name = "F*"
        emp_func = pd.DataFrame(emp_func, index=unique).T

        mean = np.mean(data)

        var = np.var(data, ddof=1)

        std = np.std(data, ddof=1)

        cv = (std / mean) * 100

        answer['Номер лабораторной работы'] = [lb_num]
        answer['Вариант лабораторной работы'] = [i + 1]
        answer['Номер задания лабораторной работы'] = [lb_exercise_num]

        answer['Вариационный ряд'] = [str(data_sort.tolist())]
        answer['Варианты'] = [str(unique)]
        answer['Частота'] = [str(freq.values.tolist()[0])]
        answer['Относительная частота'] = [str(rel_freq.values.tolist()[0])]
        answer['Эмпирическая функция распределения'] = [str(emp_func.values.tolist()[0])]

        answer['Выборочное среднее'] = [mean]
        answer['Выборочная дисперсия'] = [var]
        answer['Среднеквадратическое отклонение'] = [std]
        answer['Коэффицент вариации'] = [cv]

        all_answers = pd.concat([all_answers, answer], ignore_index=True)
    return all_answers


def lab1_task3(path_to_json):
    lb_num = 1
    lb_exercise_num = 3
    all_answers, answer = pd.DataFrame(), pd.DataFrame()
    task = pd.read_json(path_to_json)
    for i, data in enumerate(task['Данные']):
        data = pd.Series(data)

        data_sort = data.sort_values()

        unique = sorted(data.unique())

        k = int(np.ceil(np.log2(len(data_sort)) + 1))

        delta = (data_sort.max() - data_sort.min()) / k

        intervals = pd.Series([data_sort.min() + i * delta for i in range(k + 1)])

        # intervals_mean = [(i.left + i.right)/2 for i in pd.Series(data_sort).value_counts(bins=8).sort_index().index]
        intervals_mean = [f'{intervals[i]:.2f}-{intervals[i + 1]:.2f}' for i in range(intervals.count() - 1)]

        freq_intervals = pd.Series(data_sort).value_counts(bins=8).sort_index().values
        freq_intervals = pd.DataFrame(freq_intervals, index=intervals_mean, columns=["Частота"]).T

        rel_intervals_freq = pd.Series(data_sort).value_counts(bins=8).sort_index().values / len(data_sort)
        rel_intervals_freq = pd.DataFrame(rel_intervals_freq,
                                          index=[f'{intervals[i]:.2f}-{intervals[i + 1]:.2f}' for i in
                                                 range(intervals.count() - 1)],
                                          columns=["Относительная частота"]).T

        emp_func = rel_intervals_freq.iloc[0].cumsum()
        emp_func.name = "F*"
        emp_func = pd.DataFrame(emp_func,
                                index=[f'{intervals[i]:.2f}-{intervals[i + 1]:.2f}' for i in
                                       range(intervals.count() - 1)]).T

        mean = np.mean(data)

        var = np.var(data, ddof=1)

        std = np.std(data, ddof=1)

        cv = (std / mean) * 100

        answer['Номер лабораторной работы'] = [lb_num]
        answer['Вариант лабораторной работы'] = [i + 1]
        answer['Номер задания лабораторной работы'] = [lb_exercise_num]

        answer['Вариационный ряд'] = [str(data_sort.tolist())]
        answer['Варианты'] = [str(unique)]
        answer['Количество интервалов'] = [k]
        answer['Шаг интервала'] = [delta]
        answer['Интервальный вариационный ряд'] = [str(intervals.tolist())]
        answer['Среднее по интервалу'] = [str(intervals_mean)]
        answer['Частота интервального вариационного ряда'] = [str(freq_intervals.values.tolist()[0])]
        answer['Относительная частота интервального вариационного ряда'] = [str(rel_intervals_freq.values.tolist()[0])]
        answer['Эмпирическая функция распределения'] = [str(emp_func.values.tolist()[0])]

        answer['Выборочное среднее'] = [mean]
        answer['Выборочная дисперсия'] = [var]
        answer['Среднеквадратическое отклонение'] = [std]
        answer['Коэффицент вариации'] = [cv]

        all_answers = pd.concat([all_answers, answer], ignore_index=True)
    return all_answers


lab1_task1('../input/Данные к заданию №1.json').to_csv('../reference_output/Задание 1 Ответы.csv', index=False)
lab1_task2('../input/Данные к заданию №2.json').to_csv('../reference_output/Задание 2 Ответы.csv', index=False)
lab1_task3('../input/Данные к заданию №3.json').to_csv('../reference_output/Задание 3 Ответы.csv', index=False)
