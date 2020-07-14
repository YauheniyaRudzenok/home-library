import { OnInit, Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

import { MenuItem, ConfirmationService, MessageService } from 'primeng/api';

import { BookService } from '../services/book.service';
import { ImageService, IndexService } from '../../../common';
import { IBook } from '../models/book.model';

@Component({
    templateUrl:'./book-details.component.html',
    selector: 'book-details',
    styleUrls:['./book-details.component.scss']
})
export class BookDetails implements OnInit {
    constructor(private route: ActivatedRoute,
        private bookService: BookService,
        private indexService: IndexService,
        private confirmationService: ConfirmationService,
        private messageService: MessageService,
        private router: Router,
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
            { label: 'Delete', icon: 'pi pi-trash', command: () => this.deleteBook() }
        ];
    }

    private updateMetadata(): void {
        this.indexService.indexBook(this.Book.id).subscribe(()=>{
            this.getBook();
        });
    }

    private deleteBook(): void {
        this.confirmationService.confirm({
            message: 'Are you sure that you want to delete this book file?',
            accept: () => {
                this.bookService.delete(this.Book.id).subscribe(
                    x => null,
                    error => this.messageService.add({severity:'error', summary:'Book was not deleted'}),
                    () => this.router.navigateByUrl('/')
                )
            }
        });
    }
}