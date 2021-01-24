import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { CommonService } from '../common.service';

const PostcodesIO = require('postcodesio-client');

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.less']
})
export class HomeComponent implements OnInit {

  public form: FormGroup;
  public geolocationError = false;

  constructor(
    private fb: FormBuilder,
    private router: Router,
    private service: CommonService
    ) {
    const minRadius = 0.5;
    const maxRadius = 20;
    this.form = this.fb.group({
      location: ['', [
        Validators.required,
        Validators.pattern('^(([A-Z][0-9]{1,2})|(([A-Z][A-HJ-Y][0-9]{1,2})|(([A-Z][0-9][A-Z])|([A-Z][A-HJ-Y][0-9]?[A-Z])))) [0-9][A-Z]{2}$')
      ]],
      radius: ['', [
        Validators.required,
        Validators.min(minRadius),
        Validators.max(maxRadius),
        Validators.pattern('^[0-9]+$')
      ]]
    })
  }

  public submit(f: FormGroup) {

    const postcodes = new PostcodesIO('https://api.postcodes.io');
    postcodes
      .lookupPostcode(this.controls.location.value, {})
      .then((data: any) => {
        this.service.setLat(data.latitude);
        this.service.setLon(data.longitude);
        this.service.getPlants(data.latitude, data.longitude, this.controls.radius.value);
      });

    this.form.markAllAsTouched();
    setTimeout(() => this.goToRouteView(), 60000);
  }

  get controls() {
    return this.form.controls;
  }

  public getMyLocation() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
          };

		  console.log( `Current Latitude is ${pos.lat}, longitude is ${pos.lng}`);
		  
		  //const a = fetch(`https://api.postcodes.io/postcodes?lon=${pos.lng}&lat=${pos.lat}`).then(function(response) {
		//	return response.json();
		// }).then(function(data) {
		//	return data.result[0].postcode;
		//  });
		//  console.log(a);

        //  this.form.controls['location'].setValue(Object.values(a)[1]);
		  this.form.controls['location'].setValue(`${pos.lng}, ${pos.lat}`)
          this.form.controls['location'].setErrors({'incorrect': true})
        },
        () => this.geolocationError = true
      );
    } else {
      this.geolocationError = true
    }
  }

  goToRouteView() {
    this.router.navigate(['/routeview'])
  }


  ngOnInit(): void {
  }

}