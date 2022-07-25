$(window).on('load', function() {
    $('.c-toggle').on('click', function (e) {
        var id = e.target.id.slice(5);
        if ($(this).attr('aria-expanded') === 'false') {
            var x = document.getElementById(e.target.id).getBoundingClientRect().x;
            var inner_w = window.innerWidth;
            if (x > inner_w / 2) {
                document.getElementById(id).classList.add("r-dropdown");
            }
        }
    });

    $('.carousel').carousel({
        interval: 2000
    });

});
function getCsrfToken() {
	return getCooke("csrftoken");
}
function getCooke(name) {
	var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$( document ).ajaxSend(function( event, jqxhr, settings ) {
    jqxhr.setRequestHeader("X-CSRFToken", getCsrfToken());
});

$('#searchinput').keypress(function (e) {
    if (e.which === 13) {
        var keyword = $('#searchinput').val();
        window.location.href = '/search?keyword=' + keyword;
    }

})
$('#mobilesearchinput').keypress(function (e) {
    if (e.which === 13) {
        var keyword = $('#mobilesearchinput').val();
        window.location.href = '/search?keyword=' + keyword;
    }

})

function explore_content(id){
    window.location.href = "/contents/" + id;
}

function gopage(i) {
    var cur_path = window.location.href;
    window.location.href = cur_path + "&page=" + i;
}
function contactus() {
    redirect('/contact_us');
}
function visit_site(url){
    redirect(url);
}
function redirect(url) {
    window.location.href = url;
}
function contact() {
    var email = $('#contact_email').val();
    var mes = $('#contact_message').val();
    var param = {
        email: email,
        mes: mes
    };
    $.ajax({
        type: "POST",
        url: "/contact",
        data: param,
        success: function (res) {
            console.log(res)
        }
    })
}
function mcontact() {
    var email = $('#m_contact_email').val();
    var mes = $('#m_contact_message').val();
    var param = {
        email: email,
        mes: mes
    };
    $.ajax({
        type: "POST",
        url: "/contact",
        data: param,
        success: function (res) {
            console.log(res)
        }
    })
}