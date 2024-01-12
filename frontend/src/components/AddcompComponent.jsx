/**
 * v0 by Vercel.
 * @see https://v0.dev/t/0W13RkH
 */
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function AddcompComponent() {
    const navigate = useNavigate();
    
    const [compInfo, setCompInfo] = useState({
        compname: '',
        compdate: '',
        compvenue: ''
    });

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        setCompInfo((prevCompInfo) => ({
            ...prevCompInfo,
            [name]: type === 'checkbox' ? checked : value,
        }));
    };

    const handleSubmit = async () => {
        // Replace with your endpoint URL
        const endpoint = 'http://localhost:8501/add_competition';

        try {
            const response = await fetch(endpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(compInfo),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            // Process the response (optional)
            const data = await response.json();
            console.log(data);
            // Redirect to a different page after successful submission
        } catch (error) {
            console.error('Error posting data:', error);
        }
        navigate('/');
    };
 
    return (
        <div>
            <div className="bg-gradient-to-r from-[#0001c1] to-[#2193b0]">
                <nav className="flex items-center justify-between px-6 py-4">
                    <div className="flex items-center space-x-4">
                        <div className="hidden md:flex space-x-2">
                            <ArrowLeftButton
                            onClick={() => navigate('/')}
                            />
                        </div>
                    </div>
                </nav>
            </div>
            <section className="w-full py-12 md:py-24 lg:py-32 xl:py-48 bg-black">
                <div className="container px-4 md:px-6">
                    <div className="flex flex-col justify-center space-y-8 text-center">
                        <div className="space-y-1">
                            <h1 className="text-3xl font-bold tracking-tighter sm:text-5xl xl:text-6xl/none bg-clip-text text-transparent bg-gradient-to-r from-white to-gray-500">
                            Add Competition
                            </h1>
                        </div>
                        <input
                            className="m-2 p-2 bg-white hover:bg-white text-black font-bold py-2 px-4 rounded"
                            type="string"
                            name="compname"
                            placeholder="Competition Name"
                            value={compInfo.compname}
                            onChange={handleChange}
                        />
                        <input
                            className="m-2 p-2 bg-white hover:bg-white text-black font-bold py-2 px-4 rounded"
                            type="date"
                            name="compdate"
                            placeholder="Competition Date" // Placeholder text here
                            value={compInfo.compdate}
                            onChange={handleChange}
                        />
                        <input
                            className="m-2 p-2 bg-white hover:bg-white text-black font-bold py-2 px-4 rounded"
                            type="string"
                            name="compvenue"
                            placeholder="Competition Venue"
                            value={compInfo.compvenue}
                            onChange={handleChange}
                        />
                        <button
                            className="m-2 p-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                            onClick={handleSubmit}
                        >
                            Submit
                        </button>
                    </div>
                </div>
            </section>
        </div>
    );
}

function ArrowLeftButton(props) {
    // Your ArrowLeftIcon component
    const ArrowLeftIcon = (
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
        fill="none"
        stroke="white"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        <path d="m12 19-7-7 7-7" />
        <path d="M19 12H5" />
      </svg>
    );
  
    // Your click handler function
    const handleButtonClick = () => {
      // Add the action you want to perform here
      //navigate('/');
      // For example, you can navigate to a different page, toggle a state, etc.
    };
  
    return (
      <button onClick={handleButtonClick} {...props}>
        {ArrowLeftIcon}
      </button>
    );
}