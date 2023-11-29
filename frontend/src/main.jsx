import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home'
import AddCompetition from './pages/AddCompetition'
import Event from './pages/Events'
import AddEvent from './pages/AddEvent'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
      <BrowserRouter>
          <Routes>
              <Route
                  path="/"
                  element={<Home />}
              />
              <Route
                  path="/Add_Competition"
                  element={<AddCompetition />}
              />
              <Route
                  path="/Events"
                  element={<Event />}
              />
              <Route
                  path="/Add_Event"
                  element={<AddEvent />}
              />
          </Routes>
      </BrowserRouter>
  </React.StrictMode>
);
