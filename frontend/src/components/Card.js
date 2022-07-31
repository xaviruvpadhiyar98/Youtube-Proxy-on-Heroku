import React from "react";
const Card = ({ data, playVideo }) => {
  return (
    <div
      onClick={playVideo}
      className="card"
      style={{ maxHeight: 400, maxWidth: 300 }}
    >
      <div className="card-image">
        <img src={data.thumbnail} alt="thumbnail" />
        <span
          style={{ color: "#222233", fontWeight: "bold" }}
          className="card-title"
        >
          {data.title}
        </span>
      </div>
      <div
        style={{ background: "#666699", color: "#aaccff" }}
        className="card-content"
      >
        <p>{data.dec}</p>
      </div>
    </div>
  );
};

export default Card;
