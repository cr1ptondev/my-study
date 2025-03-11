<?php 

// Функция для подключения скриптов
function enqueue_scripts() {
    // Подключаем скрипт фильтрации с зависимостью от jQuery
    wp_enqueue_script('filter-script', get_template_directory_uri() . '/js/filter.js', array('jquery'), null, true);

    // Передаем AJAX URL в скрипт для работы с AJAX-запросами
    wp_localize_script('filter-script', 'initialData', array(
        'ajax_url' => admin_url('admin-ajax.php') // URL для обработки AJAX-запросов
    ));
}

// Добавляем функцию enqueue_scripts в хуки для подключения скриптов на фронтенде
add_action('wp_enqueue_scripts', 'enqueue_scripts');


// Функция обработки AJAX-запроса фильтрации портфолио
function filter_portfolio() {
    // Получаем параметры фильтра из POST-запроса и очищаем их
    $work_type = isset($_POST['work_type']) ? sanitize_text_field($_POST['work_type']) : '';
    $theme = isset($_POST['theme']) ? sanitize_text_field($_POST['theme']) : '';

    // Создаем массив условий для фильтрации (по умолчанию - AND)
    $tax_query = array('relation' => 'AND');

    // Если выбран work_type, добавляем его в запрос
    if (!empty($work_type)) {
        $tax_query[] = array(
            'taxonomy' => 'work_type', // Используем таксономию "work_type"
            'field'    => 'slug', // Фильтруем по slug
            'terms'    => $work_type, // Значение фильтра
        );
    }

    // Если выбрана theme, добавляем ее в запрос
    if (!empty($theme)) {
        $tax_query[] = array(
            'taxonomy' => 'theme', // Используем таксономию "theme"
            'field'    => 'slug', // Фильтруем по slug
            'terms'    => $theme, // Значение фильтра
        );
    }

    // Параметры запроса к WP_Query для получения работ портфолио
    $args = array(
        'post_type'      => 'portfolio', // Тип постов - "portfolio"
        'posts_per_page' => -1, // Выводим все посты
        'orderby'        => 'menu_order', // Упорядочиваем по полю "menu_order"
        'order'          => 'desc', // В порядке убывания
        'tax_query'      => !empty($tax_query) ? $tax_query : array(), // Добавляем фильтр по таксономиям
    );

    $ajaxposts = new WP_Query($args); // Выполняем запрос
    $response = '';

    // Если есть записи в портфолио, загружаем их
    if ($ajaxposts->have_posts()) {
        while ($ajaxposts->have_posts()) : $ajaxposts->the_post();
            ob_start(); // Начинаем буферизацию вывода
            include('layout/portfolio_item.php'); // Подключаем шаблон карточки портфолио
            $response .= ob_get_clean(); // Добавляем его в переменную response
        endwhile;
    } else {
        $response = '<p>Пусто</p>'; // Если записей нет, возвращаем сообщение
    }

    // Подсчет количества работ по фильтрам
    $counts = array(
        'all'       => wp_count_posts('portfolio')->publish, // Общее количество опубликованных работ
        'filtered'  => $ajaxposts->found_posts, // Количество работ после фильтрации
        'work_type' => array(), // Количество работ по work_type
        'theme'     => array(), // Количество работ по theme
        'theme_available' => array() // Список доступных тематик
    );

    // Получаем список всех типов работ (work_type)
    $work_types = get_terms(array('taxonomy' => 'work_type', 'hide_empty' => false));
    foreach ($work_types as $type) {
        $query = new WP_Query(array(
            'post_type' => 'portfolio',
            'tax_query' => array(array(
                'taxonomy' => 'work_type',
                'field'    => 'slug',
                'terms'    => $type->slug
            ))
        ));
        // Сохраняем количество работ в каждом work_type
        $counts['work_type'][$type->slug] = $query->found_posts;
    }

    // Получаем список всех тематик (theme)
    $themes = get_terms(array('taxonomy' => 'theme', 'hide_empty' => false));
    foreach ($themes as $theme) {
        $query = new WP_Query(array(
            'post_type' => 'portfolio',
            'tax_query' => array(array(
                'taxonomy' => 'theme',
                'field'    => 'slug',
                'terms'    => $theme->slug
            ))
        ));
        // Сохраняем количество работ в каждой theme
        $counts['theme'][$theme->slug] = $query->found_posts;

        // Проверяем, есть ли работы с данной тематикой в выбранном work_type
        if (!empty($work_type)) {
            $theme_query = new WP_Query(array(
                'post_type' => 'portfolio',
                'tax_query' => array(
                    array(
                        'taxonomy' => 'work_type',
                        'field'    => 'slug',
                        'terms'    => $work_type,
                    ),
                    array(
                        'taxonomy' => 'theme',
                        'field'    => 'slug',
                        'terms'    => $theme->slug,
                    ),
                ),
            ));

            // Если есть работы, добавляем тематику в список доступных
            if ($theme_query->found_posts > 0) {
                $counts['theme_available'][] = $theme->slug;
            }
        } else {
            // Если фильтр work_type не выбран, добавляем все темы
            $counts['theme_available'][] = $theme->slug;
        }
    }

    // Отправляем JSON-ответ с HTML-кодом портфолио и обновленными счетчиками
    echo json_encode(array(
        'html'   => $response,
        'counts' => $counts
    ));
    exit; // Завершаем выполнение скрипта
}

// Регистрируем обработчик AJAX-запроса для авторизованных пользователей
add_action('wp_ajax_filter_portfolio', 'filter_portfolio');

// Регистрируем обработчик AJAX-запроса для неавторизованных пользователей
add_action('wp_ajax_nopriv_filter_portfolio', 'filter_portfolio');

?>