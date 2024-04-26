$(document).ready(function() {

    // jQuery validator method for custom validation
    // jQuery validator method for custom validation
    $.validator.addMethod('answercheck', function(value, element) {
        return this.optional(element) || /^\bcat\b$/.test(value);
        }, "Type the correct answer -_-");


    // Validate contactForm form
    $('#contactForm').validate({
        rules: {
            name: {
                required: true,
                minlength: 2
            },
            subject: {
                required: true,
                minlength: 4
            },
            number: {
                required: true,
                minlength: 5
            },
            email: {
                required: true,
                email: true
            },
            message: {
                required: true,
                minlength: 20
            }
        },
        messages: {
            name: {
                required: "Please enter your name.",
                minlength: "Your name must consist of at least 2 characters."
            },
            subject: {
                required: "Please enter a subject.",
                minlength: "Your subject must consist of at least 4 characters."
            },
            number: {
                required: "Please enter your phone number.",
                minlength: "Your phone number must consist of at least 5 characters."
            },
            email: {
                required: "Please enter your email address."
            },
            message: {
                required: "Please write something to send this form.",
                minlength: "Please write more than 20 characters."
            }
        },
        submitHandler: function(form) {
            $(form).ajaxSubmit({
                type: "POST",
                url: "/contact/contact_form/",
                success: function(response) {
                    $('#contactForm :input').prop('disabled', true);
                    $('#contactForm').fadeTo("slow", 1, function() {
                        $(this).find(':input').prop('disabled', true);
                        $(this).find('label').css('cursor', 'default');
                        $('#success').html(response.message).fadeIn();
                        $('.modal').modal('hide');
                        $('#success').modal('show');
                    });
                },
                error: function() {
                    $('#contactForm').fadeTo("slow", 1, function() {
                        $('#error').fadeIn();
                        $('.modal').modal('hide');
                        $('#error').modal('show');
                    });
                }
            });
        }
    });

});
