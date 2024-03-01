import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { decrement, increment, selectCount } from './counterSlice';

export function Counter() {
    const dispatch = useDispatch()
    const count = useSelector(selectCount)

    return (
        <div>
            <button onClick={() => dispatch(increment())}>Increment</button>
            <button onClick={() => dispatch(decrement())}>Decrement</button>
        Current count: <span>{count}</span>
        </div>
    )
}