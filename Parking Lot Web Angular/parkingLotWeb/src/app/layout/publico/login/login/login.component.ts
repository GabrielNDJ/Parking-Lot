import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AutenticationService } from 'src/app/services/autentication.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  public myForm!:FormGroup;

  constructor(private fb:FormBuilder, private loginPrd:AutenticationService){}


  ngOnInit(): void {
    this.myForm = this.createMyForm();
  }

  private createMyForm():FormGroup{
    return this.fb.group({
      usuario:['', Validators.required],
      password:['', Validators.required]
    });
  }

  public submitFormulario(){
    console.log(this.myForm)
    if(this.myForm.invalid){
      Object.values(this.myForm.controls).forEach(control =>{
        control.markAllAsTouched();
      });
      return;
    }

    if (!this.loginPrd.ingresarAplicativo(this.myForm.value)){
      alert('usuario o contraseña invalida')
    }
  }


  public get f():any{
    return this.myForm.controls;
  }
}
