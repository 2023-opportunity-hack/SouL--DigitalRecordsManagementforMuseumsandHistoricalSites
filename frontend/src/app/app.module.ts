import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { TableModule } from 'primeng/table';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { InputTextModule } from 'primeng/inputtext';
import { FileUploadModule } from 'primeng/fileupload';
import { PaginatorModule } from 'primeng/paginator';
import { ButtonModule } from 'primeng/button';
import { ToastModule } from 'primeng/toast';
import { HttpClientModule } from  '@angular/common/http';
import { AppRoutingModule } from './app-routing.module'; // CLI imports AppRoutingModule
import { NgxDocViewerModule } from 'ngx-doc-viewer';
import { TooltipModule } from 'primeng/tooltip';

// import { MultiSelectModule } from 'primeng/multiselect';

import { AppComponent } from './app.component';


// Import the module from the SDK
import { AuthModule } from '@auth0/auth0-angular';
import { LoginComponent } from './login/login.component';
import { TableComponent } from './table/table.component';
import { HomepageComponent } from './homepage/homepage.component';
// import { AuthComponent } from './auth/auth.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    TableComponent,
    HomepageComponent,
    // AuthComponent
  ],
  imports: [
    BrowserModule,
    TableModule,
    FormsModule,
    TooltipModule,
    ReactiveFormsModule,
    InputTextModule,
    NgxDocViewerModule,
    FileUploadModule,
    ToastModule,
    PaginatorModule,
    ButtonModule,
    BrowserAnimationsModule,
    HttpClientModule,
    AuthModule.forRoot({
      domain: 'dev-do75vkgslcepewnw.us.auth0.com',
      clientId: 'vqOLNJQ8AftsIWhVqLbMzlLyqjSzZzJj',
      authorizationParams: {
        redirect_uri: window.location.origin
      }
    }),
    AppRoutingModule
  ],
  bootstrap: [AppComponent],
})

export class AppModule {}
