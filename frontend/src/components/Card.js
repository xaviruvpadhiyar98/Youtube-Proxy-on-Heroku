import React from "react";
const Card = ({ data, playVideo }) => {
  return (
    <div
      onClick={playVideo}
      className="card"
      style={{ maxHeight: 400, maxWidth: 300 }}
    >
      <div className="card-image">
        <img src={data.thumbnails[0]["url"]} alt="thumbnail" />
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
      </div>
    </div>
  );
};

export default Card;
