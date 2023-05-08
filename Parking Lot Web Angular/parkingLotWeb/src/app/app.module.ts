import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { headerComponent } from './header/header.componet';
import { NavComponent } from './nav/nav.component';
import { FooterComponent } from './footer/footer.component';
import { AdminComponent } from './admin/admin.component';
import { ClientesComponent } from './clientes/clientes.component';
import { EmpleadosComponent } from './empleados/empleados.component';
import { FacturacionComponent } from './facturacion/facturacion.component';
import { TarifasComponent } from './tarifas/tarifas.component';
import { Route, RouterModule } from '@angular/router';
import { TiendaComponent } from './tienda/tienda.component';

const Route=[ //importante para el ruteo

  {path:'', component:AdminComponent},
  {path:'clientes', component:ClientesComponent},
  {path:'empleado', component:EmpleadosComponent},
  {path:'facturacion', component:FacturacionComponent},
  {path:'tarifas', component:TarifasComponent},
  {path:'tienda',Comment:TiendaComponent}
]

@NgModule({
  declarations: [
    AppComponent, 
    headerComponent, 
    NavComponent, 
    FooterComponent, 
    AdminComponent, 
    ClientesComponent, 
    EmpleadosComponent, 
    FacturacionComponent, 
    TarifasComponent, TiendaComponent,
  ],

  imports: [
    BrowserModule,
    AppRoutingModule, 
    RouterModule.forRoot(Route)// impotante para el ruteo
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
