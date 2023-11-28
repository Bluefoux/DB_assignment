import { useNavigate } from 'react-router-dom';
import { useEffect } from 'react';
import axios from 'axios';
import AddcompComponent from '../components/AddcompComponent';

import '../index.css';

function AddCompetition() {
    const navigate = useNavigate();
    
    return (
        <div>
            <AddcompComponent />
        </div>
    );
}

export default AddCompetition;