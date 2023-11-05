import { Component, OnInit } from '@angular/core';
import { CommonService } from '../services/common.service';
import { FormGroup, FormControl, FormBuilder } from '@angular/forms';
import { Router } from '@angular/router';


@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.scss']
})
export class HomepageComponent implements OnInit {
  queryForm = new FormGroup({
    query: new FormControl('')
  });

  constructor(public commonservice: CommonService, private router: Router) {
  }

  // TODO: Insert audio search

  ngOnInit(): void {
  }

  onSubmit() {
    // Handle form submission here
    console.log(this.queryForm.value);
    this.router.navigate(['/table'], {
      queryParams: { query: this.queryForm.value.query }
    });
  }


  login() {
    this.commonservice.login();
  }

}