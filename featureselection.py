from pprint import pprint
from PyInquirer import prompt, Separator
import numpy as np

import os

from src.datareader import read_data
from src.featuresearch import forward_feature_search, backward_feature_search
from src.datanormalize import normalize

data_path = 'data'
datasets = [dataset for dataset in os.listdir(data_path) if os.path.splitext(dataset)[1] == '.txt']
datasets.sort()

# custom = 1; default = 0
def is_custom_or_defualt_data(answers):
    return answers['dataSource'] == questions[0]['choices'][1]

# forward = 1; backward = 0
def is_forward_or_backward(answers):
    return answers['chosenAlgorithm'] == questions[3]['choices'][0]

questions = [
    {
        'type': 'list',
        'name': 'dataSource',
        'message': 'choose the source of data',
        'choices': [
            'use default datas',
            'enter enter custom data'
        ]
    },
    {
        'type': 'input',
        'name': 'customDataPath',
        'message': '''Enter the relevant path to your data''',
        'when': is_custom_or_defualt_data
    },
    {
        'type': 'list',
        'name': 'chosenData',
        'message': 'choose data',
        'choices': datasets,
        'when': lambda ans: not is_custom_or_defualt_data(ans)
    },
    {
        'type': 'list',
        'name': 'chosenAlgorithm',
        'message': 'choose algorithm you want to run',
        'choices': [
            'Forward Selection',
            'Backward Elimination'
        ]
    }
]

if __name__ == '__main__':
    answers = prompt(questions)
    # pprint(answers)

    if is_custom_or_defualt_data(answers):
        path = answers['customDataPath']
    else:
        path = os.path.join(data_path, answers['chosenData'])

    if is_forward_or_backward(answers):
        feature_search = forward_feature_search
    else:
        feature_search = backward_feature_search

    data = read_data(path)
    (n, m) = data.shape
    print(
        '\nThis dataset has ',
        str(m-1),
        ' features',
        '(not including the class attribute), with ',
        str(n),
        ' instances\n'
    )

    feature_search(data)
