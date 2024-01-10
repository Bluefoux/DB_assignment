import { useNavigate } from 'react-router-dom';
import { useEffect } from 'react';
import axios from 'axios';
import EventComponent from '../components/EventComponent';

import '../index.css';


function Event() {
    const navigate = useNavigate();
    
    return (
        <div>
            <EventComponent />
        </div>
    );
}

export default Event;