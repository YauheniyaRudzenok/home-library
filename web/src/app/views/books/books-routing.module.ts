import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { BooksList } from './list/books-list.component';
import { BookDetails } from './details/book-details.component';
import { BookEdit } from './edit/book-edit.component';

const routes: Routes = [
  { path: '', component: BooksList },
  { path: 'books/:id', component: BookDetails },
  { path: 'books/:id/edit', component: BookEdit }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class BooksRoutingModule { }