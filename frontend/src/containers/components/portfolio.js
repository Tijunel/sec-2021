import React from "react";
import { Button } from "react-bootstrap";
import "./_styling/portfolio.css";

const Portfolio = (props) => {
  return (
    <div className="portfolio" key={props.portfolio.id}>
      <div id="name">{props.portfolio.name}</div>
      <Button onClick={() => props.select(props.portfolio)}>View</Button>
    </div>
  );
};

export default Portfolio;
