import { Component,  OnDestroy, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Subject } from 'rxjs';

@Component({
  selector: 'app-clientes',
  templateUrl: './clientes.component.html',
  styleUrls: ['./clientes.component.css']
})
export class ClientesComponent implements OnDestroy, OnInit {

  dtOptions: DataTables.Settings = {};
  dtTrigger: Subject<any> = new Subject<any>();
  data: any
e: any;

  constructor(private httpClient: HttpClient) { }

  ngOnInit(): void {
    this.dtOptions = {
      pagingType: 'full_numbers',
      pageLength: 5
    };
    this.httpClient.get('https://jsonplaceholder.typicode.com/users')
      .subscribe((res: any) =>{
        this.data= res.data;
        this.dtTrigger.next;
      })
    
  }

  ngOnDestroy(): void {
    this.dtTrigger.unsubscribe();
  }

  
};
