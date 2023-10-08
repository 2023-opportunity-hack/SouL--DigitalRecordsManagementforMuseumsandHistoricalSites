import { Component, OnInit } from '@angular/core';
import { MessageService } from 'primeng/api';
import {DataService} from './services/data.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  providers: [MessageService]
})
export class AppComponent implements OnInit {
  query: string = "";
  files: any = [];
  limit = 10;
  offset = 0;
  sort_by = 'rank';
  sort_order = 'ASC';
  file_type = '';
  total_pages = 0;
  pagination_line = ""

  showTable = false;

  table_config = [
    {
      'name':'rank',
      'label': 'Rank',
      'width':'13%',
      'filter': false
    },
    {
      'name':'name',
      'label': 'Name',
      'width':'40%',
      'filter': true
    },
    {
      'name':'type',
      'label': 'Categories',
      'width':'20%',
      'filter': true
    },
    {
      'name':'date',
      'label': 'Date',
      'width':'40%',
      'filter': false
    },
  ]

  constructor(private messageService: MessageService, private dataService: DataService) {}

  ngOnInit(): void {
  }

  customSort(event: any) {
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

  onUpload(event: any) {
    this.messageService.add({ severity: 'info', summary: 'Success', detail: 'File Uploaded with Basic Mode' });
  };

  getQueryData() {
    this.showTable = true;
    let response: any = this.dataService.getQueryData(this.query, this.limit, this.offset, this.sort_by, this.sort_order, this.file_type);
    
    this.limit = response['limit']
    this.total_pages = response['total_pages']
    this.files = response['query']
    this.offset = response['offset']
    this.pagination_line = (this.offset/this.limit)+ " out of" + this.total_pages + " pages."
  }

}
