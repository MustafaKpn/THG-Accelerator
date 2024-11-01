import { useState, useEffect } from "react";
import "./App.css";
import Cell from "./components/cell";
import words from "./components/wordsList.json";
import clickSound from "./components/clickSound.wav";
import winSound from "./components/winSound.mp3";
import wrongSound from "./components/wrong.mp3";

const wordToGuess = words[Math.floor(Math.random() * words.length)];
function App() {
  const letters = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
  ];

  const btnStyles = [
    {
      backgroundColor: "lightgray",
      color: "black",
      padding: "10px",
      border: "1px solid black",
    },
    {
      backgroundColor: "yellow",
      color: "black",
      padding: "10px",
      border: "1px solid black",
    },
    {
      backgroundColor: "green",
      color: "black",
      padding: "10px",
      border: "1px solid black",
    },
  ];

  const [cellContent, setCellContent] = useState([
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""],
  ]);

  const [rowStyling, setRowStyling] = useState(
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
  );

  const playTypingSound = () => {
    const audio = new Audio(clickSound);
    audio.play();
  };

  const playWinSound = () => {
    const audio = new Audio(winSound);
    audio.play();
  };

  const playWrongSound = () => {
    const audio = new Audio(wrongSound);
    audio.play();
  };

  console.log(wordToGuess);
  const rows = ["a", "b", "c", "d", "e"];
  const [currentRow, setCurrentRow] = useState("a");
  const [cellIndex, setCellIndex] = useState(0);
  const [cellValues, setCellValues] = useState(["", "", "", "", ""]);
  const [word, setWord] = useState("");
  const [rowIndex, setRowIndex] = useState(1);

  const updateItemAtIndex = (index, newItem) => {
    setCellValues((prevItems) =>
      prevItems.map((item, i) => (i === index ? newItem : item))
    );
  };

  const setCell = (btn) => {
    if (word !== wordToGuess) {
      const indexToUpdate = cellIndex; // Specify the index you want to update (e.g., the second item)
      const newItem = btn.target.value; // Specify the new item
      updateItemAtIndex(indexToUpdate, newItem); // Update the item at the specific index
      setCellIndex(cellIndex + 1);
      if (word.length < 5) {
        setWord((prevWord) => prevWord + btn.target.value);
      }
      playTypingSound();
    }
  };

  useEffect(() => {
    console.log(word); // This will log the updated word whenever it changes
  }, [word]);

  const deleteLetters = () => {
    if (word !== wordToGuess) {
      setWord((prevWord) => "");
      setCellIndex(0);
      setCellValues(["", "", "", "", ""]);
    }
  };

  function check() {
    const wordLength = word.length;

    if (word === wordToGuess) {
      setRowStyling((prevStyling) =>
        prevStyling.map((rowStyle, index) =>
          index === rowIndex - 1 ? [2, 2, 2, 2, 2] : rowStyle
        )
      );
      playWinSound();
    } else if (word !== wordToGuess && wordLength === 5) {
      const { newCellValues, stylingBits } = compareStrings(word, wordToGuess);
      setRowIndex((rowIndex) => rowIndex + 1);
      setCellContent((prevContent) =>
        prevContent.map((row, index) =>
          index === rowIndex - 1 ? newCellValues : row
        )
      );

      setRowStyling((prevStyling) =>
        prevStyling.map((rowStyle, index) =>
          index === rowIndex - 1 ? stylingBits : rowStyle
        )
      );

      setCurrentRow(rows[rowIndex]);
      setWord("");
      setCellIndex(0);
      console.log(stylingBits);
      setCellValues(["", "", "", "", ""]);
      playWrongSound();
    }
  }

  console.log(rowStyling);
  function compareStrings(string1, string2) {
    const newCellValues = [];
    const stylingBits = [];

    let string2Array = string2.split("");

    for (let i = 0; i < string1.length; i++) {
      newCellValues.push(string1[i]);

      if (string1[i] === string2Array[i]) {
        stylingBits.push(2);
        string2Array[i] = "0"; // This is to solve the problem of duplicates
      } else if (string2Array.includes(string1[i])) {
        stylingBits.push(1);
      } else {
        stylingBits.push(0);
      }
    }

    return { newCellValues, stylingBits };
  }

  return (
    <>
      <h1>Wordle</h1>
      <div className="grid">
        <Cell
          row="a"
          content={currentRow === "a" ? cellValues : cellContent[0]}
          buttonsStyles={btnStyles}
          stylingBits={rowStyling[0]}
        />
        <Cell
          row="b"
          content={currentRow === "b" ? cellValues : cellContent[1]}
          buttonsStyles={btnStyles}
          stylingBits={rowStyling[1]}
        />
        <Cell
          row="c"
          content={currentRow === "c" ? cellValues : cellContent[2]}
          buttonsStyles={btnStyles}
          stylingBits={rowStyling[2]}
        />
        <Cell
          row="d"
          content={currentRow === "d" ? cellValues : cellContent[3]}
          buttonsStyles={btnStyles}
          stylingBits={rowStyling[3]}
        />
        <Cell
          row="e"
          content={currentRow === "e" ? cellValues : cellContent[4]}
          buttonsStyles={btnStyles}
          stylingBits={rowStyling[4]}
        />
      </div>

      <h3>Keyboard</h3>
      <div className="keyboard">
        {letters.map((letter) => (
          <button
            key={letter}
            className="letter"
            value={letter}
            onClick={setCell}
          >
            {letter}
          </button>
        ))}
        <button key="del" className="delButton letter" onClick={deleteLetters}>
          Del
        </button>
        <button key="Enter" className="enterButton letter" onClick={check}>
          Enter
        </button>
      </div>
    </>
  );
}

export default App;
