function cargarMapa() {
    var wwd = new WorldWind.WorldWindow("canvasOne");

    wwd.addLayer(new WorldWind.BMNGOneImageLayer());
    wwd.addLayer(new WorldWind.BMNGLandsatLayer());
    
    wwd.addLayer(new WorldWind.CompassLayer());
    wwd.addLayer(new WorldWind.CoordinatesDisplayLayer(wwd));
    wwd.addLayer(new WorldWind.ViewControlsLayer(wwd));
    
    var markerLayer = new WorldWind.RenderableLayer("Markers");
    
    var placemarkAttributes = new WorldWind.PlacemarkAttributes(null);
    placemarkAttributes.imageSource = "/static/images/fire.svg";
    placemarkAttributes.imageScale = 0.25;
    
    var latitude = 40.4168;
    var longitude = -3.7038;
    var position = new WorldWind.Position(latitude, longitude, 1000);
    var placemark = new WorldWind.Placemark(position, false, placemarkAttributes);
    markerLayer.addRenderable(placemark);
    
    
    var parisLatitude = 48.8566; // Latitud de París, Francia
    var parisLongitude = 2.3522; // Longitud de París, Francia
    var parisPosition = new WorldWind.Position(parisLatitude, parisLongitude, 1000);
    
    // Crea el marcador en la ubicación de París
    var parisPlacemark = new WorldWind.Placemark(parisPosition, false, placemarkAttributes);
    
    // Agrega el marcador de París al RenderableLayer
    markerLayer.addRenderable(parisPlacemark);

    
    setTimeout(function () {
        var germanyLatitude = 51.1657;
        var germanyLongitude = 10.4515;
        var germanyPosition = new WorldWind.Position(germanyLatitude, germanyLongitude, 1000);
        var germanyPlacemark = new WorldWind.Placemark(germanyPosition, false, placemarkAttributes);
        markerLayer.addRenderable(germanyPlacemark);
    }, 5000);

    wwd.addLayer(markerLayer);

}

document.addEventListener("DOMContentLoaded", function () {
    const button = document.querySelector('.botonPrincipal');
    const logo = document.querySelector('.logoInicio');
    const loadingModal = document.getElementById('loadingModal');
    const canvas = document.getElementById('canvasOne');

    $(loadingModal).modal({
        backdrop: 'static',
        keyboard: false
    });

    button.addEventListener('click', function () {
        button.style.display = 'none';
        logo.style.opacity = '0';
        logo.classList.add('moving-logo');

        setTimeout(function () {
            var myCard = document.getElementById('myCard');
            $("#myCard").removeClass("mshide");
            myCard.addEventListener('click', function () {
                myCard.style.display = 'none'; // Oculta la tarjeta al hacer clic en ella
            });
        }, 7000);

        setTimeout(function () {
            logo.src = '/static/images/4everforest2.svg'
            logo.style.opacity = '1';
        }, 500);

        setTimeout(function () {
            logo.classList.remove('moving-logo');
            logo.classList.add('moving-logo');
        }, 1000);

        setTimeout(function () {
            $(loadingModal).modal('hide');
            $("#canvasOne").removeClass('mshide');
            cargarMapa();
        }, 2000);

        document.body.classList.toggle('white_background'); // Cambia la clase del cuerpo
    });
});