import React from 'react';

const Child = ({ onUpdate }) => {
  const style = {
    backgroundColor: '#ebf8ff',
    padding: '16px',
    border: '1px solid #90cdf4',
    borderRadius: '8px',
    textAlign: 'center',
  };

  return (
    <div style={style}>
      <p>Child Component</p>
      <button onClick={onUpdate} style={{ marginTop: '10px', padding: '8px 12px', cursor: 'pointer' }}>
        Click me to update
      </button>
    </div>
  );
};

export default Child;
