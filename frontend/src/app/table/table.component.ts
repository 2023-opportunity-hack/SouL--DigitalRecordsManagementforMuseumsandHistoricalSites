import { Component, OnInit } from '@angular/core';
import { MessageService } from 'primeng/api';
import {DataService} from '../services/data.service';
import { HttpClient, HttpEventType } from  '@angular/common/http';
import { Router } from '@angular/router';

// Import the AuthService type from the SDK
import { AuthService } from '@auth0/auth0-angular';
import { FileUploadEvent } from 'primeng/fileupload';


@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.scss']
})
export class TableComponent implements OnInit {
  query: string = "";
  files: any = [];
  limit = 10;
  offset = 0;
  sort_by = 'rank';
  sort_order = 1;
  filetype = '';
  total_pages = 0;
  pagination_line = ""
  url = 'http://10.159.44.185:8080/'

  showTable = false;

  table_config = [
    {
      'name':'rank',
      'label': 'Rank',
      'width':'13%',
      'filter': false
    },
    {
      'name':'filename',
      'label': 'Name',
      'width':'40%',
      'filter': true
    },
    {
      'name':'filetype',
      'label': 'Categories',
      'width':'20%',
      'filter': true
    },
    {
      'name':'creation_date',
      'label': 'Date',
      'width':'40%',
      'filter': false
    },
  ]

  constructor(public http: HttpClient, private messageService: MessageService, public dataService: DataService, public auth: AuthService, public router: Router) {}
  
  ngOnInit(): void {
  }

  AuthButtonComponent(){
  }

  customSort(event: any) {
    this.sort_by = event.field
    this.sort_order = event.order
    this.showQueryTable();
    event.data.sort((data1: any, data2: any) => {
      let value1 = data1[event.field];
      let value2 = data2[event.field];
      let result = null;

      if (value1 == null && value2 != null) result = -1;
      else if (value1 != null && value2 == null) result = 1;
      else if (value1 == null && value2 == null) result = 0;
      else if (typeof value1 === 'string' && typeof value2 === 'string') result = value1.localeCompare(value2);
      else result = value1 < value2 ? -1 : value1 > value2 ? 1 : 0;

      return event.order * result;
    })
  }

  onUpload(event: FileUploadEvent) {
    
    let response: any = this.dataService.imageSearch(event.files[0])
    this.messageService.add({ severity: 'info', summary: 'Success', detail: 'File Uploaded with Basic Mode' });
  };

  showQueryTable() {
    this.showTable = true;
    if (!this.query.trim().length) {
      alert("Type query first")
      return
    }

    let request = '?'
    if(this.query.trim().length) {
      request = request+'query='+this.query
      request = request+'&sort_by='+this.sort_by+'&sort_order='+this.sort_order
    } else {
      request = request+'sort_by='+this.sort_by+'&sort_order='+this.sort_order
    }
    
    if(this.filetype.trim().length) {
      request = request+'&filetype='+this.filetype
    }

    this.http.get(this.url+"search"+request).subscribe((response: any) => {
      this.files = response
    })
  }

  pageChange(event: any) {
    this.offset = event.first;
    this.limit = event.rows;

    this.showQueryTable();
}
  goToOtherComponent(): void {
    this.router.navigate(['']); // Navigate to OtherComponent
  }



}
