$(document).ready(function () {

    console.log("Hello, JazzWorld!");

    $("#musicians-ref").mouseover(function(){

        console.log("musicians ref!");

    });

    $("#styles-ref").mouseover(function(){

        console.log("styles ref!");

    });

    $("#clubs-ref").mouseover(function(){

        console.log("clubs ref!");

    });


    $(".quote-previous-wrapper").on("click", function(){
    
        console.log("previous hovered");
        var quote_id = $(this).data("quote-id");
        console.log("quote id is " + quote_id);


        $.ajax({
            type: "GET",
            url: "previous_quote/",
            data: {
                "quote_id": quote_id
            },
            success: function (data) {
                // Сообщение
                console.log("success!");

                $(".quote-wrapper").html(data.quote_html);

                $(".quote-next-wrapper").data("quote-id", data.quote_id);
                $(".quote-previous-wrapper").data("quote-id", data.quote_id);

                console.log($(".quote-next-wrapper").data("quote-id"), $(".quote-previous-wrapper").data("quote-id"));

            },

            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });


    });

    $(".quote-next-wrapper").on("click", function(){

        console.log("next hovered");
        var quote_id = $(this).data("quote-id");
        console.log("quote id is " + quote_id);


        $.ajax({
            type: "GET",
            url: "next_quote/",
            data: {
                "quote_id": quote_id
            },
            success: function (data) {
                // Сообщение
                console.log("success!");

                $(".quote-wrapper").html(data.quote_html);

                $(".quote-next-wrapper").data("quote-id", data.quote_id);
                $(".quote-previous-wrapper").data("quote-id", data.quote_id);

                console.log($(".quote-next-wrapper").data("quote-id"), $(".quote-previous-wrapper").data("quote-id"));

            },

            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });

    });

});