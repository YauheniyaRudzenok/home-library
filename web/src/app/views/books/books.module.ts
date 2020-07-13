import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from "@angular/common";

import { ButtonModule } from 'primeng/button';
import { DataViewModule } from 'primeng/dataview';
import { InputTextModule } from 'primeng/inputtext';
import { EditorModule } from 'primeng/editor';

import { BooksRoutingModule } from './books-routing.module';

import { BooksList } from './list/books-list.component';
import { BookDetails } from './details/book-details.component';
import { BookEdit } from './edit/book-edit.component';
import { BookService } from './services/book.service';
import { ImageService } from '../../common';

@NgModule({
    imports: [
        FormsModule,
        CommonModule,
        ButtonModule,
        BooksRoutingModule,
        DataViewModule,
        InputTextModule,
        EditorModule
    ],
    declarations: [
        BookDetails,
        BookEdit,
        BooksList
    ],
    providers:[
        BookService,
        ImageService
    ]
})
export class BooksModule { }