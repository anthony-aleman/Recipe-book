import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios';


function App() {
  const [getMessage, setGetMessage] = useState({})

  useEffect(() => {
    
    /*ONCE BACKEND IS DEPLOYED REMEMBER TO CHANGE API GET URL*/
    axios.get('http://localhost:5000/recipes').then(res => {
      setGetMessage(res)
    }).catch(err => 
      console.log(err))
  }, [])



  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>React frontend and Flask backend</p>
        {/*BASICALLY MEANS IF SERVER RESPONSE == 200 THEN DISPLAY DATA, OTHERWISE DISPLAY LOADING */}
        <div>{getMessage.status === 200 ? <h3>{getMessage.data.foo}</h3> :<h3>LOADING</h3>}</div>
      </header>
    </div>
  );
}

export default App;
