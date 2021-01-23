import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.less']
})
export class HomeComponent implements OnInit {

  public form: FormGroup;

  constructor(private fb: FormBuilder) {
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
    console.log(this.form.get('location'));
    console.log(this.form.get('radius'));
  }

  ngOnInit(): void {
  }

}
