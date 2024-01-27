fetch('http://127.0.0.1:8000/main/api/cv/',
{
    method:"GET",
    credentials:'include',
})
  .then(response => response.json())
  .then(data => {
    // Обработка полученных данных
    console.log(data);
  })
  .catch(error => {
    // Обработка ошибок
    console.error('Ошибка при запросе данных:', error);
  });