import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import {ButtonModule} from 'primeng/button';
import {ConfirmDialogModule} from 'primeng/confirmdialog';
import {ListboxModule} from 'primeng/listbox';
import {ToastModule} from 'primeng/toast';
import {InputTextModule} from 'primeng/inputtext';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import {
  FileManagerService,
  LibraryService,
  HttpService,
  IndexService
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
    FormsModule,
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    ButtonModule,
    ConfirmDialogModule,
    ListboxModule,
    ToastModule,
    InputTextModule
  ],
  providers: [
    FileManagerService,
    LibraryService,
    HttpService,
    IndexService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
