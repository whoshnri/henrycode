
import ItemList from "./ItemList";



const Content = ({handleDelete , checkCheck , items }) => {


    return(
        <>
        {
            !(items.length === 0) ? 
            (                
                <ItemList 
                    items = {items}
                    handleDelete = {handleDelete}
                    checkCheck = {checkCheck}
                ></ItemList>
            ) : 
            (
                <h1 className="empty">
                    This list is empty
                </h1>
            )
        }
        
        
        
        </>
    )



}


export default Content