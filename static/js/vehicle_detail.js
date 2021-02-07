$(document).ready(function(){
    const tradeinDiv = $('#trade-in');
    const tradeinInput = $('#trade-in-input');
    tradeinInput.on('change', function(){
        if (tradeinInput.prop('checked')){
            tradeinDiv.show();
        } else {
            tradeinDiv.hide();
        }
    });

    setInterval(function(){
        const vehicle_id = $('#vehicle-id').val();
        const sale_state = $('#sale-state');
        const reserve_button = $('#reserve-button');

        $.ajax({
            url: '/buy/sale-state/' + vehicle_id, 
            success: function(data){
                if (data !== sale_state.text()){
                    if(data == 'Sold' || data == 'Reserved'){
                        reserve_button.hide();
                    } else {
                        reserve_button.show();
                    }
                    sale_state.text(data);
                }
            }
        })
    }, 5000);

});