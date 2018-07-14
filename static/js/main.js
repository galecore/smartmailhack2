// DOM element where the Timeline will be attached
$.getJSON( "data/letters.json", function( data ) {

var container = document.getElementById('vis');


console.log('dd');
console.log(data);
// Create a DataSet (allows two way data-binding)


var items = new vis.DataSet([
  {id: 1, content: 'item 1', start: '2018-04-20'},
  {id: 2, content: 'item 2', start: '2018-04-15', end: '2018-04-18', style: 'border-radius: 10px; color: pink'},
  {id: 3, content: 'item 3', start: '2018-04-16', end: '2018-04-17'},
  {id: 4, content: 'item 4', start: '2018-04-16', end: '2018-04-19'},
  {id: 5, content: 'item 5', start: '2018-04-25'},
  {id: 6, content: 'item 6', start: '2018-04-27'}
]);


// Configuration for the Timeline
var options = {
  template: function (item, element, data) {
  console.log(data);
  return '' + data.content   + '  <span class="badge badge-danger"> '+ data.discount  + '</snap>'+'';
},
width: '100%',
height: '250px',
locale: 'ru',
min: '2018-01-01',
max:'2018-12-30',
timeAxis :  { scale: 'week', step:1 }
};

var items2 = [];
var tmp=1;
for (let i of data){
  let tmp2= i.data.from.split('.');
  let tmp3= i.data.to.split('.');
  let tmp4;
  tmp4=tmp2[2];
  tmp2[2]=tmp2[0];
  tmp2[0]=tmp4;
  tmp4=tmp3[2];
  tmp3[2]=tmp3[0];
  tmp3[0]=tmp4;

  items2.push({start: tmp2.join('-') , id: tmp, end: tmp3.join('-') , content: i.company, discount: i.data.discount  });
  tmp++;
}

var items3=new vis.DataSet(items2);
console.log(items2);
var timeline = new vis.Timeline(container, items3, options);

});
