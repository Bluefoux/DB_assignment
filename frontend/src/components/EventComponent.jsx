/**
 * v0 by Vercel.
 * @see https://v0.dev/t/0W13RkH
 */
import React from 'react';
import { useNavigate } from 'react-router-dom';

export default function EventComponent() {
    const navigate = useNavigate();
    const mylst = ['Home', 'newpage', 'thing', 'anotherThing', 'temp', 'temp2', 'jadalada'];

    const handleClickevent = async (buttonValue) => {
    // Replace with your endpoint URL
    const endpoint = 'https://your-endpoint.com/post';

    try {
        const response = await fetch(endpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ buttonValue }),
        });

        if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
        }

      // Process the response (optional)
        const data = await response.json();
        console.log(data);
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
                    Event
                </h1>
                </div>
                {mylst.map((item, index) => (
                <button
                    key={index}
                    className="m-2 p-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                    onClick={() => handleClickevent(item)}
                >
                    {item}
                </button>
                ))}
                <button className="m-2 p-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                    //onClick={window.location('/Add_Competition')}
                    onClick={() => navigate('/Add_event')}
                >
                    Add Event
                </button>
            </div>
        </div>
    </section>
    );
}