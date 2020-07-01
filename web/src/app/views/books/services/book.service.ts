import { Injectable } from '@angular/core';

import { Observable } from 'rxjs';

import { HttpService } from '../../../common';

import { IPage } from '../models/book.model';

@Injectable()
export class BookService {
    constructor(private http: HttpService){}

    public getBooks(offset: number, count: number): Observable<IPage> {
        return this.http.get<IPage>(`/books/${offset}/${count}`);
    }
}