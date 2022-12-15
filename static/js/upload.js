$(document).ready(function(){
        $(".files").attr('data-before',"Drag file here or click the above button");
        $('input[type="file"]').change(function(e){
            let fileName = e.target.files[0].name;
            $(".files").attr('data-before',fileName);

        });
    });