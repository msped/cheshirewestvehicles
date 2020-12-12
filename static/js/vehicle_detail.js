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
});