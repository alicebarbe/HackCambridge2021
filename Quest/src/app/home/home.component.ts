import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { CommonService } from '../common.service';

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
        Validators.max(maxRadius)
      ]]
    })
  }

  public submit(f: FormGroup) {
    this.form.markAllAsTouched();
    console.log(this.form.controls['location'].value);
    console.log(this.form.controls['radius'].value);
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

          this.form.controls['location'].setValue(pos);
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
