document.getElementById('datauploadForm').addEventListener('submit', function(event) {
    event.preventDefault(); 
    const progressBarContainer = document.getElementById('progressBarContainer');
    progressBarContainer.classList.remove('d-none');

    const progressBar = document.getElementById('progressBar');
    progressBar.style.width = '0%';
    progressBar.innerText = '0%';

    const formData = new FormData(this);

    const xhr = new XMLHttpRequest();
    xhr.open('POST', this.action, true);

    xhr.upload.addEventListener('progress', function(e) {
        if (e.lengthComputable) {
            const percentComplete = (e.loaded / e.total) * 100;
            progressBar.style.width = percentComplete + '%'; 
            progressBar.innerText = Math.round(percentComplete) + '%'; 
        }
    });

    xhr.onload = function() {
        if (xhr.status >= 200 && xhr.status < 300) {
            Swal.fire({
                title: "Success!",
                text: "File uploaded successfully!",
                icon: "success",
                timer: 2000,
                showConfirmButton: false
            }).then(() => {
                window.location.href = '/company'; 
            });
        } else {
            Swal.fire({
                title: "Error!",
                text: "Upload failed. Please try again.",
                icon: "error",
                confirmButtonText: "Okay"
            });
        }
        progressBarContainer.classList.add('d-none'); 
    };

    xhr.onerror = function() {
        Swal.fire({
            title: "Error!",
            text: "Upload failed. Please try again.",
            icon: "error",
            confirmButtonText: "Okay"
        });
        progressBarContainer.classList.add('d-none');
    };

    xhr.send(formData);
});
