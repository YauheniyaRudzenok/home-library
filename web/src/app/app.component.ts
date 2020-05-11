import { Component } from '@angular/core';
import { HttpService } from '../common';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor(private http: HttpService){}
  
  ItemsArray= [];
  Hello = "app"

  ngOnInit() {
    this.getFiles().subscribe((res: any) => {
      this.ItemsArray = res;
    });
  }

  getFiles(): Observable<any[]> {
    return this.http.get<any>("/file");
  }

  getHello(): Observable<string> {
    return this.http.get<string>("/");
  }
}
