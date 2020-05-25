import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {
  BooksList,
  LibraryList,
  ManageLibrary } from './views';


const routes: Routes = [
  { path: '', component: BooksList },
  { path: 'libraries', component: LibraryList },
  { path: 'libraries/manage', component: ManageLibrary }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
