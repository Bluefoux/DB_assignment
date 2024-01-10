import { useNavigate } from 'react-router-dom';
import { useEffect } from 'react';
import axios from 'axios';
import AddeventComponent from '../components/AddeventComponent';

import '../index.css';

function AddEvent() {
    const navigate = useNavigate();
    
    return (
        <div>
            <AddeventComponent />
        </div>
    );
}

export default AddEvent;