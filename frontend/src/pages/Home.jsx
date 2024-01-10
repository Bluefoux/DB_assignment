import { useNavigate } from 'react-router-dom';
import { useEffect } from 'react';
import axios from 'axios';
import HomeComponent from '../components/HomeComponent';

import '../index.css';

function Home() {
    const navigate = useNavigate();
    
    return (
        <div>
            <HomeComponent />
        </div>
    );
}

export default Home;