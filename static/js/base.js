$(function () {
  window.category_queue = [];
  $.ajax({
    url: '/product/categories/eng/',
    dataType: 'json',
    type: 'GET',
    success: function( data, status, xhr ){
        var count = 1;
        window.categories = data;
        $.each(data, function (key, element) {
            var li = $('<li>', {'class': 'nav-item dropdown'});
            li.append($('<a>', {'class': 'nav-link dropdown-toggle', 'id': 'category' + count, 'data-toggle': 'dropdown',
                                'aria-haspopup': 'true', 'aria-expanded': 'true', 'style': 'color: #383d41;', 'text': key}));
            var div = $('<div>', {'class': 'dropdown-menu', 'aria-labelledby': 'category' + count})
            $.each(element, function (key, element) {
                div.append($('<a>', {'class': 'dropdown-item', 'href': '#', 'href': '/product/' + element[0] + '/','text': element[1]}));
            });
            li.append(div);
            $('#navbars-sub-top > ul').append(li);
            count++;
        });
        while(window.category_queue.length)
        {
          window.category_queue.pop()();
        }
    },
    error: function( xhr, status, error ){
        console.log( error );
    }
})});
