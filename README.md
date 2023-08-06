Файлу app.py
Цей скрипт представляє собою веб-додаток на Flask, який здійснює повнотекстовий пошук контактів у базі даних. Він дозволяє швидко знаходити контакти, засновані на введеному тексті.

Як запустити
Для коректної роботи додатку, переконайтесь, що у вас встановлено і з файлу requirements.txt, або запустіть його

Щоб запустити додаток, відкрийте командний рядок або термінал, перейдіть у директорію, де знаходиться скрипт, і введіть:

python app.py
Після запуску додатку, ви можете виконати повнотекстовий пошук контактів.

Використання
Цей додаток має один ендпоінт:

GET /search
Цей ендпоінт здійснює пошук контактів у базі даних згідно з вказаним текстом.

Параметри:

text (необов'язковий): Текст, за яким здійснюється пошук контактів.
Приклад використання:

Якщо додаток запущено на http://localhost:5000/, для пошуку контактів з текстом "John Doe", виконайте GET-запит за наступною адресою:


http://localhost:5000/search?text=John%20Doe
Додаток поверне результат у форматі JSON, який містить знайдені контакти з відповідними полями.

Запит SQL
Для здійснення повнотекстового пошуку, додаток виконує наступний SQL-запит:

SELECT * FROM contacts

WHERE to_tsvector('simple', first_name || ' ' || last_name || ' ' || email) @@ to_tsquery('simple', %s)


Цей запит використовує функції повнотекстового пошуку PostgreSQL (to_tsvector та to_tsquery) для пошуку контактів, що містять вказаний текст у полях first_name, last_name або email.

Файл main.py

Файл що оновлює контакти у БД раз у 24 години.
Для запуску просто заумустіть файл main.py переконайтеся що потрібні фреймворки із файлу requirements.txt. встановлено.
Після запуску оновиться БД і наступного разу вона автоматично буде оновлюватись раз у 24 години, цей параметр можна змінити щоб оновлювалась кожного разу певний час

Файл import_csv.py

Файл який відповідає за імпортданих із файла CSV у БД для імпорта просто запустіть файл

Файл Const.py

Файл містить у собі константи та функції потрібний для чистоти коду.

Файл test.py

Містить у собі тести до файлу app.py там усе закоментовано