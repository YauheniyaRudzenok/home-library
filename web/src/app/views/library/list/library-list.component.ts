import { Component, OnInit } from '@angular/core';

import { ILibrary } from '../../../models';
import { LibraryService } from '../../../common';

@Component({
    templateUrl:'./library-list.component.html',
    selector: 'library-list',
    styleUrls: ['./library-list.component.scss']
})
export class LibraryList implements OnInit {
    constructor(private libraryService: LibraryService){}

    Libraries: ILibrary[];

    ngOnInit(): void {
        this.libraryService.getLibraries().subscribe((data: ILibrary[]) => {
            this.Libraries = data;
        });
    }
}