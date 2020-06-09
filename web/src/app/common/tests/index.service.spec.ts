import { TestBed } from '@angular/core/testing';

import { Observable } from 'rxjs';

import { HttpService } from '../http.service';
import { IndexService } from '../index.service';


describe('IndexService', () => {
    let service: IndexService;
    let httpService: jasmine.SpyObj<HttpService>;

    beforeEach(() => {
        var spy = jasmine.createSpyObj('HttpService', ['get']);

        TestBed.configureTestingModule({
            providers: [
                IndexService,
                { provide: HttpService, useValue: spy }
            ]
        });

        service = TestBed.inject(IndexService);
        httpService = TestBed.inject(HttpService) as jasmine.SpyObj<HttpService>;
    })

    it('should index library', () => {
        const testId = 1;

        httpService.get.and.returnValue(Observable.create(observer => {
            observer.next(new Object());
        }));

        service.indexLibrary(testId).subscribe(result => {
            expect(result).toBeTruthy();

            expect(httpService.get).toHaveBeenCalledWith(`/index/${testId}`);
        });
    });
})