import React, { useState } from 'react';
import Child from './Child';

const Parent = () => {
  const [count, setCount] = useState(0);

  const handleUpdate = () => {
    setCount(count => count + 1);
  };

  return (
    <div style={{ textAlign: 'center', margin: '20px' }}>
      <h1>Count from Parent: {count}</h1>
      <Child onUpdate={handleUpdate} />
    </div>
  );
};

export default Parent;
