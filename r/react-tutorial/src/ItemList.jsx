import React from 'react'
import LineItem from './LineItem'

const ItemList = ({handleDelete , checkCheck , items }) => {
  return (
    <>
        <ul>
                    {
                         items.map
                        (
                            (item) => 
                            (
                                <LineItem
                                key={item.id}
                                    handleDelete = {handleDelete}
                                    item = {item}
                                    checkCheck = {checkCheck}
                                ></LineItem>
                            )
                        )
                    }
                </ul>

    
    
    </>
  )
}

export default ItemList
