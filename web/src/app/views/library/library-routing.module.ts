import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { LibraryList } from './list/library-list.component';
import { ManageLibrary } from './manage/manage-library.component';

const routes: Routes = [
  { path: '', component: LibraryList },
  { path: 'libraries/manage', component: ManageLibrary }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class LibraryRoutingModule { }