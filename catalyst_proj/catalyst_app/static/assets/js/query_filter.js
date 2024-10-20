document.getElementById('searchBtn').addEventListener('click', function () {
    const formData = new FormData(document.getElementById('myForm'));

    fetch('/api/filter_company/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': '{{ csrf_token }}'
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); 

        let alerts = [];

        if (formData.get('industry') && data.industry_count > 0) {
            alerts.push({
                title: "Filtered Industry",
                text: 'Filtered Industry count: ' + data.industry_count,
            });
        }
        if (formData.get('company_name') && data.company_name_count > 0) {
            alerts.push({
                title: "Filtered Company Name",
                text: 'Filtered Company Name count: ' + data.company_name_count,
            });
        }
        if (formData.get('yr_founded') && data.year_founded_count > 0) {
            alerts.push({
                title: "Filtered Year Founded",
                text: 'Filtered Year Founded count: ' + data.year_founded_count,
            });
        }
        if (formData.get('country') && data.country_count > 0) {
            alerts.push({
                title: "Filtered Country",
                text: 'Filtered Country count: ' + data.country_count,
            });
        }

        const showAlertsSequentially = (alerts) => {
            return alerts.reduce((promise, alert) => {
                return promise.then(() => {
                    return Swal.fire({
                        title: alert.title,
                        text: alert.text,
                        icon: "info",
                        confirmButtonText: "OK",
                    });
                });
            }, Promise.resolve());
        };

        if (alerts.length > 0) {
            showAlertsSequentially(alerts);
        } else {
            Swal.fire({
                title: "No Results",
                text: "No filters returned any results.",
                icon: "info",
                confirmButtonText: "OK"
            });
        }

    })
    .catch(error => {
        console.error('Error:', error);
        Swal.fire({
            title: "Error",
            text: "An error occurred while fetching data. Please try again.",
            icon: "error",
            confirmButtonText: "OK"
        });
    });
});
