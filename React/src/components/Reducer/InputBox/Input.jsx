import React, { useState } from "react";

const Input = () => {
  const [data, setData] = useState("");
  const [list, setList] = useState([]);
  const handleAdd = () => {
    setList([...list, data]);
    setData("");
  };
  return (
    <div>
      <input
        value={data}
        onChange={(e) => setData(e.target.value)}
        type="text"
      />
      <button onClick={handleAdd}>Click me to list</button>

      <h1>List : </h1>
        <ul>
            {list.map((l, index) => (
               <li key={index} > {l}</li> 
            ))}
        </ul>
    </div>
  );
};

export default Input;
