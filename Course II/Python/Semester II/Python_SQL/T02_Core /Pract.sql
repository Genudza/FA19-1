/*
1. Напишите запрос для вывода идентификатора (номера) предмета
обучения, его наименования, семестра, в котором он читается, и
количества отводимых на него часов для всех строк таблицы SUBJECT.
*/
SELECT *
FROM SUBJECT;

/*
2. Напишите запрос, позволяющий вывести все строки таблицы
EXAM_MARKS, в которых предмет обучения имеет номер (SUBJ_ID),
равный 12.
*/
SELECT * 
FROM exam_marks 
WHERE subj_id = 12;

/*
3. Напишите запрос, выбирающий все данные из таблицы STUDENT,
расположив столбцы таблицы в следующем порядке: KURS, SURNAME,
NAME, STIPEND.
*/
SELECT kurs, surname, name, stipend 
FROM student;

/*
4. Напишите запрос SELECT, который выполняет вывод наименований
предметов обучения (SUBJ_NAME) и следом за ним количества часов
(HOUR) для каждого предмета обучения (SUBJECT) в 4-м семестре
(SEMESTR).
*/
SELECT subj_name, hour 
FROM SUBJECT 
WHERE semester = 4;

/*
5. Напишите запрос, позволяющий получить из таблицы EXAM_MARKS
значения столбца MARK (экзаменационная оценка) для всех студентов,
исключив из списка повторение одинаковых строк.
*/
SELECT DISTINCT mark FROM exam_marks;

/*
6. Напишите запрос, который выполняет вывод списка фамилий студентов,
обучающихся на третьем и более старших курсах.
*/
SELECT * FROM student 
WHERE kurs >= 3;

/*
7. Напишите запрос, выбирающий данные о фамилии, имени и номерекурса
для студентов, получающих стипендию больше 140.
*/
SELECT surname, name, kurs 
FROM student 
WHERE stipend > 140;

/*
8. Напишите запрос, выполняющий выборку из таблицы SUBJECT названий
всех предметов обучения, на которые отводится более 30 часов.
*/
SELECT * FROM subject 
WHERE hour > 30;

/*
9. Напишите запрос, который выполняет вывод списка университетов,
рейтингкоторых превышает 300 баллов.
*/
SELECT univ_name 
FROM university 
WHERE rating > 300;

/*
10. Напишите запрос к таблице STUDENT для вывода списка фамилий
(SURNAME), имен (NAME) и номера курса (KURS) всех студентов со
стипендией большей или равной 100, и живущих в Воронеже.
*/
SELECT surname, name, kurs 
FROM student 
WHERE city = 'Воронеж' 
AND stipend >=100;

/*
11. Будут выведены все данные студентов, у которых стипендия меньше 100 или студенты, у которых
день рождения НЕ больше или равен дате 10/03/1980 и их ID НЕ больше 1003
*/
SELECT *
FROM STUDENT
WHERE (STIPEND < 100 OR
NOT (BIRTHDAY >= '10/03/1980' AND STUDENT_ID > 1003 ));

/*
12. Будут выведены все данные студентов, у которых день рождения НЕ равен дате 10/03/1980
или стипендия меньше или равно 100 и ID меньше 1003
*/
SELECT *
FROM STUDENT
WHERE NOT(
    (BIRTHDAY ='10/03/1980' OR STIPEND>100)
    AND STUDENT_ID > = 1003
);

-- ### Упражнение 2

/*
1. Напишите запрос, выполняющий вывод находящихся в таблице EXAM_MARKS номеров предметов обучения, 
экзамены по которым сдавались между 10 и 20 января 1999 года .
*/
SELECT * FROM exam_marks 
WHERE exam_date 
BETWEEN '1999-01-10' 
AND '1999-01-20';

/*
2. Напишите запрос, выбирающий данные обо всех предметах обучения,
экзамены по которым сданы студентами,имеющими идентификаторы 12 и 32
*/
SELECT * 
FROM exam_marks 
WHERE student_id in (12, 32);

/*
3.  Напишите запрос, который выполняет вывод названий предметов 
обучения, начинающихся на букву ‘И ’
*/
SELECT subj_name 
FROM subject 
WHERE subj_name LIKE 'И%';

/*
4. Напишите запрос, выбирающий сведения о студентах, у которых имена начинаются на буквы ‘И’или ‘С’.
*/
SELECT * 
FROM student 
WHERE name LIKE 'И%' 
OR name LIKE 'С%';

/*
5. Напишите запрос для выбора из таблицы EXAM_MARKS записей, для которых отсутствуют значения оценок(поле MARK).
*/
SELECT * 
FROM exam_marks 
WHERE mark is NULL;

/*
6.  Напишите запрос, выполняющий вывод из таблицы EXAM_MARKS записей,для которых в поле MARK проставлены значения оценок.
*/
SELECT * 
FROM exam_marks 
WHERE mark is not NULL;