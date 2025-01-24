import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Content from './Content'
import Header  from './Header'
import Footer from './Footer'

import {LuCirclePlus} from 'react-icons/lu'



function App() {
  const [newName , setNewName] = useState('')
  const [items , setItems] = useState([
    {
        id: 1,
        checked : false,
        item : 'bread sticks'
    },
    {
        id: 2,
        checked : false,
        item : 'hotdogs'
    },
    {
        id: 3,
        checked : true,
        item : 'toffies'
    }
  ])

  const checkCheck = (id) => {
        
    const listItems = items.map (
        (item) => item.id === id ? {...item , checked: !item.checked} : item
    )
    setItems(listItems)
    localStorage.setItem('shopping-list' , JSON.stringify(listItems))

}

  const handleDelete = (id) => {
      const listItems = items.filter (
          (item) => item.id !== id 
      )
      setItems(listItems)
      localStorage.setItem('shopping-list' , JSON.stringify(listItems))
  }

  


  const createItem = () => {
     document.querySelector('.form').style.visibility = 'visible';
    }

  function addName(e){
    e.preventDefault()
    document.querySelector('.form').style.visibility = 'hidden'
    if(newName.trim() !== '') {
      console.log(newName)


      setItems(listItems)
    }

  }

  const cancelPrompt = () => {
    document.querySelector('.form').style.visibility = 'hidden'
  }



  return (
    <>
    <div className="App">
      <Header title="Groceries List"></Header>
      <Content
        handleDelete = {handleDelete}
        checkCheck = {checkCheck}
        items = {items}  
      ></Content>

      <LuCirclePlus
        role='button' className='add-new-item' onClick={createItem}
      ></LuCirclePlus>

      <form onSubmit={addName} method="get" className='form'>
        <input type="text" className="grocery-new-name-textarea" value={newName} placeholder='Whats the item you want to add' onChange={(e) => setNewName(e.target.value)}>


        </input>
        <button type="submit">Submit</button>
        <button value='Cancel' onClick={cancelPrompt}>Cancel</button>
      </form>
      

      <Footer length={items.length}></Footer>

    </div>
      
    
      
      
    </>
  )
}

export default App
