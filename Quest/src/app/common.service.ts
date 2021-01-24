import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CommonService {

  private baseUrl = 'http://localhost:5000/';
  public lat: number = 0;
  public lon: number = 0;


  constructor(private httpClient: HttpClient) { }

  public getPlants(lat: string, lon: string, radius: string) {

    this.httpClient.get(this.baseUrl + '?lat=' + lat + '&lon=' + lon + '&radius=' + radius)
      .subscribe(
        res => console.log(res),
        err => console.log(err)
      )
  }

  public setLat(lat: number) {
    this.lat = lat;
  }

  public setLon(lon: number) {
    this.lon = lon;
  }

  public getLat() {
    return this.lat;
  }

  public getLon() {
    return this.lon;
  }
}
