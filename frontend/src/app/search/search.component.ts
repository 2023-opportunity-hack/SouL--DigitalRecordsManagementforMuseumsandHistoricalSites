import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';


// Import the AuthService type from the SDK
import { AuthService } from '@auth0/auth0-angular';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss']
})
export class SearchComponent implements OnInit {

  constructor(public auth: AuthService,  public router: Router) {}
  
  ngOnInit(): void {
  }

  login() {
    return this.auth.loginWithRedirect({
      appState: {target: "table"}
});
  }
}