### Создайте класс, который описывает вектор (в трёхмерном пространстве).

У него должны быть:

* a. конструктор с параметрами в виде списка координат x, y, z
* b. метод, вычисляющий длину вектора. Корень можно посчитать с помощью Math.sqrt()
* c. метод, вычисляющий скалярное произведение
* d. метод, вычисляющий векторное произведение с другим вектором
* e. метод, вычисляющий угол между векторами (или косинус угла): косинус угла между векторами равен скалярному
  произведению векторов, деленному на произведение модулей (длин) векторов
* f. методы для суммы и разности
* g. статический метод, который принимает целое число N, и возвращает массив случайных векторов размером N
* h. Если метод возвращает вектор, то он должен возвращать новый объект, а не менять базовый