import React, { useState } from "react";
import WatchList from "./components/watchList";
import Portfolios from "./components/portfolios";
import PortfolioInspect from "./components/portfolioInspect";
import "./_styling/home.css";

const watchList = <WatchList />;

const Home = () => {
  const [portfolio, setPortfolio] = useState(null);

  const selectPortfolio = (portfolio) => {
    setPortfolio(portfolio);
  };

  return (
    <div id="home">
      {watchList}
      {portfolio ? (
        <PortfolioInspect
          exit={() => selectPortfolio(null)}
          portfolio={portfolio}
        />
      ) : (
        <Portfolios selectPortfolio={selectPortfolio} />
      )}
    </div>
  );
};

export default Home;
