'''
SciPy - это библиотека алгоритмов Python с открытым исходным кодом и набор математических инструментов. SciPy включает модули для оптимизации,
линейной алгебры, интегрирования, интерполяции, специальных функций, быстрого преобразования Фурье, обработки сигналов и изображений,
решения обыкновенных дифференциальных уравнений и других часто используемых вычислений в науке и технике.
Программное обеспечение с аналогичными функциями включает MATLAB, GNU Octave и Scilab. SciPy в настоящее время выпускается под лицензией BSD.
Его разработка финансируется Enthought.
Ниже приводится распространенный метод вызова функции распределения (в качестве примера возьмем наиболее распространенное нормальное распределение):
Инициализировать функцию распределения (также называемую замороженным распределением);
Метод вызова функции распределения или расчета ее числовых характеристик;
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import stats

norm_dis = stats.norm(5, 3) # Используйте соответствующую функцию распределения и параметры, чтобы создать замороженное нормальное распределение (замороженное распределение)
x = np.linspace(-5, 15, 101)  #  Равномерно возьмите 101 точку в интервале [-5, 15].


#  Вычислить значение функции распределения плотности вероятности распределения в точках в x (PDF)
pdf = norm_dis.pdf(x)

#  Вычислить кумулятивное значение функции распределения (CDF) распределения в точках x
cdf = norm_dis.cdf(x)

#  Ниже показано использование matplotlib для рисования
plt.figure(1)
# plot pdf
plt.subplot(211)  #  Две строки и один столбец, первый подграф
plt.plot(x, pdf, 'b-',  label='pdf')
plt.ylabel('Probability')
plt.title(r'PDF/CDF of normal distribution')
plt.text(-5.0, .12, r'$\mu=5,\ \sigma=3$')  #  3 - стандартное отклонение, а не дисперсия
plt.legend(loc='best', frameon=False)
# plot cdf
plt.subplot(212)
plt.plot(x, cdf, 'r-', label='cdf')
plt.ylabel('Probability')
plt.legend(loc='best', frameon=False)

plt.show()