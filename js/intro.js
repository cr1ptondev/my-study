// ---------------------------------------------------------------
// Обучение JavaScript с помощью сайта learn.javascript.ru
// ---------------------------------------------------------------

// Изначально JavaScript был создан, чтобы «сделать веб-страницы живыми».
// Программы на этом языке называются скриптами. Они могут встраиваться в HTML и выполняться автоматически при загрузке веб-страницы.
// Скрипты распространяются и выполняются, как простой текст. Им не нужна специальная подготовка или компиляция для запуска.
// Это отличает JavaScript от другого языка – Java.


// ---------------------------------------------------------------
// Почему JavaScript?
// ---------------------------------------------------------------

// Когда JavaScript создавался, у него было другое имя – «LiveScript». Однако, язык Java был очень популярен в то время, и было решено, что позиционирование JavaScript как «младшего брата» Java будет полезно.
// Со временем JavaScript стал полностью независимым языком со своей собственной спецификацией, называющейся ECMAScript, и сейчас не имеет никакого отношения к Java.

// Сегодня JavaScript может выполняться не только в браузере, но и на сервере или на любом другом устройстве, которое имеет специальную программу, называющуюся «движком» JavaScript.

// У браузера есть собственный движок, который иногда называют «виртуальная машина JavaScript».

// Разные движки имеют разные «кодовые имена». Например:

// V8 – в Chrome, Opera и Edge.
// SpiderMonkey – в Firefox.
// …Ещё есть «Chakra» для IE, «JavaScriptCore», «Nitro» и «SquirrelFish» для Safari и т.д.
// Эти названия полезно знать, так как они часто используются в статьях для разработчиков. Мы тоже будем их использовать. Например, если «функциональность X поддерживается V8», тогда «Х», скорее всего, работает в Chrome, Opera и Edge.


// ---------------------------------------------------------------
// Как работают движки?
// ---------------------------------------------------------------

// Движки сложны. Но основы понять легко.

// Движок (встроенный, если это браузер) читает («парсит») текст скрипта.
// Затем он преобразует («компилирует») скрипт в машинный язык.
// После этого машинный код запускается и работает достаточно быстро.
// Движок применяет оптимизации на каждом этапе. Он даже просматривает скомпилированный скрипт во время его работы, анализируя проходящие через него данные, и применяет оптимизации к машинному коду, полагаясь на полученные знания. В результате скрипты работают очень быстро.


// ---------------------------------------------------------------
// Что может JavaScript в браузере?
// ---------------------------------------------------------------

// Современный JavaScript – это «безопасный» язык программирования. Он не предоставляет низкоуровневый доступ к памяти или процессору, потому что изначально был создан для браузеров, не требующих этого.

// Возможности JavaScript сильно зависят от окружения, в котором он работает. Например, Node.js поддерживает функции чтения/записи произвольных файлов, выполнения сетевых запросов и т.д.

// В браузере для JavaScript доступно всё, что связано с манипулированием веб-страницами, взаимодействием с пользователем и веб-сервером.

// Например, в браузере JavaScript может:

// Добавлять новый HTML-код на страницу, изменять существующее содержимое, модифицировать стили.
// Реагировать на действия пользователя, щелчки мыши, перемещения указателя, нажатия клавиш.
// Отправлять сетевые запросы на удалённые сервера, скачивать и загружать файлы (технологии AJAX и COMET).
// Получать и устанавливать куки, задавать вопросы посетителю, показывать сообщения.
// Запоминать данные на стороне клиента («local storage»).


// ---------------------------------------------------------------
// Что НЕ может JavaScript в браузере?
// ---------------------------------------------------------------

// Возможности JavaScript в браузере ограничены ради безопасности пользователя. Цель заключается в предотвращении доступа недобросовестной веб-страницы к личной информации или нанесения ущерба данным пользователя.

// Примеры таких ограничений включают в себя:

// JavaScript на веб-странице не может читать/записывать произвольные файлы на жёстком диске, копировать их или запускать программы. Он не имеет прямого доступа к системным функциям ОС.

// Современные браузеры позволяют ему работать с файлами, но с ограниченным доступом, и предоставляют его, только если пользователь выполняет определённые действия, такие как «перетаскивание» файла в окно браузера или его выбор с помощью тега <input>.

// Существуют способы взаимодействия с камерой/микрофоном и другими устройствами, но они требуют явного разрешения пользователя. Таким образом, страница с поддержкой JavaScript не может незаметно включить веб-камеру, наблюдать за происходящим и отправлять информацию в ФСБ.

// Различные окна/вкладки не знают друг о друге. Иногда одно окно, используя JavaScript, открывает другое окно. Но даже в этом случае JavaScript с одной страницы не имеет доступа к другой, если они пришли с разных сайтов (с другого домена, протокола или порта).

// Это называется «Политика одинакового источника» (Same Origin Policy). Чтобы обойти это ограничение, обе страницы должны согласиться с этим и содержать JavaScript-код, который специальным образом обменивается данными.

// Это ограничение необходимо, опять же, для безопасности пользователя. Страница https://anysite.com, которую открыл пользователь, не должна иметь доступ к другой вкладке браузера с URL https://gmail.com и воровать информацию оттуда.

// JavaScript может легко взаимодействовать с сервером, с которого пришла текущая страница. Но его способность получать данные с других сайтов/доменов ограничена. Хотя это возможно в принципе, для чего требуется явное согласие (выраженное в заголовках HTTP) с удалённой стороной. Опять же, это ограничение безопасности.

// Подобные ограничения не действуют, если JavaScript используется вне браузера, например — на сервере. Современные браузеры предоставляют плагины/расширения, с помощью которых можно запрашивать дополнительные разрешения.


// ---------------------------------------------------------------
// Что делает JavaScript особенным?
// ---------------------------------------------------------------

// Как минимум, три сильные стороны JavaScript:

// Полная интеграция с HTML/CSS.
// Простые вещи делаются просто.
// Поддерживается всеми основными браузерами и включён по умолчанию.
// JavaScript – это единственная браузерная технология, сочетающая в себе все эти три вещи.

// Вот что делает JavaScript особенным. Вот почему это самый распространённый инструмент для создания интерфейсов в браузере.

// Хотя, конечно, JavaScript позволяет делать приложения не только в браузерах, но и на сервере, на мобильных устройствах и т.п.


// ---------------------------------------------------------------
// Языки «над» JavaScript
// ---------------------------------------------------------------

// Синтаксис JavaScript подходит не под все нужды. Разные люди хотят иметь разные возможности.

// Это естественно, потому что проекты разные и требования к ним тоже разные.

// Так, в последнее время появилось много новых языков, которые транспилируются (конвертируются) в JavaScript, прежде чем запустятся в браузере.

// Современные инструменты делают транспиляцию очень быстрой и прозрачной, фактически позволяя разработчикам писать код на другом языке, автоматически преобразуя его в JavaScript «под капотом».

// Примеры таких языков:

// CoffeeScript добавляет «синтаксический сахар» для JavaScript. Он вводит более короткий синтаксис, который позволяет писать чистый и лаконичный код. Обычно такое нравится Ruby-программистам.
// TypeScript концентрируется на добавлении «строгой типизации» для упрощения разработки и поддержки больших и сложных систем. Разработан Microsoft.
// Flow тоже добавляет типизацию, но иначе. Разработан Facebook.
// Dart стоит особняком, потому что имеет собственный движок, работающий вне браузера (например, в мобильных приложениях). Первоначально был предложен Google, как замена JavaScript, но на данный момент необходима его транспиляция для запуска так же, как для вышеперечисленных языков.
// Brython транспилирует Python в JavaScript, что позволяет писать приложения на чистом Python без JavaScript.
// Есть и другие. Но даже если мы используем один из этих языков, мы должны знать JavaScript, чтобы действительно понимать, что мы делаем.


// ---------------------------------------------------------------
// Итого
// ---------------------------------------------------------------

// JavaScript изначально создавался только для браузера, но сейчас используется на многих других платформах.
// Сегодня JavaScript занимает уникальную позицию в качестве самого распространённого языка для браузера, обладающего полной интеграцией с HTML/CSS.
// Многие языки могут быть «транспилированы» в JavaScript для предоставления дополнительных функций. Рекомендуется хотя бы кратко рассмотреть их после освоения JavaScript.