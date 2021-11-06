import React from "react";
import { Button } from "react-bootstrap";
import "./_styling/coin.css";

const Coin = (props) => {
  return (
    <div key={props.coin.id} className="coin">
      <div className="coin-name">{props.coin.name}</div>
      <div className="coin-ticker">{props.coin.ticker}</div>
      <div className="coin-price">${props.coin.price} (USD)</div>
      {props.onRemove ? (
        <Button onClick={() => props.onRemove(props.coin)}>Remove</Button>
      ) : (
        ""
      )}
      {props.onSelect ? (
        <Button onClick={() => props.onSelect(props.coin)}>Select</Button>
      ) : (
        ""
      )}
    </div>
  );
};

export default Coin;
