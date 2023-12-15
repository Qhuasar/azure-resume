window.addEventListener('DOMContentLoaded', (event) => {
  getVisitCount();
});

const import_api = 'http://localhost:7071/api/GetCounter';

const getVisitCount = () => {
  let count = 30;
  fetch(import_api)
    .then((response) => {
      return response.json();
    })
    .then((response) => {
      console.log('Website called function API');
      count = response.count;
      document.getElementById('counter').innerText = count;
    })
    .catch((error) => {
      console.log(error);
    });
};
