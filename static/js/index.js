function file_changed() {
    let file = $('#file').prop('files')[0];
    console.log(file.name)

    filename = file.name.split(".")[0]
    console.log(filename)
}

$(document).ready(function () {
    $("#submit_btn").click(function () {
        let formData = new FormData();
        formData.append('file', $('#file').prop('files')[0]);
        formData.append('title', $('#title').val().trim());

        let start = new Date().getTime();
        $.ajax({
            type: "POST",
            url: "/upload",
            data: formData,
            cache: false,
            contentType: false,
            processData: false,
            success: function (data) {
                $(".ui .form")[0].reset();
            },
            error: function (err) {
                console.log(err);
            },
        })
        let end = new Date().getTime();
        let time = end - start;
        console.log(time)
    });

    // Form Clear
    $("#clear_btn").click(function () {
        $(".ui .form")[0].reset();
    });
})