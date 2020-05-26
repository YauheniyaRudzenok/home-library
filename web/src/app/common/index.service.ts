import { Injectable } from '@angular/core';

import { HttpService } from './http.service';
import { Observable } from 'rxjs';

@Injectable()
export class IndexService {
    constructor(private http: HttpService){}

    indexLibrary(libraryId: number): Observable<Object> {
        return this.http.get(`/index/${libraryId}`);
    }
}