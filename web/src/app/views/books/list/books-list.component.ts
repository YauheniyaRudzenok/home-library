import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { IPage } from '../models/book.model';
import { BookService } from '../services/book.service';
import { ImageService } from '../../../common';

@Component({
    templateUrl:'./books-list.component.html',
    selector: 'books-list',
    styleUrls:['./books-list.component.scss']
})
export class BooksList implements OnInit {
    constructor(private router: Router, 
        private bookService: BookService,
        public imageService: ImageService) { }

    Page: IPage;

    ngOnInit(): void {
         this.bookService.getBooks(0, 18).subscribe((page: IPage) => {
            if(page?.data.length > 0) {
                this.Page = page;
            } else {
                this.router.navigateByUrl('/libraries/manage');
            }
        });
    }

    loadBooks(event) {
        this.bookService.getBooks(event.first, event.rows).subscribe((page: IPage) => {
            this.Page = page;
        });
    }
}