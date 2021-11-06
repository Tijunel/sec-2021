import React, { useEffect, useState } from "react";
import Coin from "./coin";

const PortfolioInspect = (props) => {
  const [portfolioCoins, setPortfolioCoins] = useState([]);

  useEffect(() => {
    fetch("/api/portfolio/" + props.portfolio.portfolio_id, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      credentials: "include",
    })
      .then(async (res) => {
        if (res.status === 200) {
          let coins = await res.json();
          setPortfolioCoins(coins);
        } else {
          // Error
        }
      })
      .catch({
        // Error
      });
  }, []);

  const onRemove = (coin) => {
    fetch("/api/portfolio/" + props.portfolio.portfolio_id + "/" + coin.id, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      credentials: "include",
    })
      .then((res) => {
        if (res.status === 200) {
          let currentCoins = [...portfolioCoins];
          currentCoins = currentCoins.filter((c) => coin.id !== c.id);
          setPortfolioCoins(currentCoins);
        } else {
          // Error
        }
      })
      .catch((error) => {
        // Error
      });
  };

  return (
    <div id="portfolio-inspect">
      <h2>{props.portfolio.name}</h2>
      <h3>Assets:</h3>
      {portfolioCoins.map((coin) => (
        <Coin coin={coin} onRemove={onRemove} />
      ))}
    </div>
  );
};

export default PortfolioInspect;
