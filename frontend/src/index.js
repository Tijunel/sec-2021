import React from "react";
import ReactDOM from "react-dom";
import { Switch, BrowserRouter as Router, Route } from "react-router-dom";

import Home from "./containers/home";
import NotFound from "./containers/components/watchList";

import "bootstrap/dist/css/bootstrap.min.css";
import "./index.css";

ReactDOM.render(
  <React.StrictMode>
    <Router>
      <Switch>
        <Route path="/" component={Home} />
        <Route path="*" exact={true} component={NotFound} />
      </Switch>
    </Router>
  </React.StrictMode>,
  document.getElementById("root")
);
