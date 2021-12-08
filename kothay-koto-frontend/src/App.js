import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";
import Authentication from './components/Authentication/Authentication';
import Header from './components/Header/Header'
import './App.css';
import Carousel from './components/Carousel/Carousel';
import Deals from './components/Deals/Deals';
import Footer from './components/Footer/Footer';
import NotFound from './components/NotFound/NotFound';
import ProductDetails from './components/ProductDetails/ProductDetails';

function App() {
  return (
    <Router>
      <div className="mainApp">
      <Switch>
        <Route exact path ="/">
        <Header></Header>
        <Carousel></Carousel>
        <Deals></Deals>
        <Footer></Footer>
        </Route>
        <Route path ="/login">
        <Authentication></Authentication>
        </Route>
        <Route path ="/logitechG403">
        <Header></Header>
        <ProductDetails></ProductDetails>
        <Footer></Footer>
        </Route>
        <Route path="*">
        <NotFound />
        </Route>
      </Switch>
      </div>
    </Router>
  );
}

export default App;
