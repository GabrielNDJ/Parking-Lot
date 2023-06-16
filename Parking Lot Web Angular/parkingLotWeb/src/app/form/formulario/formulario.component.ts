import { Component } from '@angular/core';
import { FormBuilder, NgForm, Validator, Validators } from '@angular/forms';
import { Route } from '@angular/router';

@Component({
  selector: 'app-formulario',
  templateUrl: './formulario.component.html',
  styleUrls: ['./formulario.component.css']
})
export class FormularioComponent {

  loginform=this.formBuilder.group({
    Username:['', [Validators.required]],
    password:['', [Validators.required]]
  })

  constructor(private formBuilder:FormBuilder){}
  

  ngOnInit():void{

  }

  login(form:NgForm){
    const Username= form.value.Username

    const password= form.value.Password
  }
}
