import { ActivatedRoute } from '@angular/router';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { NoopAnimationsModule } from '@angular/platform-browser/animations';

import { SplitButtonModule } from 'primeng/splitbutton';

import { Observable } from 'rxjs';

import { BookDetails } from "./book-details.component";
import { BookService } from '../services/book.service';
import { ImageService, IndexService } from '../../../common';
import { IBook } from '../models/book.model';
import { By } from '@angular/platform-browser';

describe('BookDetails', () => {
    const id: number = 15;
    const book: IBook = { 
        authors: '', 
        description: '', 
        file: { image: '', file_name: '', full_path: '', id: 1, library_id:1, path:'' },
        goodreads_id: 1, 
        id: id, 
        title: '' 
    };

    let fixture: ComponentFixture<BookDetails>;
    let component: BookDetails;
    let bookService: jasmine.SpyObj<BookService>;
    let route: jasmine.SpyObj<ActivatedRoute>;
    let indexService: jasmine.SpyObj<IndexService>;

    beforeEach(() => {
        TestBed.configureTestingModule({
            imports:[
                SplitButtonModule,
                RouterTestingModule,
                NoopAnimationsModule
            ],
            declarations: [BookDetails],
            providers: [
                { provide: BookService, useValue: jasmine.createSpyObj('BookService', ['getBook']) },
                { provide: IndexService, useValue: jasmine.createSpyObj('IndexService', ['indexBook'])},
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
        indexService = TestBed.inject(IndexService) as jasmine.SpyObj<IndexService>;
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

    describe('updateMetadata', () => {
        it('should update metadata and get new book information', () => {
            const updatedBook: IBook = { 
                authors: 'Author, Name', 
                description: '', 
                file: { image: '', file_name: '', full_path: '', id: 1, library_id:1, path:'' }, 
                goodreads_id: 1, 
                id: id, 
                title: 'Updated book' 
            };

            bookService.getBook.and.returnValue(Observable.create(observer => {
                observer.next(updatedBook);
            }));

            indexService.indexBook.and.returnValue(Observable.create(observer => {
                observer.next();
            }));
            
            component.Book = book;

            fixture.detectChanges();

            const dropDownEl = fixture.debugElement.query(By.css('.ui-splitbutton-menubutton')).nativeElement;
            dropDownEl.click();
            fixture.detectChanges();

            const menuEl = fixture.debugElement.query(By.css('.ui-menuitem')).children[0].nativeElement;
            menuEl.click();
            fixture.detectChanges();

            expect(component.Book).toEqual(updatedBook);
            expect(bookService.getBook).toHaveBeenCalledWith(id);
            expect(indexService.indexBook).toHaveBeenCalledWith(id);
        });
    });
});