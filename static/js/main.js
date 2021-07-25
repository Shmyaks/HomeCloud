jQuery(function () {
    modal = $('exampleModal')

    // $('#change_path').on('click', function () {
    //     id = this.value()
    //     $.ajax({
    //         type: 'PATCH',
    //         contentType: "application/json",
    //         url: "/path" + id,
    //         success: function (data) {

    //         }
    //     });
    // })

    $('#delete_path').on('click', function () {
        id = this.value
        console.log(id)
        $.ajax({
            type: 'DELETE',
            contentType: "application/json",
            url: "/path/" + id,
            success: function () {
                location.replace("/settings")
            }
        });
    })

    $('#create_path').on('click', function () {
        $('.modal-body').empty()
            html_input = $(`<div class="mb-3">
        <label for="exampleInputpath" class="form-label">Укажите путь до папки с видеофайлами</label>
        <input type="text" class="form-control" id="exampleInputpath" aria-describedby="emailHelp">
        </div>`)
        html_input.appendTo('.modal-body')

    })

    $("#Succes_btn").on('click', function () {
        path = $('#exampleInputpath').val()
        request = $.post('/path', { path: `${path}`})
            .done(function () {
                location.replace("/settings")
            })
    });
});