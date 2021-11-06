import React, { useEffect, useState } from "react";
import CoinSearch from "./coinSearch";
import Coin from "./coin";

const WatchList = () => {
  const [coins, setCoins] = useState([]);

  useEffect(() => {
    fetch("/api/watchlist", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      credentials: "include",
    }).then(async (res) => {
      if (res.status === 200) {
        let watchListCoins = await res.json();
        setCoins(watchListCoins);
      }
    });
  }, []);

  const onCoinAdded = (coin) => {
    setCoins((prevCoins) => [...prevCoins, coin]);
  };

  const removeCoin = (coin) => {
    fetch("/api/watchlist/coin", {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      credentials: "include",
      body: JSON.stringify(coin),
    })
      .then((res) => {
        if (res.status === 200) {
          let tempCoins = [...coins];
          tempCoins = tempCoins.filter((c) => c.id !== coin.id);
          setCoins(tempCoins);
        } else {
          // Error
        }
      })
      .catch((err) => {
        // Error
      });
  };

  return (
    <div id="watch-list">
      <h2>Watch List</h2>
      {coins.map((coin) => (
        <Coin coin={coin} onRemove={removeCoin} />
      ))}
      <br />
      <CoinSearch onCoinSelect={onCoinAdded} />
    </div>
  );
};

export default WatchList;
