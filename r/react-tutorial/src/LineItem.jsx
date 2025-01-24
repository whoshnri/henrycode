import React from 'react'
import {CiTrash} from 'react-icons/ci'

const LineItem = ({item , checkCheck , handleDelete}) => {
  return (
        <li className="item">
            <input type="checkbox" checked={
                item.checked} onChange={() => checkCheck(item.id)
                }/>
            <label
                style={
                    (item.checked) ? {textDecoration : 'line-through'} : null
                }
                onDoubleClick={() => checkCheck(item.id)}
            >
                {item.item}
            </label>
            <CiTrash
                onClick={() => handleDelete(item.id)}
                role="button" 
                tabIndex='0'
            />
                                    
        </li>
  )
}

export default LineItem
