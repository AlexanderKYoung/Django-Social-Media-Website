function showNotifications() {
    const container = document.getElementById('notification-container');

    if (container.classList.contains('d-none')) {
        container.classList.remove('d-none');
    } else {
        container.classList.add('d-none');
    }
}

function getCookie(name){
    let cookieValue = null;
    if (document.cookie && document.cookie !== ''){
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function deleteNotification(deleteNotificationURL, redirect){
    const csrftoken = getCookie('csrftoken');
    let xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == XMLHttpRequest.DONE) {
            if (xmlhttp.status == 200){
                window.location.replace(reidrectURL);
            } else {
                alert('There was an error');
            }
        }
    };

    xmlhttp.open("DELETE", deleteNotificationURL, true);
    xmlhttp.setRequestHeader("X-CSRFToken", csrftoken);
    xmlhttp.send();
}