import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { SearchComponent } from './search/search.component';
import { TableComponent } from './table/table.component';

const routes: Routes = [
  { path: '', component: SearchComponent }, // Route to SearchComponent
  { path: 'table', component: TableComponent}, // Default route
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
