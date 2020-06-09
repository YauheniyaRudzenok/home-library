import { TestBed } from '@angular/core/testing';
import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';

import { HttpService } from '../http.service';
import { IPath } from '../../models';
import { environment } from '../../../environments/environment'


describe('HttpService', () => {
    const expectedPath = <IPath>{path: 'path', folders:[]};
    const testUrl = '/test';

    let service: HttpService;
    let httpClient: jasmine.SpyObj<HttpClient>;

    beforeEach(() => {
        var spy = jasmine.createSpyObj('HttpClient', ['get', 'delete', 'post']);

        TestBed.configureTestingModule({
            providers: [
                HttpService,
                { provide: HttpClient, useValue: spy }
            ]
        });

        service = TestBed.inject(HttpService);
        httpClient = TestBed.inject(HttpClient) as jasmine.SpyObj<HttpClient>;
    })

    it('should get', () => {
        httpClient.get.and.returnValue(Observable.create(observer => {
            observer.next(expectedPath);
        }));

        service.get(testUrl).subscribe((result: IPath) => {
            expect(result).toBeTruthy();

            expect(httpClient.get).toHaveBeenCalledWith(environment.api + testUrl);
        });
    });

    it('should post', () => {
        httpClient.post.and.returnValue(Observable.create(observer => {
            observer.next(expectedPath);
        }));

        service.post(testUrl, expectedPath).subscribe((result: IPath) => {
            expect(result).toBeTruthy();

            expect(httpClient.post).toHaveBeenCalledWith(environment.api + testUrl, expectedPath);
        });
    });

    it('should delete', () => {
        httpClient.delete.and.returnValue(Observable.create(observer => {
            observer.next(new Object());
        }));

        service.delete(testUrl).subscribe(result => {
            expect(result).toBeTruthy();

            expect(httpClient.delete).toHaveBeenCalledWith(environment.api + testUrl);
        });
    });
})