var refreshNotification = 
    function(){
        $('#live_data').load('/live');
    };

jQuery(document).ready(function(){
    var autoRefresh = setTimeout(refreshNotification, 2000);
});
