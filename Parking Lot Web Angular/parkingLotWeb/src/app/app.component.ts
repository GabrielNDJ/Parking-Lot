import { Component } from '@angular/core';
import { AutenticationService } from './services/autentication.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'miPrimeraAplicacion';

  constructor(private loginPrd:AutenticationService){}

  public visualizacionMenu():boolean{
    return this.loginPrd.hablitarLogeo();
  }
}
