import React, { useState } from 'react';
import FileUploadComponent from './DataInferenceConversion/FileUploadComponent';
import DataTableComponent from './DataInferenceConversion/DataTableComponent';
import './App.css';

// Defines the main component of the application
function App() {
  // State to control when data needs to be reloaded
  const [reloadData, setReloadData] = useState(false);

  // Function to trigger data reloading
  const handleDataReload = () => {
    setReloadData(true); // Sets reloadData to true, indicating data needs to be refreshed
  };

  // Renders the application UI
  return (
    <div className="app-container">
      <h1>Rhombus AI - Datasets Conversion</h1> {/* Application title */}
      <div className="components-container">
        {/* FileUploadComponent is passed a prop to notify when data processing is complete */}
        <FileUploadComponent onDataProcessed={handleDataReload} />
        {/* DataTableComponent receives props to control and respond to data reloading */}
        <DataTableComponent reloadData={reloadData} setReloadData={setReloadData} />
      </div>
    </div>
  );
}

export default App; // Exports the App component for use in other parts of the application
