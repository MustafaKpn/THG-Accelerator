import "./Cell.css";

function Cell({ row, content, buttonsStyles, stylingBits }) {
  const firstButtonStyle = buttonsStyles[stylingBits[0]] || {};
  const secondButtonStyle = buttonsStyles[stylingBits[1]] || {};
  const thirdButtonStyle = buttonsStyles[stylingBits[2]] || {};
  const fourthButtonStyle = buttonsStyles[stylingBits[3]] || {};
  const fifthtButtonStyle = buttonsStyles[stylingBits[4]] || {};
  return (
    <>
      <div className="cells">
        <button
          className="unit"
          id={row + 1}
          value={content[0]}
          style={firstButtonStyle}
        >
          {content[0]}
        </button>
        <button
          className="unit"
          id={row + 2}
          value={content[1]}
          style={secondButtonStyle}
        >
          {content[1]}
        </button>
        <button
          className="unit"
          id={row + 3}
          value={content[2]}
          style={thirdButtonStyle}
        >
          {content[2]}
        </button>
        <button
          className="unit"
          id={row + 4}
          value={content[3]}
          style={fourthButtonStyle}
        >
          {content[3]}
        </button>
        <button
          className="unit"
          id={row + 5}
          value={content[4]}
          style={fifthtButtonStyle}
        >
          {content[4]}
        </button>
      </div>
    </>
  );
}

export default Cell;
