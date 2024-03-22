import React, { useState, useEffect } from 'react';
import './DataTableComponent.css';

function DataTableComponent({ reloadData, setReloadData }) {
  // Initializes state to hold column data
  const [columns, setColumns] = useState([]);

  useEffect(() => {
    // Checks if data needs to be reloaded
    if (!reloadData) return;

    // Fetches data from the server
    fetch('http://localhost:8000/myapp/process-csv/')
      .then(response => {
        if (!response.ok) {
          // Throws error if response is not ok
          throw new Error('Network response was not ok');
        }
        // Parses JSON response
        return response.json();
      })
      .then(data => {
        // Updates columns state with new data
        console.log(data); // Logs data for debugging
        setColumns(data.columns);
        setReloadData(false); // Resets reload state in parent component
      })
      .catch(error => {
        // Catches and logs any errors during fetching
        console.error('Error fetching data:', error);
      });

    // Effect dependency on reloadData to trigger re-fetching
  }, [reloadData, setReloadData]);

  // Displays a message if there is no data to display
  if (columns.length === 0) {
    return <div className="no-data-table">Loading data or no data available...</div>;
  }

  // Renders the data table with column names and data types
  return (
    <div className="data-table-container">
      <h2>Results</h2>
      <table>
        <thead>
          <tr>
            <th>Column Name</th>
            <th>Data Type</th>
          </tr>
        </thead>
        <tbody>
          {columns.map((column, index) => (
            // Maps each column to a row in the table
            <tr key={index}>
              <td>{column.columnName}</td>
              <td>{column.dataType}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default DataTableComponent;
