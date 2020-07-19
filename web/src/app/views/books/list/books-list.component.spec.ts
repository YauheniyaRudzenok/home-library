import { TestBed, ComponentFixture } from '@angular/core/testing';
import { ActivatedRoute, ParamMap } from '@angular/router';

import { Observable } from 'rxjs';

import { DataViewModule } from 'primeng/dataview';

import { BooksList } from "./books-list.component"
import { BookService } from '../services/book.service';
import { IPage, IBook } from '../models/book.model';
import { ImageService, SessionStorage } from '../../../common';
import { Constants } from '../../../constants';

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
    let sessionStorage: jasmine.SpyObj<SessionStorage>;
    let paramMap: jasmine.SpyObj<ParamMap> = jasmine.createSpyObj('ParamMap', ['get']);

    beforeEach(() => {
        TestBed.configureTestingModule({
            imports:[
                DataViewModule
            ],
            declarations: [BooksList],
            providers: [
                { provide: BookService, useValue: jasmine.createSpyObj('BookService', ['getBooks', 'search']) },
                { provide: SessionStorage, useValue: jasmine.createSpyObj('SessionStorage', ['getItem', 'setItem'])},
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
        sessionStorage = TestBed.inject(SessionStorage) as jasmine.SpyObj<SessionStorage>;
    });

    describe('ngOnInit', () => {
        beforeEach(()=> {
            paramMap.get.and.returnValue(pattern);
        });

        it('should get pattern', () => {
            component.ngOnInit();

            expect(paramMap.get).toHaveBeenCalledWith('pattern');
        });

        it('should set offset when it exists in session', () => {
            const testOffset: number = 10;

            sessionStorage.getItem.and.returnValue(testOffset.toString());

            component.ngOnInit();

            expect(component.Offset).toEqual(testOffset);
            expect(sessionStorage.getItem).toHaveBeenCalledWith(Constants.OffsetKey);
        });

        it('should set offset to 0 when it doesnot exists in session', () => {
            sessionStorage.getItem.and.returnValue(null);

            component.ngOnInit();

            expect(component.Offset).toEqual(0);
            expect(sessionStorage.getItem).toHaveBeenCalledWith(Constants.OffsetKey);
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
            expect(sessionStorage.setItem).toHaveBeenCalledWith(Constants.OffsetKey, event.first as any);
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