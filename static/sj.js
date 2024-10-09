function uploadImage() {
    var input = document.getElementById('myfile');
    var file = input.files[0];
   

    if (file) {
     var formData = new FormData();
        formData.append('image', file);

        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .catch(error => console.error('Error:', error));
    } else {
        alert('Please select an image.');
    }
}