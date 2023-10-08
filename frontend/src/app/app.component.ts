import { Component, OnInit } from '@angular/core';
import { MessageService } from 'primeng/api';
import {DataService} from './services/data.service';
import { FileUploadEvent } from 'primeng/fileupload';

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
  sort_order = 1;
  file_type = 'img';
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

    let data = this.dataService.imageSearch(event.files[0])
    

    this.messageService.add({ severity: 'info', summary: 'Success', detail: 'File Uploaded with Basic Mode' });
  };

  showQueryTable() {
    this.showTable = true;
    if (!this.query.trim().length) {
      alert("Type query first")
      return
    }
    let response: any = this.dataService.contextSearch(this.query, this.sort_by, this.sort_order, this.file_type);

    this.limit = response['limit']
    this.files = response['query']
    this.total_pages = response['total_pages']
    this.offset = response['offset']
    this.pagination_line = "Showing page " + (this.offset/this.limit)+ " out of" + this.total_pages + " pages."
  }

  pageChange(event: any) {
    this.offset = event.first;
    this.limit = event.rows;

    this.showQueryTable();
}

downloadFile(fileName: string) {
  // You should replace this with your actual file download logic.
  // For demonstration purposes, we'll create a dummy download link.
  
  // Create an anchor element for downloading the file.
  const link = document.createElement('a');
  
  // Construct the file URL or path. You should replace 'your_base_url' with the actual base URL.
  const fileUrl = `http://10.159.44.185:8080/${fileName}`;
  
  // Set the anchor's href attribute to the file URL.
  link.href = fileUrl;
  
  // Specify the download attribute to suggest a file name for the downloaded file.
  link.download = fileName;
  
  // Trigger a click event to initiate the download.
  link.click();
  
  // Cleanup: Remove the anchor element from the DOM.
  document.body.removeChild(link);
}





}
