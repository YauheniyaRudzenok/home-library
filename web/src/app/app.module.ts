import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import {ButtonModule} from 'primeng/button';
import {ListboxModule} from 'primeng/listbox';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import {
  FileManagerService,
  LibraryService,
  HttpService
} from './common';
import {
  LibraryList,
  ManageLibrary
} from './views'


@NgModule({
  declarations: [
    AppComponent,
    LibraryList,
    ManageLibrary
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    ButtonModule,
    ListboxModule
  ],
  providers: [
    FileManagerService,
    LibraryService,
    HttpService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
