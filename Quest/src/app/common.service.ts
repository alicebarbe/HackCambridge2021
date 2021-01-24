import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CommonService {

  private baseUrl = 'http://127.0.0.1:5000';
  private params = new HttpParams();

  constructor(private httpClient: HttpClient) { }

  public getPlants(lat: string, lon: string, radius: string) {
    this.params.set('lat', lat);
    this.params.set('lot', lon);
    this.params.set('radius', radius)

    this.httpClient.get(this.baseUrl, {
      params: this.params
    });
  }
}
