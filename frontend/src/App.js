import React, { useState } from 'react';
import './App.css';

function App() {
  const [topic, setTopic] = useState('');
  const [details, setDetails] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const topicMaxLength = 100;
  const detailsMaxLength = 500;

  const handleTopicChange = (e) => {
    setTopic(e.target.value.slice(0, topicMaxLength));
  };

  const handleDetailsChange = (e) => {
    setDetails(e.target.value.slice(0, detailsMaxLength));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true); // Start loading
    try {
      const response = await fetch('http://localhost:8000/create_video/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ topic, details })
      });
      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error('Failed to create video:', error);
    }
    setIsLoading(false); // Stop loading after the request is finished
  };

  return (
    <div className="App">
      <div className="App-header">
        <h1>tubeAI</h1>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={topic}
            onChange={handleTopicChange}
            placeholder="Enter Video Topic"
            maxLength={topicMaxLength}
          />
          <div className="character-count">
            {topic.length} / {topicMaxLength}
          </div>
          <textarea
            value={details}
            onChange={handleDetailsChange}
            placeholder="Enter Video Details"
            maxLength={detailsMaxLength}
          />
          <div className="character-count">
            {details.length} / {detailsMaxLength}
          </div>
          <button type="submit" disabled={isLoading}>
            {isLoading ? 'Loading...' : 'Start'}
          </button>
        </form>
      </div>
    </div>
  );
}

export default App;
