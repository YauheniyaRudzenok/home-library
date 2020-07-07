import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { BooksList } from './list/books-list.component';
import { BookDetails } from './details/book-details.component';

const routes: Routes = [
  { path: '', component: BooksList },
  { path: 'books/:id', component: BookDetails }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class BooksRoutingModule { }