function initMap(){
    
    
       


    
    // zoom option 
    var options = {
      zoom:7,
      center:{lat:42.3601,lng:-71.0589},
    
      styles: [
        {
            "featureType": "administrative",
            "elementType": "geometry.fill",
            "stylers": [
                {
                    "color": "#d6e2e6"
                }
            ]
        },
        {
          "featureType": "administrative",
          "elementType": "geometry.stroke",
          "stylers": [
              {
                  "color": "#cfd4d5"
              }
          ]
      },
      {
          "featureType": "administrative",
          "elementType": "labels.text.fill",
          "stylers": [
              {
                  "color": "#7492a8"
              }
          ]
      },
      {
          "featureType": "administrative.neighborhood",
          "elementType": "labels.text.fill",
          "stylers": [
              {
                  "lightness": 25
              }
          ]
      },
      {
          "featureType": "landscape.man_made",
          "elementType": "geometry.fill",
          "stylers": [
              {
                  "color": "#dde2e3"
              }
          ]
      },
      {
          "featureType": "landscape.man_made",
          "elementType": "geometry.stroke",
          "stylers": [
              {
                  "color": "#cfd4d5"
              }
          ]
      },
      {
          "featureType": "landscape.natural",
          "elementType": "geometry.fill",
          "stylers": [
              {
                  "color": "#dde2e3"
              }
          ]
      },
      {
          "featureType": "landscape.natural",
          "elementType": "labels.text.fill",
          "stylers": [
              {
                  "color": "#7492a8"
              }
          ]
      },
      {
          "featureType": "landscape.natural.terrain",
          "elementType": "all",
          "stylers": [
              {
                  "visibility": "off"
              }
          ]
      },
      {
          "featureType": "poi",
          "elementType": "geometry.fill",
          "stylers": [
              {
                  "color": "#dde2e3"
              }
          ]
      },
      {
          "featureType": "poi",
          "elementType": "labels.text.fill",
          "stylers": [
              {
                  "color": "#588ca4"
              }
          ]
      },
      {
          "featureType": "poi",
          "elementType": "labels.icon",
          "stylers": [
              {
                  "saturation": -100
              }
          ]
      },
      {
        "featureType": "poi.park",
        "elementType": "geometry.fill",
        "stylers": [
            {
                "color": "#a9de83"
            }
        ]
    },
    {
        "featureType": "poi.park",
        "elementType": "geometry.stroke",
        "stylers": [
            {
                "color": "#bae6a1"
            }
        ]
    },
    {
        "featureType": "poi.sports_complex",
        "elementType": "geometry.fill",
        "stylers": [
            {
                "color": "#c6e8b3"
            }
        ]
    },
    {
        "featureType": "poi.sports_complex",
        "elementType": "geometry.stroke",
        "stylers": [
            {
                "color": "#bae6a1"
            }
        ]
    },
    {
        "featureType": "road",
        "elementType": "labels.text.fill",
        "stylers": [
            {
                "color": "#41626b"
            }
        ]
    },
    {
        "featureType": "road",
        "elementType": "labels.icon",
        "stylers": [
            {
                "saturation": -45
            },
            {
                "lightness": 10
            },
            {
                "visibility": "on"
            }
        ]
    },
    {
        "featureType": "road.highway",
        "elementType": "geometry.fill",
        "stylers": [
            {
                "color": "#c1d1d6"
            }
        ]
    },
    {
        "featureType": "road.highway",
        "elementType": "geometry.stroke",
        "stylers": [
            {
                "color": "#a6b5bb"
            }
        ]
    },
    {
        "featureType": "road.highway",
        "elementType": "labels.icon",
        "stylers": [
            {
                "visibility": "on"
            }
        ]
    },
    {
        "featureType": "road.highway.controlled_access",
        "elementType": "geometry.fill",
        "stylers": [
            {
                "color": "#9fb6bd"
            }
        ]
    },
    {
        "featureType": "road.arterial",
        "elementType": "geometry.fill",
        "stylers": [
            {
                "color": "#ffffff"
            }
        ]
    },
    {
        "featureType": "road.local",
        "elementType": "geometry.fill",
        "stylers": [
            {
                "color": "#ffffff"
            }
        ]
    },
    {
        "featureType": "transit",
        "elementType": "labels.icon",
        "stylers": [
            {
                "saturation": -70
            }
        ]
    },
    {
        "featureType": "transit.line",
        "elementType": "geometry.fill",
        "stylers": [
            {
                "color": "#b4cbd4"
            }
        ]
    },
    {
        "featureType": "transit.line",
        "elementType": "labels.text.fill",
        "stylers": [
            {
                "color": "#588ca4"
            }
        ]
    },
    {
        "featureType": "transit.station",
        "elementType": "all",
        "stylers": [
            {
                "visibility": "off"
            }
        ]
    },
    {
      "featureType": "transit.station",
      "elementType": "labels.text.fill",
      "stylers": [
          {
              "color": "#008cb5"
          },
          {
              "visibility": "on"
          }
      ]
  },
  {
      "featureType": "transit.station.airport",
      "elementType": "geometry.fill",
      "stylers": [
          {
              "saturation": -100
          },
          {
              "lightness": -5
          }
      ]
  },
  {
      "featureType": "water",
      "elementType": "geometry.fill",
      "stylers": [
          {
              "color": "#a6cbe3"
          }
      ]
  }
      ]
    }





    // New map
    var map = new google.maps.Map(document.getElementById('map'), options);
   











    
    
            
          
            
         
       




        //   marker
    var iconBase = 'images/';

    const contentString = '<div id="content" style="width:225px;height:150px;border-radius:15px;">' + 
                                '<div id="siteNotice">' +
                                  '<div class="top-content" style="border-bottom:1px solid #e7e7e7;position:relative;padding-bottom:20px;">'+
                                    '<span style="position:absolute;top:0;left:0;">'+
                                      '<img src="images/location-5.png" class="img-fluid">'+
                                    '</span>'+
                                    '<span>'+
                                      '<h4 style=" margin:0; margin-left:55px; padding-top:2px; color:#0A1724; font-size:14px; font-family:"robotoregular"; letter-spacing:1.5px;>'+ 'Patient Name' + '</h4>'+
                                      '<p style=" margin-left:55px; padding-top:7px;margin-bottom:0;color:#000; font-size:13px; font-family:"robotoregular"; letter-spacing:1.5px;>'+ 'Gangubai Kathiawadi' + '</h4>'+
                                    '</span>'+
                                  '</div>'+
                                  '<div class="bottom-content">'+
                                    '<div style="">'+
                                        '<h4 style="color:#0A1724; margin-top:15px; display:inline-block; font-size:14px; letter-spacing:1.5px; font-family:"robotoregular";" >'+ 'Age' + '</h4>'+
                                        '<p style=" display:inline-block; margin-left:12px; margin-bottom:10px;color:#000; font-size:13px; font-family:"robotomedium"; font-weight:700; letter-spacing:1.5px;>'+ '24 years' + '</h4>'+
                                    '</div>'+
                                    '<div>'+
                                        '<h4 style="color:#0A1724; display:inline-block; font-size:14px; letter-spacing:1.5px; font-family:"robotoregular";" >'+ 'Name Of Diseases' + '</h4>'+
                                        '<p style=" display:inline-block; margin-left:12px; margin-bottom:5px;color:#000; font-size:13px; font-family:"robotomedium"; font-weight:700; letter-spacing:1.5px;>'+ 'cancer' + '</h4>'+
                                    '</div>'+
                                   
                                  '</div>'+
                                '</div>' +
                              '</div>';

    
    
    
    // Array of markers
    var markers = [
      {
        coords:{lat:42.4668,lng:-70.9495},
        iconImage:iconBase + 'tb.png',
        content:contentString
      },
      {
        coords:{lat:42.8584,lng:-70.9300},
        iconImage:iconBase + 'Heart-Disease.png',
        content:contentString
      },
      {
        coords:{lat:42.757870,lng:-71.463951},
        iconImage:iconBase + 'tb.png',
        content:contentString
      },
      {
        coords:{lat:42.333672,lng:-71.120880},
        iconImage:iconBase + 'Cancer.png',
        content:contentString
      },
      {
        coords:{lat:42.845871,lng:-72.563019},
        iconImage:iconBase + 'Cancer.png',
        content:contentString
      },
      {
        coords:{lat:42.275871,lng:-72.433019},
        iconImage:iconBase + 'Kidney-Disease.png',
        content:contentString
      },
      {
        coords:{lat:43.275871,lng:-72.433019},
        iconImage:iconBase + 'Diabetes.png',
        content:contentString
      },
      {
        coords:{lat:42.275871,lng:-71.433019},
        iconImage:iconBase + 'Diabetes.png',
        content:contentString
      },
      {
        coords:{lat:41.275871,lng:-71.859019},
        iconImage:iconBase + 'Hypertension.png',
        content:contentString
      },
      {
        coords:{lat:42.258871,lng:-72.433019},
        iconImage:iconBase + 'Hypertension.png',
        content:contentString
      },
      {
        coords:{lat:42.815321,lng:-72.215019},
        iconImage:iconBase + 'Kidney-Disease.png',
        content:contentString
      },
      {
        coords:{lat:42.262592,lng:-71.802292},
        iconImage:iconBase + 'Asthma.png',
        content:contentString
      },
      {
        coords:{lat:42.325089,lng:-72.641197},
        iconImage:iconBase + 'Asthma.png',
        content:contentString
      },
    ];

    // Loop through markers
    for(var i = 0;i < markers.length;i++){
      // Add marker
      addMarker(markers[i]);
    }

    // Add Marker Function
    function addMarker(props){
      var marker = new google.maps.Marker({
        position:props.coords,
        map:map,
        visible: true
        //icon:props.iconImage
      });

      // Check for customicon
      if(props.iconImage){
        // Set icon image
        marker.setIcon(props.iconImage);
      }

      // Check content
      if(props.content){
        
        var infoWindow = new google.maps.InfoWindow({
          content:props.content
        });

        marker.addListener('click', function(){
          infoWindow.open(map, marker);
        });
      }
    }


// marker end



  }
  