import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import {
  LibraryService,
  HttpService
} from './common';
import {
  ManageLibrary
} from './views'


@NgModule({
  declarations: [
    AppComponent,
    ManageLibrary
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule
  ],
  providers: [
    LibraryService,
    HttpService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
