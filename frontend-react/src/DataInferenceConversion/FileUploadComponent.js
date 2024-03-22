import React, { useState, useRef } from 'react';
import './FileUploadComponent.css';

function FileUploadComponent({ onDataProcessed }) {
    // State to hold the selected file
    const [selectedFile, setSelectedFile] = useState(null);
    // Reference to the file input for resetting it later
    const fileInputRef = useRef(null);

    // Updates state when a file is selected
    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
    };

    // Handles the file upload process
    const handleFileUpload = async (event) => {
        event.preventDefault(); // Prevents form from submitting traditionally
        if (!selectedFile) {
            alert('Please select a file first.'); // Alerts if no file is selected
            return;
        }

        const formData = new FormData(); // Creates a FormData object for the file
        formData.append('file', selectedFile); // Appends the selected file to the FormData object

        // Retrieves the CSRF token from cookies
        const csrftoken = document.cookie
            .split('; ')
            .find(row => row.startsWith('csrftoken='))
            ?.split('=')[1];

        try {
            // Makes a POST request to the backend with the FormData
            const response = await fetch('http://localhost:8000/myapp/process-csv/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken, // Includes the CSRF token in the request header
                },
                body: formData,
                credentials: 'include', // Ensures cookies are sent with the request
            });

            // Handles non-OK responses
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            } else {
                // Parses the response data as JSON
                const data = await response.json();
                console.log(data); // Logs the response data for debugging
                alert('File processed successfully. Check the console for the data.');
                onDataProcessed(); // Notifies the parent component that data has been processed
                setSelectedFile(null); // Resets the selected file state
                fileInputRef.current.value = ""; // Clears the file input
            }
        } catch (error) {
            console.error('Error uploading file:', error); // Logs any errors during the upload process
            alert('Failed to process file.'); // Alerts if the file processing fails
        }
    };

    // Renders the file upload form
    return (
        <div className="file-upload-container">
            <h2>File Upload</h2>
            <form onSubmit={handleFileUpload}>
                <input type="file" name="file" ref={fileInputRef} onChange={handleFileChange} />
                <button type="submit">Upload</button>
            </form>
        </div>
    );
}

export default FileUploadComponent;
