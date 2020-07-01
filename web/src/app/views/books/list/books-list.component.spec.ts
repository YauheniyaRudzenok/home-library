import { TestBed, ComponentFixture } from '@angular/core/testing';
import { Router } from '@angular/router';

import { Observable } from 'rxjs';

import { DataViewModule } from 'primeng/dataview';

import { BooksList } from "./books-list.component"
import { BookService } from '../services/book.service';
import { IPage, IBook } from '../models/book.model';
import { ImageService } from '../../../common';

describe('BooksList', () => {
    const page: IPage = <IPage>{
        count: 2, 
        data: [
            <IBook>{ authors: '', description: '', file: null, goodreads_id: 1, id: 1, title: '' }
        ]
    };

    let fixture: ComponentFixture<BooksList>;
    let component: BooksList;
    let bookService: jasmine.SpyObj<BookService>;
    let router: jasmine.SpyObj<Router>;

    beforeEach(() => {
        TestBed.configureTestingModule({
            imports:[
                DataViewModule
            ],
            declarations: [BooksList],
            providers: [
                { provide: BookService, useValue: jasmine.createSpyObj('BookService', ['getBooks']) },
                { provide: Router, useValue: jasmine.createSpyObj('Router', ['navigateByUrl']) },
                ImageService
            ]
        });

        fixture = TestBed.createComponent(BooksList);
        component = fixture.componentInstance;
        bookService = TestBed.inject(BookService) as jasmine.SpyObj<BookService>;
        router = TestBed.inject(Router) as jasmine.SpyObj<Router>;
    });

    describe('ngOnInit', () => {
        it('should navigate to the manage library route when there are not books', () => {
            bookService.getBooks.and.returnValue(Observable.create(observer => {
                observer.next();
            }));

            component.ngOnInit();

            expect(router.navigateByUrl).toHaveBeenCalledWith('/libraries/manage');
        });

        it('should load books', () => {
            bookService.getBooks.and.returnValue(Observable.create(observer => {
                observer.next(page);
            }));

            component.ngOnInit();

            expect(component.Page).toEqual(page)
            expect(bookService.getBooks).toHaveBeenCalledWith(0, 18);
        });
    });

    describe('loadBooks', () => {
        it('should load books with offset and count specified', () => {
            bookService.getBooks.and.returnValue(Observable.create(observer => {
                observer.next(page);
            }));

            const event = { first: 10, rows: 20};
            component.loadBooks(event);

            expect(component.Page).toEqual(page)
            expect(bookService.getBooks).toHaveBeenCalledWith(event.first, event.rows);
        });
    });
});