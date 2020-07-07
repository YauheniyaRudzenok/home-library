import { NgModule } from '@angular/core';

import { DataViewModule } from 'primeng/dataview';

import { BooksRoutingModule } from './books-routing.module';

import { BooksList } from './list/books-list.component';
import { BookDetails } from './details/book-details.component';
import { BookService } from './services/book.service';
import { ImageService } from '../../common';

@NgModule({
    imports: [
        BooksRoutingModule,
        DataViewModule
    ],
    declarations: [
        BookDetails,
        BooksList
    ],
    providers:[
        BookService,
        ImageService
    ]
})
export class BooksModule { }