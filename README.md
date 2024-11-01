
Реалізувати worker для отримання та зберігання відкритих даних моніторингу центрів надання адміністративних послуг

  Технологічний стек : python , postgresql, docker


Завдання:
    1. Визначити актуальний річний квартал та отримувати  за попередній період 

Запит на отримання звітів ОДА:

GET https://guide.diia.gov.ua/api/v1/static_reports/list/<year>/<quarter>/?format=json

	де: 
	year - рік 
	quarter - річний квартал 

Запит на отримання списку ЦНАП області:

GET https://guide.diia.gov.ua/api/v1/static_reports/entries/<report_id>?format=json

де: 
	report_id - ідентифікатор звіту ОДА


Запит на отримання даних ЦНАП:

GET https://guide.diia.gov.ua/api/v1/static_reports/detail/<report_entries_id>

де: 
	report_entries_id - ідентифікатор даних звіту  про ЦНАП

	
    2. Спроектувати базу даних та зберігати дані отримані з API. 
Дані по ЦНАП мають оновлюватись по унікальному параметру IDF, щоквартально. 


    3. Реалізувати benchmark та записувати в лог файл:
(*обов'язково) час роботи worker - час запуску - час завершення - підсумковий час за який відпрацював
(*не обов'язково буде перевагою) - споживання системних ресурсів (оперативної пам'яті та процесора).

    4. Вкласти компоненти програми в docker та написати інструкцію по розгортанню.

    5. Закомітити код в GitHub, додати інструкцію і надіслати посилання ____________


 




# sync_data
