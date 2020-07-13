import { Injectable } from '@angular/core';

import { Observable } from 'rxjs';

import { HttpService } from '../../../common';

import { IPage, IBook } from '../models/book.model';

@Injectable()
export class BookService {
    constructor(private http: HttpService){}

    public getBooks(offset: number, count: number): Observable<IPage> {
        return this.http.get<IPage>(`/books/${offset}/${count}`);
    }

    public getBook(id: number): Observable<IBook> {
        return this.http.get<IBook>(`/books/${id}`);
    }

    public update(book: IBook): Observable<Object> {
        return this.http.put<IBook>(`/books/${book.id}`, book);
    }
}