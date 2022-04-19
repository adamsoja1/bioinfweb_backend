import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import App2 from './components/blog/blog'
import App3 from './components/blog/add'
import { render } from "react-dom";

import { BrowserRouter as Router, Route
} from "react-router-dom";

ReactDOM.render((
  <Router>
    <Route path='/' render={App} />
    <Route exact path='/blog' render ={App2}/>
    <Route exact path = '/dodaj' render = {App3}/>
  </Router>
  ),
  document.getElementById('root')
);
