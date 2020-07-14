import { OnInit, Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { BookService } from '../services/book.service';
import { ImageService, IndexService } from '../../../common';
import { IBook } from '../models/book.model';
import { MenuItem } from 'primeng/api';

@Component({
    templateUrl:'./book-details.component.html',
    selector: 'book-details',
    styleUrls:['./book-details.component.scss']
})
export class BookDetails implements OnInit {
    constructor(private route: ActivatedRoute,
        private bookService: BookService,
        private indexService: IndexService,
        public imageService: ImageService) { }

    Book: IBook;
    commands: MenuItem[];

    ngOnInit(): void {
        this.initializeCommands();
        this.getBook();        
    }

    private getBook(): void {
        const id = +this.route.snapshot.paramMap.get('id');

        this.bookService.getBook(id).subscribe((book: IBook) => {
            this.Book = book;
        });
    }

    private initializeCommands(): void {
        this.commands = [
            { label: 'Update metadata', icon: 'pi pi-refresh', command: () => this.updateMetadata() },
            { label: 'Delete', icon: 'pi pi-trash', command: () => { } }
        ];
    }

    private updateMetadata(): void {
        this.indexService.indexBook(this.Book.id).subscribe(()=>{
            this.getBook();
        });
    }
}