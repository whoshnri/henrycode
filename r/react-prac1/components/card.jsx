import { useState } from 'react';
import './card.css';

function Card({ img, id, price, details }) {
  const [total, setTotal] = useState(price);
  const [quantity, setQuantity] = useState(1);
  const [isDetailsVisible, setDetailsVisible] = useState(false);
  const [active, setActive] = useState({});

  const showItemDetails = () => {
    const activeItem = { image: img, id, rating: '4.4', details, price };
    setActive(activeItem);
    setDetailsVisible(true);
  };

  const closePopup = () => {
    setDetailsVisible(false);
    setActive({});
  };

  const increaseQuantity = () => {
    if (quantity < 10) {
      setQuantity(quantity + 1);
      setTotal((quantity + 1) * active.price);
    }
  };

  const decreaseQuantity = () => {
    if (quantity > 0) {
      setQuantity(quantity - 1);
      setTotal((quantity - 1) * active.price);
    }
  };

  return (
    <>
      <div className="card">
        <div className="card-img" onClick={showItemDetails}>
          <img className="item-img" src={img} alt="item-img" />
        </div>

        <div className="item-overlay">
          <p className="item-details">{details}</p>
          <div className="item-price">${price}</div>
          <img src="../assets/tag.svg" alt="tag" width="26px" height="33px" className="tag" />
          <button className="buy">Buy Now</button>
          <button className="add-to-cart">Add to Cart</button>
        </div>
      </div>

      {isDetailsVisible && (
        <div className="card-details">
          <div className="close" onClick={closePopup}>
            <img src="../assets/close.svg" alt="Close" height="50px" className="close-svg" />
          </div>

          <img src={active.image} alt="Active Item" />
          <div className="details-details">
            <div className="details-head">
              <h2>{details}</h2>
              <p>Maker: Adidas</p>
              <div className="details-price">{'$' + active.price}</div>
            </div>

            <p className="specs">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero, perspiciatis
              consequatur praesentium alias laborum beatae aliquam nemo? Blanditiis tenetur tempore.
            </p>

            <div className="mid">
              <div className="quantity">
                <button className="minus" onClick={decreaseQuantity} disabled={quantity === 0}>
                  <img src="../assets/decrease.svg" alt="Decrease" width="26px" height="20px" />
                </button>
                <input value={quantity} type="text" disabled />
                <button className="plus" onClick={increaseQuantity} disabled={quantity === 10}>
                  <img src="../assets/increase.svg" alt="Increase" width="16px" height="20px" />
                </button>
              </div>
              <div className="total">${total}</div>
            </div>

            <div className="button-grp">
              <button className="details-buy">Buy Now</button>
              <button className="details-add-to-cart">Add to Cart</button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}

export default Card;
