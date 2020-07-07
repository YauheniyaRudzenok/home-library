import { ActivatedRoute } from '@angular/router';
import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Observable } from 'rxjs';

import { BookDetails } from "./book-details.component";
import { BookService } from '../services/book.service';
import { ImageService } from '../../../common';
import { IBook } from '../models/book.model';

describe('BookDetails', () => {
    const id: number = 15;
    const book: IBook = { 
        authors: '', 
        description: '', 
        file: null, 
        goodreads_id: 1, 
        id: id, 
        title: '' 
    };

    let fixture: ComponentFixture<BookDetails>;
    let component: BookDetails;
    let bookService: jasmine.SpyObj<BookService>;
    let route: jasmine.SpyObj<ActivatedRoute>;

    beforeEach(() => {
        TestBed.configureTestingModule({
            declarations: [BookDetails],
            providers: [
                { provide: BookService, useValue: jasmine.createSpyObj('BookService', ['getBook']) },
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

        fixture = TestBed.createComponent(BookDetails);
        component = fixture.componentInstance;
        bookService = TestBed.inject(BookService) as jasmine.SpyObj<BookService>;
        route = TestBed.inject(ActivatedRoute) as jasmine.SpyObj<ActivatedRoute>;
    });

    describe('ngOnInit', () => {
        it('should load book', () => {
            bookService.getBook.and.returnValue(Observable.create(observer => {
                observer.next(book);
            }));

            component.ngOnInit();

            expect(component.Book).toEqual(book);
            expect(bookService.getBook).toHaveBeenCalledWith(id);
        });
    });
});