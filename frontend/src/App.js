import React, { useState } from 'react';
import './App.css';

function App() {
  const [word, setWord] = useState('');
  const [nuLevel, setNuLevel] = useState(3);
  const [sizeOfLevel, setSizeOfLevel] = useState(12);
  const [percentageOfCandidates, setPercentageOfCandidates] = useState(0.5);
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState([]);
  const [sortBy, setSortBy] = useState(null);
  const [sortDirection, setSortDirection] = useState(null);
  const [currentPage, setCurrentPage] = useState(1);

  const handleGenerate = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:8000/generate-password/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          base_password: word,
          num_levels: nuLevel,
          size_of_level: sizeOfLevel,
          percentage_of_candidates: percentageOfCandidates,
        }),
      });
      const data = await response.json();
      if (data.password_set && data.password_set.length > 0) {
        setResults(data.password_set);
      } else {
        setResults([]);
        alert('No passwords found. Please try again with different parameters.');
      }
    } catch (error) {
      console.error('Error fetching data:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleChangeSortBy = (key) => {
    if (sortBy === key) {
      setSortDirection(sortDirection === 'asc' ? 'desc' : 'asc');
    } else {
      setSortBy(key);
      setSortDirection('asc');
    }
  };

  const sortedResults = [...results].sort((a, b) => {
    if (sortBy === 'difference_metric') {
      return sortDirection === 'asc' ? a.difference_metric - b.difference_metric : b.difference_metric - a.difference_metric;
    }
    if (sortBy === 'strength_metric') {
      return sortDirection === 'asc' ? a.strength_metric - b.strength_metric : b.strength_metric - a.strength_metric;
    }
    if (sortBy === 'password_value') {
      return sortDirection === 'asc' ? a.password_value - b.password_value : b.password_value - a.password_value;
    }
    return 0;
  });

  const resultsPerPage = 20;
  const indexOfLastResult = currentPage * resultsPerPage;
  const indexOfFirstResult = indexOfLastResult - resultsPerPage;
  const currentResults = sortedResults.slice(indexOfFirstResult, indexOfLastResult);

  const paginate = (pageNumber) => setCurrentPage(pageNumber);

  return (
    <div className="App">
      <h1>Password Generator</h1>
      <div className="input-container">
        <label htmlFor="wordInput">Word:</label>
        <input id="wordInput" type="text" value={word} onChange={(e) => setWord(e.target.value)} />
      </div>
      <div className="input-container">
        <label>Number of Level:</label>
        <input type="range" min={2} max={7} value={nuLevel} onChange={(e) => setNuLevel(e.target.value)} />
        <span>{nuLevel}</span>
      </div>
      <div className="input-container">
        <label>Size of Level:</label>
        <input type="range" min={5} max={25} value={sizeOfLevel} onChange={(e) => setSizeOfLevel(e.target.value)} />
        <span>{sizeOfLevel}</span>
      </div>
      <div className="input-container">
        <label>Percentage of Candidates:</label>
        <input type="range" min={0.2} max={0.8} step={0.1} value={percentageOfCandidates} onChange={(e) => setPercentageOfCandidates(e.target.value)} />
        <span>{percentageOfCandidates}</span>
      </div>
      <button onClick={handleGenerate} disabled={loading || !word}>Generate</button>
      <div>
        {loading && <p className="loading">Loading...</p>}
        {!loading && results.length > 0 && (
          <div>
            <button onClick={() => handleChangeSortBy('difference_metric')} className={sortBy === 'difference_metric' ? `active ${sortDirection}` : ''}>Sort by Difference Metric</button>
            <button onClick={() => handleChangeSortBy('strength_metric')} className={sortBy === 'strength_metric' ? `active ${sortDirection}` : ''}>Sort by Strength Metric</button>
            <button onClick={() => handleChangeSortBy('password_value')} className={sortBy === 'password_value' ? `active ${sortDirection}` : ''}>Sort by Password Value</button>
            <table>
              <thead>
                <tr>
                  <th>Word</th>
                  <th>Difference Level</th>
                  <th>Strength Level</th>
                  <th>Percentage</th>
                </tr>
              </thead>
              <tbody>
                {currentResults.map((result, index) => (
                  <tr key={index}>
                    <td>{result.password}</td>
                    <td>{result.difference_metric}</td>
                    <td>{result.strength_metric}</td>
                    <td>{result.password_value.toFixed(2)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
            <Pagination
              resultsPerPage={resultsPerPage}
              totalResults={results.length}
              paginate={paginate}
              currentPage={currentPage}
            />
          </div>
        )}
      </div>
    </div>
  );
}

const Pagination = ({ resultsPerPage, totalResults, paginate, currentPage }) => {
  const pageNumbers = [];

  for (let i = 1; i <= Math.ceil(totalResults / resultsPerPage); i++) {
    pageNumbers.push(i);
  }

  let visiblePageNumbers = pageNumbers;
  if (pageNumbers.length > 5) {
    visiblePageNumbers = currentPage <= 3 ? pageNumbers.slice(0, 5) : currentPage >= pageNumbers.length - 2 ? pageNumbers.slice(-5) : pageNumbers.slice(currentPage - 3, currentPage + 2);
  }

  const handlePageClick = (e, pageNumber) => {
    e.preventDefault();
    paginate(pageNumber);
  };

  return (
    <nav>
      <ul className="pagination">
        <li className="page-item">
          <a onClick={(e) => handlePageClick(e, 1)} href="#" className="page-link">
            First
          </a>
        </li>
        {currentPage > 3 && pageNumbers.length > 5 && (
          <li className="ellipsis">...</li>
        )}
        {visiblePageNumbers.map(number => (
          <li key={number} className={currentPage === number ? 'page-item active' : 'page-item'}>
            <a onClick={(e) => handlePageClick(e, number)} href="#" className="page-link">
              {number}
            </a>
          </li>
        ))}
        {currentPage < pageNumbers.length - 2 && pageNumbers.length > 5 && (
          <li className="ellipsis">...</li>
        )}
        <li className="page-item">
          <a onClick={(e) => handlePageClick(e, pageNumbers.length)} href="#" className="page-link">
            Last
          </a>
        </li>
      </ul>
    </nav>
  );
};


export default App;
