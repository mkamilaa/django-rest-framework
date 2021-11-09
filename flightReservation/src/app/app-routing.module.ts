import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ConfirmReservationComponent } from './components/confirm-reservation/confirm-reservation.component';
import { DisplayFlightsComponent } from './components/display-flights/display-flights.component';
import { FindFlightsComponent } from './components/find-flights/find-flights.component';
import { PassengerDetailsComponent } from './components/passenger-details/passenger-details.component';

const routes: Routes = [
  {path:'',redirectTo:'',pathMatch:'full'},
  {
    path:'findFlights',
    component: FindFlightsComponent

  },
  {
    path:'displayFlights',
    component: DisplayFlightsComponent

  },
  {
    path:'passengerDetails/:id',
    component: PassengerDetailsComponent

  },
  {
    path:'confirmReservation/:id',
    component: ConfirmReservationComponent

  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
