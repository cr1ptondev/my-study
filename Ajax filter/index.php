<section class="case">
    <div class="container">
        <h1>Портфолио</h1>
        <div class="case__wrapper">
            <!-- Фильтр по типу работы -->
            <div class="case__row">
                <h6>Тип работы</h6>
                <div class="filter">
                    <div class="flex align-center filter-flex">
                        <!-- Элемент фильтра "Все" с общим количеством работ -->
                        <div class="filter-item active" data-type="work_type" data-filter="">
                            <p class="descr filter-title">Все</p>
                            <p class="descr filter-amount">
                                <?php echo wp_count_posts('portfolio')->publish; // Выводим общее количество опубликованных работ ?>
                            </p>
                        </div>
                        <?php
                        // Получаем список всех типов работ (таксономия "work_type")
                        $work_types = get_terms(array('taxonomy' => 'work_type', 'hide_empty' => true));

                        // Проверяем, что список не пустой и нет ошибок
                        if (!empty($work_types) && !is_wp_error($work_types)) {
                            foreach ($work_types as $type) {
                                echo '<div class="filter-item" data-type="work_type" data-filter="'.esc_attr($type->slug).'">
                                    <p class="descr filter-title">'.esc_html($type->name).'</p>
                                    <p class="descr filter-amount">'.esc_html($type->count).'</p></div>';
                                // Выводим название типа работы и количество записей в нем
                            }
                        }
                        ?>
                    </div>
                </div>
            </div>

            <!-- Фильтр по тематике -->
            <div class="case__row">
                <h6>Тематика</h6>
                <div class="filter">
                    <div class="flex align-center filter-flex">
                        <!-- Элемент фильтра "Все" с общим количеством работ -->
                        <div class="filter-item" data-type="theme" data-filter="">
                            <p class="descr filter-title">Все</p>
                            <p class="descr filter-amount">
                                <?php echo wp_count_posts('portfolio')->publish; // Выводим общее количество опубликованных работ ?>
                            </p>
                        </div>
                        <?php
                        // Получаем список всех тематик (таксономия "theme")
                        $themes = get_terms(array('taxonomy' => 'theme', 'hide_empty' => true));

                        // Проверяем, что список не пустой и нет ошибок
                        if (!empty($themes) && !is_wp_error($themes)) {
                            foreach ($themes as $theme) {
                                echo '<div class="filter-item" data-type="theme" data-filter="'.esc_attr($theme->slug).'">
                                    <p class="descr filter-title">'.esc_html($theme->name).'</p>
                                    <p class="descr filter-amount">'.esc_html($theme->count).'</p></div>';
                                // Выводим название тематики и количество записей в ней
                            }
                        }
                        ?>
                    </div>
                </div>
            </div>
        </div>

        <!-- Блок управления фильтрацией -->
        <div class="flex align-center filter-flex-wrap">
            <div class="btn filter-reset">Сбросить фильтр</div>
            <p class="descr filter-show-result">
                Показано <span class="filter-show-from">26</span> работ из <span class="filter-show-total">500</span>
            </p>
        </div>
    </div>
</section>
