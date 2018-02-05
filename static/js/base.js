$(function () {$.ajax({
    url: '/product/get-categories/',
    dataType: 'json',
    type: 'GET',
    success: function( data, status, xhr ){
        var count = 1;
        $.each(data, function (key, element) {
            var li = $('<li>', {'class': 'nav-item dropdown'});
            li.append($('<a>', {'class': 'nav-link dropdown-toggle', 'id': 'category' + count, 'data-toggle': 'dropdown',
                                'aria-haspopup': 'true', 'aria-expanded': 'true', 'style': 'color: #383d41;', 'text': key}));
            var div = $('<div>', {'class': 'dropdown-menu', 'aria-labelledby': 'category' + count})
            $.each(element, function (key, element) {
                div.append($('<a>', {'class': 'dropdown-item', 'href': '#', 'text': element[1]}));
            });
            li.append(div);
            $('#navbars-sub-top > ul').append(li);
            count++;
        });
    },
    error: function( xhr, status, error ){
        console.log( error );
    }
})});