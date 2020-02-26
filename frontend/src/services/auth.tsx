import { Observable, BehaviorSubject } from "rxjs";
import { map } from "rxjs/operators";

import { localStorageService } from "./storage"

class AuthService {
  private tokenSubject$ = new BehaviorSubject<string | null>(localStorageService.getToken());

  public isAuthenticated(): Observable<boolean> {
    return this.tokenSubject$.pipe(map(token => !!token));
  }
}

const authService = new AuthService();

export default authService;
