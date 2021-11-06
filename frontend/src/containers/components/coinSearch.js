import React, { useRef, useState } from "react";
import { Form, Button } from "react-bootstrap";
import Coin from "./coin";

const CoinSearch = (props) => {
  const [coins, setCoins] = useState([]);
  const [loading, setLoading] = useState(false);
  const searchField = useRef();

  const searchForCoin = () => {
    let query = searchField.current.value;
    setLoading(true);
    fetch("/api/coins/search/" + query, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      credentials: "include",
    })
      .then(async (res) => {
        if (res.status === 200) {
          let newCoins = await res.json();
          console.log(newCoins);
          setCoins(newCoins);
          searchField.current.value = "";
        } else {
          // Handle error
        }
        setLoading(false);
      })
      .catch((error) => {
        // Handle error
        setLoading(false);
      });
  };

  const onSelect = (coin) => {
    fetch("/api/watchlist/coin", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      credentials: "include",
      body: JSON.stringify(coin),
    })
      .then((res) => {
        if (res.status === 200) {
          props.onCoinSelect(coin);
          let newCoins = [...coins];
          newCoins = newCoins.filter((c) => c.id !== coin.id);
          setCoins(newCoins);
        } else {
          // Handle error
        }
      })
      .catch((error) => {
        // Handle error
      });
  };

  return (
    <div id="search">
      <Form.Control ref={searchField} />
      <br />
      <Button onClick={searchForCoin}>Search Coins</Button>
      <br />
      {loading ? "Loading..." : ""}
      <br />
      {coins.map((coin) => {
        return <Coin coin={coin} onSelect={onSelect} />;
      })}
    </div>
  );
};

export default CoinSearch;
