import { Outlet } from 'react-router-dom';
import './App.css';
import NavBar from './NavBar/navbar';

function App() {
  return (
    <>
      <NavBar />
      <main className='pageBase'>
        <Outlet/>
      </main>
    </>
  );
}

export default App;