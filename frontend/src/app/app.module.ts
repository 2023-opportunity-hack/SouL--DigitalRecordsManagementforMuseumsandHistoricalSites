import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { TableModule } from 'primeng/table';
import { FormsModule } from '@angular/forms';
import { InputTextModule } from 'primeng/inputtext';
import { FileUploadModule } from 'primeng/fileupload';
import { PaginatorModule } from 'primeng/paginator';
import { ButtonModule } from 'primeng/button';
import { ToastModule } from 'primeng/toast';
import { HttpClientModule } from  '@angular/common/http';
import { AppRoutingModule } from './app-routing.module'; // CLI imports AppRoutingModule
import { NgxDocViewerModule } from 'ngx-doc-viewer';

// import { MultiSelectModule } from 'primeng/multiselect';

import { AppComponent } from './app.component';


// Import the module from the SDK
import { AuthModule } from '@auth0/auth0-angular';
import { SearchComponent } from './search/search.component';
import { TableComponent } from './table/table.component';
// import { AuthComponent } from './auth/auth.component';

@NgModule({
  declarations: [
    AppComponent,
    SearchComponent,
    TableComponent,
    // AuthComponent
  ],
  imports: [
    BrowserModule,
    TableModule,
    FormsModule,
    InputTextModule,
    NgxDocViewerModule,
    FileUploadModule,
    ToastModule,
    PaginatorModule,
    ButtonModule,
    BrowserAnimationsModule,
    HttpClientModule,
    AuthModule.forRoot({
      domain: 'dev-jrjxmhfae7ttlg5k.us.auth0.com',
      clientId: 'Qrf6s2X0Bue3LTQtv6zUNZzHo5Qc7GRZ',
      authorizationParams: {
      redirect_uri: 'http://localhost:4200/table'
      }
    }),
    AppRoutingModule
  ],
  bootstrap: [AppComponent],
})

export class AppModule {}
