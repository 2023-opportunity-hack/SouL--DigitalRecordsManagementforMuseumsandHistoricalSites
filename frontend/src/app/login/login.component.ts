import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CommonService } from '../services/common.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  constructor(public commonservice: CommonService,  public router: Router) {}
  
  ngOnInit(): void {
  }

  login() {
    this.commonservice.login();
  }
}