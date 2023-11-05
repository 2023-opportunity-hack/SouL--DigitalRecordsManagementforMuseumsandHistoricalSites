/*
 * -----------------------------------------------------------------------
 * File: common.service.ts
 * Creation Time: Nov 4th 2023 5:33 pm
 * Author: Saurabh Zinjad
 * Developer Email: zinjadsaurabh1997@gmail.com
 * Copyright (c) 2023 Saurabh Zinjad. All rights reserved | GitHub: Ztrimus
 * -----------------------------------------------------------------------
 */

import { Injectable } from '@angular/core';
import { AuthService } from '@auth0/auth0-angular';

@Injectable({
  providedIn: 'root'
})
export class CommonService {
  query = ""

  constructor(public auth: AuthService) { }

  getQuery(query: string) {
    this.query = query;
    return this.query
  }

  login() {
    return this.auth.loginWithRedirect({
      appState: { target: "search" }
    });
  }
}
