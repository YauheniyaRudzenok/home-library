import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { IPage } from '../models/book.model';
import { BookService } from '../services/book.service';
import { ImageService } from '../../../common';

@Component({
    templateUrl:'./books-list.component.html',
    selector: 'books-list',
    styleUrls:['./books-list.component.scss']
})
export class BooksList implements OnInit {
    private readonly StartOffset: number = 0;
    private readonly Count: number = 18;
    private pattern: string;

    constructor(private route: ActivatedRoute, 
        private bookService: BookService,
        public imageService: ImageService) { }

    Page: IPage;

    ngOnInit(): void {
        this.pattern = this.route.snapshot.paramMap.get('pattern');
    }

    loadBooks(event) {
        this.retrieveBooks(event.first, event.rows);
    }

    private retrieveBooks(offset: number, count: number): void {
        const observable = this.pattern
            ? this.bookService.search(this.pattern, offset, count)
            : this.bookService.getBooks(offset, count);

        observable.subscribe((page: IPage) => {
            this.Page = page;
        });
    }
}