$(function () {$.ajax({
    url: '/product/get-categories/',
    dataType: 'json',
    type: 'GET',
    success: function( data, textStatus, jQxhr ){
        var count = 1;
        $.each(data, function (key, element) {
            var li = $('<li>', {'class': 'nav-item dropdown'});
            li.append($('<a>', {'class': 'nav-link dropdown-toggle', 'id': 'category' + count, 'data-toggle': 'dropdown',
                                'aria-haspopup': 'true', 'aria-expanded': 'true', 'text': key}));
            var div = $('<div>', {'class': 'dropdown-menu', 'aria-labelledby': 'category' + count})
            $.each(element, function (key, element) {
                //TODO element, 네임 설정
                div.append($('<a>', {'class': 'dropdown-item', 'href': '#', 'text': element[1]}));
            });
            li.append(div);
            $('#navbars-sub-top > ul').append(li);
            count++;
        });
    },
    error: function( jqXhr, textStatus, errorThrown ){
        console.log( errorThrown );
    }
})});