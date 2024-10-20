
$("#userForm").submit(function(e) {
    e.preventDefault();
    var serializedData = $(this).serialize();

    $.ajax({
        url: 'add_user', 
        type: 'POST',
        data: serializedData,
        beforeSend: function() {
          
        },
        complete: function() {
        },
        success: function(response) {
            new swal("Success", response.msg, "success").then(() => {
                window.location.reload(); 
            });
            $(this).trigger('reset');
        },
        error: function(response) {
            new swal("Oops!", response.responseJSON.msg || "Failed to insert record", "error");
        }
    });
});



$(".edit-user-btn").click(function() {

    var user_id = $(this).data('id');
    var name = $(this).data('name');
    var username = $(this).data('username');
    var isActive = $(this).data('is_active');

    $("#editUserId").val(user_id);
    $("#editName").val(name);
    $("#editUsername").val(username);
    var status = (isActive === "True") ? "1" : "0"; 

    $("#status").val(status);

    $('#EditAccountModal').modal('show');
});


$("#editUserForm").submit(function(e) {
    e.preventDefault(); 

    var formData = $(this).serialize();

    $.ajax({
        url: $(this).attr('action'),
        type: 'POST', 
        data: formData, 
        beforeSend: function() {
        },
        success: function(response) {
            new swal("Success", response["msg"], "success").then(() => {
                location.reload(); 
            });
            $("#editUserForm").trigger('reset');
            $('#EditAccountModal').modal('hide');
        },
        error: function(response) {
            console.log('Hello')
            console.log(response)
            new swal("Oops!", "Failed to update record", "error");
        },
        complete: function() {
        }
    });
});



$(document).on('click', '.delete-user-btn', function(e) {
    e.preventDefault();
    var userId = $(this).data('id');

    Swal.fire({
        title: "Are you sure?",
        text: "Once deleted, you will not be able to recover this user!",
        icon: "warning",
        showCancelButton: true, 
        confirmButtonText: "Yes, delete it!",
        cancelButtonText: "No, cancel!"
    }).then((result) => {
        if (result.isConfirmed) {
            var csrftoken = document.cookie.split('; ').find(row => row.startsWith('csrftoken')).split('=')[1];
            console.log(csrftoken)
            $.ajax({
                url: '/delete_user/',
                type: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken 
                },
                data: {
                    id: userId 
                },
                success: function(response) {
                    Swal.fire("Success", response.msg, "success"); 
                    window.location.reload(); 
                },
                error: function(response) {
                    console.log(response)
                    Swal.fire("Oops!", "Failed to delete user", "error"); 
                }
            });
        } else {
            Swal.fire("Your user is safe!"); 
        }
    });
});

