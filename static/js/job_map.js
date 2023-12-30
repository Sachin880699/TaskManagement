function initMap(){
    var circle;
    // Map options
    
    var mapCenter = new google.maps.LatLng( 42.3601, -71.0589);
    var options01 = {
      zoom:14,
      center:mapCenter,
      streetViewControl:false,
      mapTypeControl: false,
    }
    var map01 = new google.maps.Map(document.getElementById('cxj-map'), options01);

    // Create a draggable marker which will later on be binded to a
    // Circle overlay.
    var marker01 = new google.maps.Marker({
      position: mapCenter,
      draggable: true,
      title: 'Drag me!',
    });
    marker01.setMap(map01);

    // Add a Circle overlay to the map.
    circle = new google.maps.Circle({
      strokeColor: "#FF0000",
      strokeOpacity: 0,
      fillColor: "#00467A",
      fillOpacity: 0.35,
      radius: 100 // 5 km
    });
    circle.setMap(map01);

    // Since Circle and Marker both extend MVCObject, you can bind them
    // together using MVCObject's bindTo() method.  Here, we're binding
    // the Circle's center to the Marker's position.
    // http://code.google.com/apis/maps/documentation/v3/reference.html#MVCObject
    circle.bindTo('center', marker01, 'position');


    // 숫자 3자리마다 콤마 찍기
    function numberWithCommas(x) {
      if (x !== null) {
          return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      }
    }


    $("#myslide").slider({
        orientation: "horizontal",
        range: "min",
        max: 1000,
        min: 100,
        value: 100,
        slide: function(event, ui) {
          updateRadius(circle, ui.value);
          $('#range-value').val(ui.value);   
        },
    });
    var rangeValue = toString().$('#myslide').slider('value', 1);
    $('#range-value').val(rangeValue);
        
            
   /* //slider range data tooltip set
    var $handler = $("#myslide .ui-slider-handle");
  
    $handler.append("<b class='amount'><span id='min'>"+numberWithCommas($( "#myslide" ).slider( "value", 0 )));*/
    


    /*//slider range pointer mousedown event
    $handler.on("mousedown",function(e){
        e.preventDefault();
        $(this).children(".amount").fadeIn(300);
    });

    //slider range pointer mouseup event
    $handler.on("mouseup",function(e){
        e.preventDefault();
        $(this).children(".amount").fadeOut(300);
    });*/
    
    function updateRadius(circle, rad) {
        circle.setRadius(rad);
    }
    
    // Register an event listener to fire when the page finishes loading.
    google.maps.event.addDomListener(window, 'load', init);
        

  }
  