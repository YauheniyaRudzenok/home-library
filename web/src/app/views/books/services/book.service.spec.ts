import { TestBed } from '@angular/core/testing';

import { BookService } from "./book.service";
import { HttpService } from '../../../common';
import { IBook, IPage } from '../models/book.model';
import { Observable } from 'rxjs';

describe('BookService', () => {
    const book: IBook = { 
        authors:'',
        description:'',
        file:null,
        goodreads_id:0,
        id:1,
        title:''
    };

    let service: BookService;
    let httpService: jasmine.SpyObj<HttpService>;

    beforeEach(() => {
        var spy = jasmine.createSpyObj('HttpService', ['get']);

        TestBed.configureTestingModule({
            providers: [
                BookService,
                { provide: HttpService, useValue: spy }
            ]
        });

        service = TestBed.inject(BookService);
        httpService = TestBed.inject(HttpService) as jasmine.SpyObj<HttpService>;
    })

    it('should get books', () => {
        const offset: number = 10;
        const count: number = 20;
        const page: IPage = { count:10, data: [book] };

        httpService.get.and.returnValue(Observable.create(observer => {
            observer.next(page);
        }));

        service.getBooks(offset, count).subscribe(result => {
            expect(result).toEqual(page);

            expect(httpService.get).toHaveBeenCalledWith(`/books/${offset}/${count}`);
        });
    });

    it('should get book', () => {
        const id: number = 12;

        httpService.get.and.returnValue(Observable.create(observer => {
            observer.next(book);
        }));

        service.getBook(id).subscribe(result => {
            expect(result).toEqual(book);

            expect(httpService.get).toHaveBeenCalledWith(`/books/${id}`);
        });
    });
});