jQuery(document).ready(function(){
    var pathname = window.location.pathname;
    var refreshNotification = 
        function(){
            $('#live_data').load(pathname);
        };
    setTimeout(refreshNotification, 3000);
});
