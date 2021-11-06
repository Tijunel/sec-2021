import React from "react";
import ReactDOM from "react-dom";
import {
  Routes as Switch,
  BrowserRouter as Router,
  Route,
} from "react-router-dom";

import Home from "./containers/home";
import NotFound from "./containers/components/watchList";

import "./index.css";

ReactDOM.render(
  <React.StrictMode>
    <Router>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="*" exact={true} component={NotFound} />
      </Switch>
    </Router>
  </React.StrictMode>,
  document.getElementById("root")
);
