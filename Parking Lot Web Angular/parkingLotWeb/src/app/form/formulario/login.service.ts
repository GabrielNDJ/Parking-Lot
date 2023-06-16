import { Injectable } from "@angular/core";
import { Route } from "@angular/router";



export class loginService{

    constructor(private router:Route){}

    token:string | undefined;

    login(Username:string, password:string){

    }
}