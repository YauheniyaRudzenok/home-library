import { TestBed } from '@angular/core/testing';
import { Router } from '@angular/router';

import { Observable } from 'rxjs';

import { BooksList } from "./books-list.component"
import { LibraryService } from '../../common';
import { ILibrary } from '../../models';

describe('BooksList', () => {
    let component: BooksList;
    let libraryService: jasmine.SpyObj<LibraryService>;
    let router: jasmine.SpyObj<Router>;

    beforeEach(() => {
        TestBed.configureTestingModule({
            declarations: [BooksList],
            providers: [
                { provide: LibraryService, useValue: jasmine.createSpyObj('LibraryService', ['getLibraries']) },
                { provide: Router, useValue: jasmine.createSpyObj('Router', ['navigateByUrl']) }
            ]
        });

        component = TestBed.createComponent(BooksList).componentInstance;
        libraryService = TestBed.inject(LibraryService) as jasmine.SpyObj<LibraryService>;
        router = TestBed.inject(Router) as jasmine.SpyObj<Router>;
    });

    describe('ngOnInit', () => {
        it('should navigate to the manage library route when there are not libraries', () => {
            libraryService.getLibraries.and.returnValue(Observable.create(observer => {
                observer.next([]);
            }));

            component.ngOnInit();

            expect(router.navigateByUrl).toHaveBeenCalledWith('/manage-library');
        });

        it('should navigate to default route when there are libraries', () => {
            libraryService.getLibraries.and.returnValue(Observable.create(observer => {
                observer.next([<ILibrary>{ id: 1, path: 'path' }]);
            }));

            component.ngOnInit();

            expect(router.navigateByUrl).toHaveBeenCalledWith('/');
        });
    });
})