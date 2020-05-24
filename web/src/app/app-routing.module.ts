import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {
  BooksList,
  ManageLibrary } from './views';


const routes: Routes = [
  { path: '', component: BooksList },
  { path: 'manage-library', component: ManageLibrary }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
