import { AfterViewInit, Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { CommonService } from '../common.service';

@Component({
  selector: 'app-routeview',
  templateUrl: './routeview.component.html',
  styleUrls: ['./routeview.component.less']
})
export class RouteviewComponent implements AfterViewInit {

  constructor(private service: CommonService) { }

  @ViewChild('mapContainer', {static: false}) gmap: ElementRef | undefined;
  map!: google.maps.Map;
  lat = this.service.getLat();
  log = this.service.getLon();
  coordinates = new google.maps.LatLng(this.lat, this.log);
  
  mapOptions: google.maps.MapOptions = {
    center: this.coordinates,
    zoom: 15
  }

  origin = new google.maps.Marker({
    position: this.coordinates,
    map: this.map,
  });
  
  ngAfterViewInit(): void {
    this.mapInitializer();
  }

  mapInitializer() {
    this.map = new google.maps.Map(this.gmap?.nativeElement, 
    this.mapOptions);
    this.origin.setMap(this.map);

    const plants = this.service.getPlantCollection()
    plants.forEach(plant => {
      let splitCoords = plant.split('/');
      let lat = parseInt(splitCoords[0]);
      let lon = parseInt(splitCoords[1]);
      let coordinates = new google.maps.LatLng(lat, lon)
      new google.maps.Marker({
        position: (coordinates),
        map: this.map
      })
    })

  }

}
