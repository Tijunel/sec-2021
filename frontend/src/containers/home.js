import React from "react";
import WatchList from "./components/watchList";
import Portfolios from "./components/portfolios";

const watchList = <WatchList />;

const Home = () => {
  return (
    <div id="home">
      {watchList}
      <Portfolios />
    </div>
  );
};

export default Home;
