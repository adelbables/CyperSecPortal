$(document).ready(function () {
    $(".files").attr('data-before', "Drag file here or click the above button");
    $('input[type="file"]').change(function (e) {
        let fileName = e.target.files[0].name;
        $(".files").attr('data-before', fileName);

    });
});

$('#encrypt_button').on('click', function (e) {
    if (!confirm('Your secret was successfully encrypted into the image. confirm download?')) {
        e.preventDefault();
    }

});
