import { Component } from '@angular/core';
import { HttpService } from '../common';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor(private http: HttpService){}
  
  ngOnInit() {

  }
}
