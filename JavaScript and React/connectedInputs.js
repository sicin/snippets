import React, { useState } from "react";

const BuyTokenPage = () => {
    const [firstVal, setFirstVal] = useState(0);
    const [secondVal, setSecondVal] = useState(0);
  
    const changeFirstValue = (e) => {
      setSecondVal(e.target.value);
      setFirstVal(e.target.value);
    };
  
    const changeSecondValue = (e) => {
      setFirstVal(e.target.value);
      setSecondVal(e.target.value);
    };
  
    const handleSubmit = (e) => {
      e.preventDefault();
      const usdt = e.target.usdt.value;
      const token = e.target.token.value;
      console.log(usdt + " " + token);
    };
  
    return (
          <form
            onSubmit={handleSubmit}
            className="d-flex flex-column flex-xl-row justify-content-between align-items-center"
          >
            <div className="buy-token-box">
              <input
                className="buy-token-form"
                id="usdt-input"
                placeholder="0.0"
                type="number"
                min="0"
                max="999999"
                name="usdt"
                value={firstVal}
                onChange={changeFirstValue}
              />
              <label className="usdt-label-padding" htmlFor="usdt-input">
                USDT
              </label>
            </div>
            <p className="swap-arrows fs-5">&#8644;</p>
            <div className="buy-token-box">
              <input
                className="buy-token-form"
                id="token-input"
                placeholder="0.0"
                type="number"
                min="0"
                max="999999"
                name="token"
                value={secondVal}
                onChange={changeSecondValue}
              />
              <label htmlFor="token-input">LOMBI TOKEN</label>
            </div>
            <button
              className="buy-token-btn ms-xl-5 mt-6 mt-xl-0 px-0"
              type="submit"
            >
              SWAP
            </button>
          </form>
    );
  };
  
  export default BuyTokenPage;
  