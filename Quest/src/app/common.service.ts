import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CommonService {

  private baseUrl = 'http://localhost:5000/';
  public lat: number = 0;
  public lon: number = 0;
  public plantCollection: string[] = [];


  constructor(private httpClient: HttpClient) { }

  public getPlants(lat: string, lon: string, radius: string) {

    this.httpClient.get(this.baseUrl + '?lat=' + lat + '&lon=' + lon + '&radius=' + radius)
      .subscribe(
        res => {
          const base = Object.values(res)[0];
          for (let i = 0; i < Object.keys(base).length; i++) {
            let lat = (base[i]).lat;
            let lon = (base[i]).long;
            this.plantCollection.push('lat' + '/' + 'lon')
          }
          console.log(this.plantCollection)
        },
        err => console.log(err)
      )
  }

  public getPlantCollection() {
    return (this.plantCollection);
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
