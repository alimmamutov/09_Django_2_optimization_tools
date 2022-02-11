function orders() {
    let quantity, price, orderitem_num, delta_quantity, orderitem_quantity, delta_cost
    let quantity_arr = []
    let price_arr = []

    let total_forms = parseInt($('input[name=orderitems-TOTAL_FORMS]').val()); // Здесь получаем количество строк таблицы
    // $ - это функция поиска из библиотеки jQuery, можно так же вызвать - jQuery('здесь указываем что ищем - тег[параметры тега]')
    console.log(total_forms);
     let total_quantity = parseInt($(
}
window.addEventListener('DOMContentLoaded', orders);