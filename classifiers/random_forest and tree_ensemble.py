'''
Случайный лес/Ансамбль деревьев. Это много бустингов и деревьев решений объединенных вместе. Бустинг — случайная выборка из базовой выборки.
За счет большого числа таких подвыборок (random patching) и построения на каждой своей модели увеличивается качество финальной модели за счет усреднения.
Для оценки качества модели нужно применять oob-оценку.
(Out-of-bag (OOB) также называемая оценкой вне пакета, представляет собой метод измерения ошибки прогнозирования случайных лесов,
расширенных деревьев решений и других моделей машинного обучения, использующих бутстреп-агрегирование (пакетирование).
Бэггинг использует подвыборку с заменой для создания обучающих выборок, на которых модель может учиться.
Ошибка OOB — это средняя ошибка прогнозирования для каждой обучающей выборки xi с использованием только тех деревьев, у которых не было xi в их начальной выборке)
Сильные стороны: нечувствительность к выбросам, малые требования к предобработке данных, к масштабированию, небольшая чувствительность к гиперпараметрам,
разброс модели меньше, а значит она не склонна к переобучению. Так как построение деревьев независимое, то вычисления можно распараллелить.
Слабые стороны — потребляет память и время, чтобы считать и хранить много деревьев. Не применять, когда признаков очень много (больше 100 000),
в этом случае лучше — регрессии.
'''
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

#model fit
X, y = make_classification(n_samples=1000, n_features=4,
                           n_informative=2, n_redundant=0,
                           random_state=0, shuffle=False)

clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(X, y)

#result
print(clf.feature_importances_)
print(clf.predict([[0, 0, 0, 0]]))
