/**
 * v0 by Vercel.
 * @see https://v0.dev/t/0W13RkH
 */
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function AddeventComponent() {
    const navigate = useNavigate();
    const mylst = ['Home', 'newpage', 'thing', 'anotherThing', 'temp', 'temp2', 'jadalada'];
    
    const [eventInfo, setEventInfo] = useState({
        eventNumber: '',
        eventName: '',
        distance: '',
        gender: '',
        maxAge: '',
        qualifyingTime: '',
        isRelay: false,
    });

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        setEventInfo((prevEventInfo) => ({
            ...prevEventInfo,
            [name]: type === 'checkbox' ? checked : value,
        }));
    };

    const handleSubmit = async () => {
        // Replace with your endpoint URL
        const endpoint = 'https://your-endpoint.com/post';

        try {
            const response = await fetch(endpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(eventInfo),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            // Process the response (optional)
            const data = await response.json();
            console.log(data);
            // Redirect to a different page after successful submission
            navigate('/success');
        } catch (error) {
            console.error('Error posting data:', error);
        }
    };

    return (
        <section className="w-full py-12 md:py-24 lg:py-32 xl:py-48 bg-black">
            <div className="container px-4 md:px-6">
                <div className="flex flex-col justify-center space-y-8 text-center">
                    <div className="space-y-2">
                        <h1 className="text-3xl font-bold tracking-tighter sm:text-5xl xl:text-6xl/none bg-clip-text text-transparent bg-gradient-to-r from-white to-gray-500">
                        Add Events
                        </h1>
                    </div>
                    <input
                        className="m-2 p-2 bg-white hover:bg-white text-black font-bold py-2 px-4 rounded"
                        type="int"
                        name="eventNumber"
                        placeholder="Event Number"
                        value={eventInfo.eventNumber}
                        onChange={handleChange}
                    />
                    <input
                        className="m-2 p-2 bg-white hover:bg-white text-black font-bold py-2 px-4 rounded"
                        type="text"
                        name="eventName"
                        placeholder="Event Name"
                        value={eventInfo.eventName}
                        onChange={handleChange}
                    />
                    <input
                        className="m-2 p-2 bg-white hover:bg-white text-black font-bold py-2 px-4 rounded"
                        type="int"
                        name="distance"
                        placeholder="Distance"
                        value={eventInfo.distance}
                        onChange={handleChange}
                    />
                    <input
                        className="m-2 p-2 bg-white hover:bg-white text-black font-bold py-2 px-4 rounded"
                        type="text"
                        name="gender"
                        placeholder="Gender"
                        value={eventInfo.gender}
                        onChange={handleChange}
                    />
                    <input
                        className="m-2 p-2 bg-white hover:bg-white text-black font-bold py-2 px-4 rounded"
                        type="int"
                        name="maxAge"
                        placeholder="Max Age"
                        value={eventInfo.maxAge}
                        onChange={handleChange}
                    />
                    <input
                        className="m-2 p-2 bg-white hover:bg-white text-black font-bold py-2 px-4 rounded"
                        type="text"
                        name="qualifyingTime"
                        placeholder="Qualification Time"
                        value={eventInfo.qualifyingTime}
                        onChange={handleChange}
                    />
                    <label className='text-white'>
                        <input
                            type="checkbox"
                            name="isRelay"
                            placeholder="Relay"
                            value={eventInfo.isRelay}
                            onChange={handleChange}
                        />
                        Relay
                    </label>
                    {/* Other input fields with similar structure */}
                    <button
                        className="m-2 p-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                        onClick={handleSubmit}
                    >
                        Submit
                    </button>
                </div>
            </div>
        </section>
    );
}