import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { BooksList } from './list/books-list.component';

const routes: Routes = [
  { path: '', component: BooksList }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class BooksRoutingModule { }