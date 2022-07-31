import React from "react";
const PlayVideo = ({ closeVideo }) => {
  return (
    <div
      style={{
        // background: "pink",
        // opacity: 0.8,
        minWidth: "75vw",
        minHeight: "60vh",
        position: "absolute",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        // flexDirection: "column",
      }}
    >
      <div style={{ overflow: "clip" }}>
        <div
          onClick={closeVideo}
          style={{
            position: "absolute",
            right: 0,
            top: 0,
            borderStyle: "solid",
            borderColor: "red",
            borderRadius: 100,
            height: 20,
            color: "red",
            width: 20,
            alignItems: "center",
            display: "flex",
            background: "#fff",
            justifyContent: "center",
          }}
        >
          <p>X</p>
        </div>
        <video width="100%" height="100%" controls>
          <source
            src="https://www.w3schools.com/tags/movie.ogg"
            type="video/mp4"
          />
        </video>
      </div>
    </div>
  );
};

export default PlayVideo;
