import { ActivatedRoute, Router } from '@angular/router';
import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Observable } from 'rxjs';

import { BookService } from '../services/book.service';
import { ImageService } from '../../../common';
import { IBook } from '../models/book.model';
import { BookEdit } from './book-edit.component';

describe('BookEdit', () => {
    const id: number = 15;
    const book: IBook = { 
        authors: '', 
        description: '', 
        file: null, 
        goodreads_id: 1, 
        id: id, 
        title: '' 
    };

    let fixture: ComponentFixture<BookEdit>;
    let component: BookEdit;
    let bookService: jasmine.SpyObj<BookService>;
    let route: jasmine.SpyObj<ActivatedRoute>;
    let router: jasmine.SpyObj<Router>;

    beforeEach(() => {
        TestBed.configureTestingModule({
            declarations: [BookEdit],
            providers: [
                { provide: BookService, useValue: jasmine.createSpyObj('BookService', ['getBook', 'update']) },
                { provide: Router, useValue: jasmine.createSpyObj('Router', ['navigateByUrl']) },
                { 
                    provide: ActivatedRoute, 
                    useValue: {
                        snapshot: {
                            paramMap: {
                                get: () => { return id; }
                            }
                        } 
                    },
                },
                ImageService
            ]
        });

        fixture = TestBed.createComponent(BookEdit);
        component = fixture.componentInstance;
        bookService = TestBed.inject(BookService) as jasmine.SpyObj<BookService>;
        route = TestBed.inject(ActivatedRoute) as jasmine.SpyObj<ActivatedRoute>;
        router = TestBed.inject(Router) as jasmine.SpyObj<Router>;
    });

    describe('ngOnInit', () => {
        it('should load book', () => {
            bookService.getBook.and.returnValue(Observable.create(observer => {
                observer.next(book);
            }));

            component.ngOnInit();

            expect(component.book).toEqual(book);
            expect(bookService.getBook).toHaveBeenCalledWith(id);
        });
    });

    describe('save', () => {
        it('should update book and redirect', () => {
            bookService.update.and.returnValue(Observable.create(observer => {
                observer.next();
                observer.complete();
            }));

            component.book = book;
            component.save();

            expect(bookService.update).toHaveBeenCalledWith(book);
            expect(router.navigateByUrl).toHaveBeenCalledWith(`/books/${book.id}`)
        });
    });
});