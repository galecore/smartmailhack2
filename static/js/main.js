// DOM element where the Timeline will be attached
var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : sParameterName[1];
        }
    }
};
var query = getUrlParameter('query');
if (query === undefined){
  query='';
}
console.log(query);
$.getJSON( "filter?query="+query, function( data ) {
  var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : sParameterName[1];
        }
    }
};


var container = document.getElementById('vis');


console.log('dd');
console.log(data);
// Create a DataSet (allows two way data-binding)




// Configuration for the Timeline
var options = {
  template: function (item, element, data) {

return '<div style="background-image: url('+data.picture+'); width:25px; height:25px;background-size: cover; border-radius: 12px;position: relative;top: 5px;margin-right:5px;display:inline-block"></div>' + data.content   + '  <span class="badge badge-danger"> '+ data.discount  + '</snap>'+'';
},
width: '100%',
height: '250px',
locale: 'ru',
min: '2018-01-01',
max:'2018-12-30',
zoomMax: 3500000000,
zoomMin:1000000000


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

  items2.push({start: tmp2.join('-') , id: tmp, end: tmp3.join('-') , content: i.company, discount: i.data.discount, picture: i.picture  });
  tmp++;
}

var items3=new vis.DataSet(items2);
console.log(items2);
var timeline = new vis.Timeline(container, items3, options);
function onSelect (properties) {
  $("html, body").animate({ scrollTop: $('#card'+properties.items).offset().top-250 }, 1000);
}

// add event listener
timeline.on('select', onSelect);
tmp= new Date();
timeline.moveTo(tmp.toISOString());

});
