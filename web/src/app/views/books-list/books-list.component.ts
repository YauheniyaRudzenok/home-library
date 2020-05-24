import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { LibraryService } from '../../common';
import { ILibrary } from '../../models';

@Component({
    templateUrl:'./books-list.component.html',
    selector: 'books-list'
})
export class BooksList implements OnInit {
    constructor(private libraryService: LibraryService, private router: Router) { }
    ngOnInit() {
        this.libraryService.getLibraries().subscribe((data: ILibrary[]) => {
            if(data.length > 0) {
                this.router.navigateByUrl('/');
            } else {
                this.router.navigateByUrl('/manage-library');
        }
    });
  }
}