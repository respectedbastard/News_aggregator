#Агрегатор новостей с использованием методов машинного обучения
Данный проект содержит набор файлов машинного обучения, тестовых фалов процесса разработки (NLP and some tests) и папку с приложением (News_agreggator)
Для запуска приложения необходимо поместить все файлы из папки News_agreggator в одну папку и запустить файл NewsAgreggator интерпретатором Python
#Краткое описание проекта:
- Данное приложение парсит новостные сайты, автоматически распределяет их на категории с помощью методов машинного обучения и предоставляет пользователю в удобном для ознакомления формате
- Функции, доступные пользователю:
    - Добавление/удаление новостей из списка избранных
    - Переход к источнику новости по ссылке (октрывается браузер)
    - Переключение экранов категорий новостей
    - Переключение темы приложения (Ночная/Дневная)
    - Использование окна "Гайд"
    - Использование окна "Часто задаваемые вопросы"
- Интерфейс приложения выполнен в "Материальном" стиле
#Инструменты реализации проекта:
- В качестве датасета для обучения модели МО был выбран "News dataset from Lenta.Ru": https://www.kaggle.com/datasets/yutkin/corpus-of-russian-news-articles-from-lenta
- Для реализации модели машинного обучения я использовал библиотеку scickit-learn,  в частности конвейер Pipeline, методы TfidfVectorizer и SGDClassifier, так как они показали наилучшие результаты с данным очищенным датасетом
- Для реализации пользовательского интерфейса был использован фреймворк KivyMD
