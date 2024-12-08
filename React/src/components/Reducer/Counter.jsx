import  { useState, useReducer } from "react"

const reducer = (state, action) => {
    switch (action.type){
        case 'increment':
            return { count : state.count + 1}
        case 'decrement' :
            return {count : state.count - 1}
        default:
            return state
    }
}

const Counter = () => {
    const [state, dispatch] = useReducer(reducer, {count : 0})

    return (
        <>
        hey
        <h2>Count : {state.count}</h2>
        <button onClick={() => dispatch({type : 'increment'})}>Plus</button>
        <button onClick={() => dispatch({type : 'decrement'})}>Minus</button>
        </>
    )
}

export default Counter