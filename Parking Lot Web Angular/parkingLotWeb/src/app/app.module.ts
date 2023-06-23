import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { DataTablesModule } from "angular-datatables";
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
import { FormularioComponent } from './form/formulario/formulario.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { PasarelaPagoComponent } from './pasarela-pago/pasarela-pago.component';
import { LoginComponent } from './layout/publico/login/login/login.component';
import { PrincipalComponent } from './layout/privado/principal/principal/principal.component';

const Route=[ //importante para el ruteo

  {path:'', component:AdminComponent},
  {path:'admin', component:AdminComponent},
  {path:'clientes', component:ClientesComponent},
  {path:'empleado', component:EmpleadosComponent},
  {path:'facturacion', component:FacturacionComponent},
  {path:'tarifas', component:TarifasComponent},
  {path:'login', component:FormularioComponent}
];

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
    TarifasComponent,
    FormularioComponent,
    PasarelaPagoComponent,
    LoginComponent,
    PrincipalComponent,
    
  ],

  imports: [
    BrowserModule,
    AppRoutingModule, 
    RouterModule.forRoot(Route),// impotante para el ruteo
    ReactiveFormsModule,
    DataTablesModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
