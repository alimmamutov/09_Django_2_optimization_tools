
function orders() {
    let quantity, price, orderitem_num, delta_quantity, orderitem_quantity, delta_cost
    let quantity_arr = []
    let price_arr = []

    let total_forms = parseInt($('input[name=orderitems-TOTAL_FORMS]').val()); // Здесь получаем количество строк таблицы
    // $ - это функция поиска из библиотеки jQuery, можно так же вызвать - jQuery('здесь указываем что ищем - тег[параметры тега]')

    console.log(total_forms);
    let order_total_quantity = parseInt($('.order_total_quantity').text()) || 0; // Если нет, то 0 по умолчанию
    let order_total_cost = parseInt($('.order_total_cost').text().replace(',','.')) || 0; // здесь получаем общее количество
     // $ - здесь получаем по названию класса .название класса


     for (let i = 0; i< total_forms; i++){
        quantity = parseInt($('input[name=orderitems-' + i + '-quantity]').val());
        price = parseInt($('.orderitems-' + i + '-price').text().replace(',', '.'));

        quantity_arr[i] = quantity;
        if (price){
            price_arr[i] = price;
        }
        else{
            price_arr[i] = 0;
        }
     }

     console.info('QUANTITY', quantity_arr);
     console.info('PRICE', price_arr);

    // 1 метод
    $('.order_form').on('click', 'input[type=number]',function(){
            let target = event.target;
            orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-quantity',''));
            if (price_arr[orderitem_num]){
                orderitem_quantity = parseInt(target.value);
                delta_quantity =orderitem_quantity - quantity_arr[orderitem_num];
                quantity_arr[orderitem_num] = orderitem_quantity;
                orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
            }
        }
    )

    function orderSummaryUpdate(orderitem_price, delta_quantity){
        delta_cost = orderitem_price * delta_quantity;
        order_total_cost = Number((order_total_cost + delta_cost).toFixed(2));
        order_total_quantity = order_total_quantity + delta_quantity;
        $('.order_total_quantity').html(order_total_quantity.toString());
        $('.order_total_cost').html(order_total_cost.toString() + ',00');
    }
}

function last_row_add(){
    let total_forms = parseInt($('input[name=orderitems-TOTAL_FORMS]').val());
    let tbody = document.getElementsByTagName('tbody');
    tbody[0].insertAdjacentHTML('beforeend',html_row_markup(total_forms));
    $('input[name=orderitems-TOTAL_FORMS]')[0].value = total_forms + 1;
}

function html_row_markup(id){
    return `
        <tr class="formset_row">
        <td class="td1 order formset_td">
        <input type="hidden" name="orderitems-`+id+`-order" id="id_orderitems-`+id+`-order">
        <input type="hidden" name="orderitems-`+id+`-id" id="id_orderitems-`+id+`-id">
        <select name="orderitems-`+id+`-product" class="form-control" id="id_orderitems-`+id+`-product">
            <option value="" selected="">---------</option>
            <option value="1">Худи черного цвета с монограммами adidas Originals | Одежда</option>
            <option value="2">Синяя куртка The North Face | Одежда</option>
            <option value="3">Коричневый спортивный oversized-топ ASOS DESIGN | Одежда</option>
            <option value="4">Черный рюкзак Nike Heritage | Аксесуары</option>
            <option value="5">Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex | Обувь</option>
            <option value="6">Темно-синие широкие строгие брюки ASOS DESIGN | Новинки</option>
        </select>
        </td>

        <td class="td2 order formset_td">
        <input type="number" name="orderitems-`+id+`-quantity" value="0" min="0" class="form-control" id="id_orderitems-`+id+`-quantity">
        </td>
        <td class="td3 order formset_td">
        <span class="orderitems-`+id+`-price">0,00 руб</span>
        </td>
        <td class="td1 order formset_td">
        <input type="checkbox" name="orderitems-`+id+`-DELETE" id="id_orderitems-`+id+`-DELETE">
        </td>
        </tr>
    `
}

window.addEventListener('DOMContentLoaded', orders);
window.addEventListener('DOMContentLoaded', last_row_add);