/**
 * v0 by Vercel.
 * @see https://v0.dev/t/0W13RkH
 */
// useEffect
import React from 'react';
import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

export default function HomeComponent() {
  const navigate = useNavigate();
  // const mylst = ['Home', 'newpage', 'thing', 'anotherThing', 'temp', 'temp2', 'jadalada'];
  // const [compinfo , setCompinfo] = useState([{
  //   compid: '',
  //   compname: '',
  //   compdate: '',
  //   complocation: ''
  // }]);
  const compinfo = [];
  const myid = [1, 2, 3, 4, 5, 6, 7];
  const [showCompetitions, setShowCompetitions] = useState(true);
  const [showAddEvent, setShowAddEvent] = useState(true);
  const [valueOfCompetition, setValueOfCompetition] = useState('');
  const [eventInfo, setEventInfo] = useState({
    eventNumber: '',
    eventName: '',
    distance: '',
    gender: '',
    maxAge: '',
    qualifyingTime: '',
    isRelay: false,
    comp_id: ''
  });
  let content = null;

  useEffect(() => {
    const fetchMessages = async () => {
      try {
                  const response = await fetch('http://localhost:8501/get_competitions');
                  if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
                  }
                  const data = await response.json();
                  setCompinfo(data);
                  setStatusMessage(data.Messages);
                  console.log(data.Messages);
              } catch (error) {
                  console.error('Failed to fetch messages:', error);
              }
          };
  
          fetchMessages();
    //handleClick(1);
      }, []);

  const handleChange = (thing) => {
    const { name, value, type, checked } = thing.target;
    const newValue = type === 'checkbox' ? checked : value;

    setEventInfo({
      ...eventInfo,
      [name]: newValue,
    });
  };

  const handleSubmit = async () => {
    const endpoint = 'http://localhost:8501/add_event';
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
            navigate('/');
        } catch (error) {
            console.error('Error posting data:', error);
        }
    console.log(eventInfo);
    setShowAddEvent(false)
    setShowCompetitions(true)
  };

  const handleClick = async (buttonValue, value) => {
    // Replace with your endpoint URL
    // const endpoint = 'http://localhost:5173/GetEvents';

    // try {
    //   const response = await fetch(endpoint, {
    //     method: 'POST',
    //     headers: {
    //       'Content-Type': 'application/json',
    //     },
    //     body: JSON.stringify({ buttonValue }),
    //   });

    //   if (!response.ok) {
    //     throw new Error(`HTTP error! status: ${response.status}`);
    //   }

    //   // Process the response (optional)
    //   const data = await response.json();
    console.log(value);
    setValueOfCompetition(value)
    setShowCompetitions(false)
    // } catch (error) {
    //   console.error('Error posting data:', error);
    // }
  };

  const handleClickevent = async (value) => {
    setEventInfo({comp_id: value})
    console.log(value);
    setShowAddEvent(false)
    setShowCompetitions(false)
  };

    if (showCompetitions){
      content = (
      <section className="w-full py-12 md:py-24 lg:py-32 xl:py-48 bg-black">
        <div className="container px-4 md:px-6">
          <div className="flex flex-col justify-center space-y-8 text-center">
            <div className="space-y-2">
            <h1 className="text-3xl font-bold tracking-tighter sm:text-5xl xl:text-6xl/none bg-clip-text text-transparent bg-gradient-to-r from-white to-gray-500">
              Competitions
            </h1>
            </div>
            {compinfo.map((item, index) => (
              <button
                key={index}
                className="m-2 p-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                onClick={() => handleClick(item, myid[index])}
              >
                {item}
              </button>
            ))}
            <button className="m-2 p-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
              //onClick={window.location('/Add_Competition')}
              onClick={() => navigate('/Add_Competition')}
            >
              Add Competition
            </button>
          </div>
        </div>
            </section>
      );
    } else if (showAddEvent && !showCompetitions) {
      content = (
        <section className="w-full py-12 md:py-24 lg:py-32 xl:py-48 bg-black">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col justify-center space-y-8 text-center">
              <div className="space-y-2">
              <h1 className="text-3xl font-bold tracking-tighter sm:text-5xl xl:text-6xl/none bg-clip-text text-transparent bg-gradient-to-r from-white to-gray-500">
                  Event
              </h1>
              </div>
              {compinfo.map((item) => (
              <h1 className="text-2xl font-bold tracking-tighter sm:text-2xl xl:text-2xl/none bg-clip-text text-transparent text-white">
                  {item}
              </h1>
              ))}
              <button
                className="m-2 p-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                onClick={() => handleClickevent(valueOfCompetition)}
              >
                Add Event
              </button>
            </div>
          </div>
        </section>
      );
    } else {
      content = (
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
    return <>{content}</>;
}