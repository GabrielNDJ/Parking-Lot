import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AutenticationService {

  constructor() { }

  private ingresar:boolean = false;

  public ingresarAplicativo(obj:any):boolean{
  
    return this.ingresar= obj.usuario == 'admin' && obj.password == 'admin';
      this.ingresar  
  }

  public hablitarLogeo(){
    return this.ingresar
  }
}
