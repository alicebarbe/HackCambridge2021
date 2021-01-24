import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CommonService {

  private baseUrl = 'localhost:5000';
  //private params = new HttpParams();

  constructor(private httpClient: HttpClient) { }

  public getPlants(lat: string, lon: string, radius: string) {

    this.httpClient.get(this.baseUrl + '?lat=' + lat + '&lon=' + lon + '&radius=' + radius);
  }
}
