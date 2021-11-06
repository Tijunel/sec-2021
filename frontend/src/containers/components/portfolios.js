import React, { useEffect, useState, useRef } from "react";
import { Form, Button } from "react-bootstrap";
import Portfolio from "./portfolio";

const Portfolios = (props) => {
  const [portfolios, setPortfolios] = useState([]);
  const newPortfolioNameRef = useRef();

  useEffect(() => {
    fetch("/api/portfolios", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      credentials: "include",
    })
      .then(async (res) => {
        if (res.status === 200) {
          let existingPortfolios = await res.json();
          console.log(existingPortfolios);
          setPortfolios(existingPortfolios);
        } else {
          // Handle error
        }
      })
      .catch((error) => {
        // Handle error
      });
  }, []);

  const createPortfolio = () => {
    let name = newPortfolioNameRef.current.value;
    fetch("/api/portfolio/" + name, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      credentials: "include",
    })
      .then(async (res) => {
        if (res.status === 200) {
          let newPortfolio = await res.json();
          setPortfolios((pastPortfolios) => [...pastPortfolios, newPortfolio]);
          newPortfolioNameRef.current.value = "";
        } else {
          // Handle error
        }
      })
      .catch((error) => {
        // Handle error
      });
  };

  return (
    <div id="portfolio-list">
      <h2>Portfolios</h2>
      {portfolios.map((portfolio) => {
        return (
          <Portfolio portfolio={portfolio} select={props.selectPortfolio} />
        );
      })}
      <div id="create">
        <Form.Control ref={newPortfolioNameRef} />
        <br />
        <Button onClick={createPortfolio}>Create New Portfolio</Button>
      </div>
    </div>
  );
};

export default Portfolios;
