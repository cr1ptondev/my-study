jQuery(document).ready(function ($) {
    // Объект для хранения выбранных фильтров
    let filters = {
        work_type: '', // Тип работы (например, Лендинг, Корпоративный сайт и т. д.)
        theme: ''      // Тематика работы (например, Недвижимость, Автосалон и т. д.)
    };

    // Функция для загрузки отфильтрованного портфолио через AJAX
    function loadFilteredPortfolio() {
        $.ajax({
            url: initialData.ajax_url, // URL обработчика AJAX-запроса
            type: 'POST', // Метод отправки данных
            dataType: 'json', // Формат получаемых данных (JSON)
            data: {
                action: 'filter_portfolio', // Название действия для обработчика на сервере
                work_type: filters.work_type, // Передаем выбранный тип работы
                theme: filters.theme // Передаем выбранную тематику
            },
            beforeSend: function () {
                // Перед загрузкой данных показываем индикатор загрузки
                $('.portfolio__wrapper').html('<p>Загрузка...</p>');
            },
            success: function (response) {
                // После успешного запроса обновляем HTML с портфолио
                $('.portfolio__wrapper').html(response.html);
                // Обновляем счетчики фильтров
                updateFilterCounts(response.counts);
            },
            error: function () {
                // В случае ошибки показываем сообщение
                $('.portfolio__wrapper').html('<p>Ошибка загрузки</p>');
            }
        });
    }

    // Функция для обновления счетчиков фильтров (сколько работ в каждой категории)
    function updateFilterCounts(counts) {
        $('.filter-item').each(function () {
            let type = $(this).data('type'); // Определяем тип фильтра (work_type или theme)
            let slug = $(this).data('filter'); // Получаем значение фильтра (например, 'seo', 'real-estate')
            let count = counts[type] && counts[type][slug] ? counts[type][slug] : 0; // Получаем количество работ в данной категории
            $(this).find('.filter-amount').text(count); // Обновляем отображаемое количество

            // Скрываем тематики, если они не относятся к выбранному типу работы
            if (type === 'theme') {
                if (counts['theme_available'] && counts['theme_available'].includes(slug)) {
                    $(this).show(); // Показываем тематику, если она есть в текущем выборе
                } else {
                    $(this).hide(); // Скрываем, если работ с этой тематикой нет
                }
            }
        });

        // Обновляем общий счетчик работ
        $('.filter-show-total').text(counts.all);
        $('.filter-show-from').text(counts.filtered);

        // Обновляем количество работ в кнопке "Все"
        $('.filter-item[data-filter=""]').find('.filter-amount').text(counts.all);
    }

    // Обработчик клика по фильтру
    $('.filter-item').on('click', function () {
        let type = $(this).data('type'); // Получаем тип фильтра (work_type или theme)
        let value = $(this).data('filter'); // Получаем значение фильтра

        // Если фильтр уже активен, снимаем его; иначе выбираем новый
        filters[type] = filters[type] === value ? '' : value;

        // Удаляем активный класс у всех элементов данного типа
        $('.filter-item[data-type="' + type + '"]').removeClass('active');

        if (filters[type]) {
            $(this).addClass('active'); // Добавляем класс активного элемента
        } else {
            // Если фильтр снят, активируем кнопку "Все"
            $('.filter-item[data-type="' + type + '"][data-filter=""]').addClass('active');
        }

        // Перезагружаем портфолио с новыми фильтрами
        loadFilteredPortfolio();
    });

    // Обработчик кнопки сброса фильтров
    $('.filter-reset').on('click', function () {
        filters = { work_type: '', theme: '' }; // Сбрасываем фильтры
        $('.filter-item').removeClass('active'); // Убираем активные классы
        $('.filter-item[data-filter=""]').addClass('active'); // Делаем активной кнопку "Все"
        loadFilteredPortfolio(); // Загружаем полный список работ
    });

    // Первоначальная загрузка портфолио при загрузке страницы
    loadFilteredPortfolio();
});
