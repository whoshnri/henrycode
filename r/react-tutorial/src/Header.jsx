
const Header = ({ title }) => {
    return(
        <header>
           <h2>{title}</h2>
        </header>


    )


}

// setting default props

Header.defaultProps = {
    title: 'Untitled list'
}

export default Header