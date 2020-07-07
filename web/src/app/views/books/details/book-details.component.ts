import { OnInit, Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { BookService } from '../services/book.service';
import { ImageService } from '../../../common';
import { IBook } from '../models/book.model';

@Component({
    templateUrl:'./book-details.component.html',
    selector: 'book-details',
    styleUrls:['./book-details.component.scss']
})
export class BookDetails implements OnInit {
    constructor(private route: ActivatedRoute,
        private bookService: BookService,
        public imageService: ImageService) { }

    Book: IBook;

    ngOnInit(): void {
        const id = +this.route.snapshot.paramMap.get('id');

        this.bookService.getBook(id).subscribe((book: IBook) => {
            this.Book = book;
        });
    }
}