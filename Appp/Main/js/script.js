function showTime() {
	document.getElementById('currentTime').innerHTML = new Date().toUTCString();
}
showTime();
setInterval(function () {
	showTime();
}, 1000);
document.querySelector('form').addEventListener('submit', function (event) {
    const nameInput = document.getElementById('name');
    if (nameInput.value.trim() === '') {
        alert('Пожалуйста, введите имя студента.');
        event.preventDefault(); // Отменяет отправку формы
    } else {
        alert('Студент добавлен: ' + nameInput.value);
    }
});