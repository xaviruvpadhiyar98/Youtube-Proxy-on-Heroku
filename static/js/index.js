$(document).ready(() => {
    $("form").submit((e) => {
        var formData = {
            search: $("input").val()
        }
        console.log(formData)
        $.ajax({
            type: "POST",
            url: "/search/",
            data: formData,
            dataType: "json",
            encode: true,
        })
            .done((data) => console.log(data))
            .fail((data) => console.log("Server Error!"))
        $(".box").css({ top: 200, left: 200, position: 'absolute' });
        e.preventDefault()
    })
})