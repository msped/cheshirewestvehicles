$(document).ready(function(){
    function get_total(){
        var total = 0;
        $('.total').each(function () {
            current = $(this);
            total += parseFloat(current.val()) || 0;  
        });
        $('#invoice-total').html(total.toFixed(2));
        $('input[name="invoice-total"]').val(total.toFixed(2));
    }

    $('tbody').on('click', '.fa-trash-alt', function() {
        const row = $(this).closest('tr');
        row.remove();
        get_total();
    });

    $('tbody').on('input', '.qty, .unit-price', function(){
        const tr = $(this).closest('tr');
        let qty = tr.find('td>input.qty').val();
        let unit_price = tr.find('td>input.unit-price').val();
        const total_box = tr.find('td>input.total');
        total = qty * unit_price;
        total_box.val(total);
        get_total();
    });

    $('.add-line').on('click', function(){
        let tr_number = $('#work-table tr').last().data('value');
        tr_number++;
        template = '<tr data-value="' + tr_number + '">' +
                        '<td>' +
                            '<input type="text" name="description-' + tr_number + '" class="form-control" required>' +
                        '</td> '+
                        '<td>' +
                            '<input type="number" name="qty-' + tr_number + '" class="form-control qty" min="0" oninput="validity.valid||(value=\'\');" required>' +
                        '</td>' +
                        '<td> '+
                            '<input type="number" name="unit-' + tr_number + '" class="form-control unit-price" min="0" oninput="validity.valid||(value=\'\');" required>' +
                        '</td>' +
                        '<td>' +
                            '<input type="number" name="line-' + tr_number + '" class="form-control total" min="0" oninput="validity.valid||(value=\'\');" required>' +
                        '</td>' +
                        '<td>' + 
                            '<div class="text-center">' +
                                '<i class="fas fa-trash-alt"></i>' +
                            '</div>' +
                        '</td>' + 
                    '</tr>';
        $('tbody').append(template);
    });
});