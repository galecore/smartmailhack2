axios.get('/')
  .then(function (response) {
    // handle success
    console.log(response);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed
  });

var cards = new Vue({
  el: '#main',
  data: {
    sales: [
      { start: '12.04.2018', stop: '12.04.2018', sale: '99%',  text: 'скидка на iphone 99%', discript: 'в магазине мтс скидка на iphon '},
{ iurl: 'https://www.verybank.ru/static/banks/logo/min/000/53ed9ac869f2216b7df49fe1464b066a.png',start: '12.04.2018', stop: '12.04.2018', sale: '99%',  text: 'скидка на iphone 99%', discript: 'в магазине мтс скидка на iphon '},
{ start: '12.04.2018', stop: '12.04.2018', sale: '99%',  text: 'скидка на iphone 99%', discript: 'в магазине мтс скидка на iphon '},
{ start: '12.04.2018', stop: '12.04.2018', sale: '99%',  text: 'скидка на iphone 99%', discript: 'в магазине мтс скидка на iphon '}
    ]
  }
})
