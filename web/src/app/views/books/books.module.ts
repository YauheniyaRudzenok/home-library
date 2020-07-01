import { NgModule } from '@angular/core';

import { DataViewModule } from 'primeng/dataview';

import { BooksRoutingModule } from './books-routing.module';

import { BooksList } from './list/books-list.component';
import { BookService } from './services/book.service';
import { ImageService } from '../../common';

@NgModule({
    imports: [
        BooksRoutingModule,
        DataViewModule
    ],
    declarations: [
        BooksList
    ],
    providers:[
        BookService,
        ImageService
    ]
})
export class BooksModule { }