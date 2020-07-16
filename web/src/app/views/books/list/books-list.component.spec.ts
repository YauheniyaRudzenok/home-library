import { TestBed, ComponentFixture } from '@angular/core/testing';
import { ActivatedRoute, ParamMap } from '@angular/router';

import { Observable } from 'rxjs';

import { DataViewModule } from 'primeng/dataview';

import { BooksList } from "./books-list.component"
import { BookService } from '../services/book.service';
import { IPage, IBook } from '../models/book.model';
import { ImageService } from '../../../common';

describe('BooksList', () => {
    const pattern: string = 'cool book';
    const page: IPage = <IPage>{
        count: 2, 
        data: [
            <IBook>{ authors: '', description: '', file: null, goodreads_id: 1, id: 1, title: '' }
        ]
    };

    let fixture: ComponentFixture<BooksList>;
    let component: BooksList;
    let bookService: jasmine.SpyObj<BookService>;
    let paramMap: jasmine.SpyObj<ParamMap> = jasmine.createSpyObj('ParamMap', ['get']);

    beforeEach(() => {
        TestBed.configureTestingModule({
            imports:[
                DataViewModule
            ],
            declarations: [BooksList],
            providers: [
                { provide: BookService, useValue: jasmine.createSpyObj('BookService', ['getBooks', 'search']) },
                { 
                    provide: ActivatedRoute, 
                    useValue: {
                        snapshot: {
                            paramMap: paramMap
                        } 
                    },
                },
                ImageService
            ]
        });

        fixture = TestBed.createComponent(BooksList);
        component = fixture.componentInstance;
        bookService = TestBed.inject(BookService) as jasmine.SpyObj<BookService>;
    });

    describe('ngOnInit', () => {
        it('should get pattern', () => {
            paramMap.get.and.returnValue(pattern);

            component.ngOnInit();

            expect(paramMap.get).toHaveBeenCalledWith('pattern');
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

        it('should search books with offset and count if pattern is specified', () => {
            paramMap.get.and.returnValue(pattern);

            bookService.getBooks.and.returnValue(Observable.create(observer => {
                observer.next(page);
            }));

            bookService.search.and.returnValue(Observable.create(observer => {
                observer.next(page);
            }));

            component.ngOnInit();

            const event = { first: 10, rows: 20};
            component.loadBooks(event);

            expect(bookService.search).toHaveBeenCalledWith(pattern, event.first, event.rows);
        });
    });
});