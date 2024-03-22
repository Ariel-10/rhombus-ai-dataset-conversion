from django.http import JsonResponse
from .models import ProcessedData 
from .utils.data_processing import process_file  
from django.views.decorators.csrf import csrf_exempt  
import tempfile
import os 

@csrf_exempt  # Disable CSRF token requirement for this view; useful for testing
def process_csv_view(request):
    if request.method == "POST":
        file = request.FILES.get('file')  # Retrieve the uploaded file from the request
        if not file:
            return JsonResponse({"error": "No file provided."}, status=400)  # Error if no file found
        
        try:
            temp_dir = tempfile.gettempdir()  # Get the system's temporary directory
            temp_file_name = next(tempfile._get_candidate_names())  # Generate a unique temp file name
            temp_file_path = os.path.join(temp_dir, temp_file_name)  # Construct the full temp file path

            with open(temp_file_path, 'wb+') as temp_file:  # Open the temp file for writing
                for chunk in file.chunks():  # Write uploaded file's chunks to the temp file
                    temp_file.write(chunk)
            
            processed_df = process_file(temp_file_path)  # Process the file with Pandas
            if processed_df is None:
                return JsonResponse({"error": "Failed to process file."}, status=500)  # Error if processing fails
            
            # Save processed data to the database
            ProcessedData.objects.all().delete()  # Optional: clear previous data
            for col in processed_df.columns:  # Loop through columns and save their names and data types
                ProcessedData.objects.create(columnName=col, dataType=str(processed_df[col].dtype))
            
            os.remove(temp_file_path)  # Clean up by removing the temp file
            return JsonResponse({"success": "Data processed and saved successfully."})  # Success response
        
        except Exception as e:  # Catch and report any errors during processing
            print(f"Error handling file: {e}")
            return JsonResponse({"error": "An error occurred handling the uploaded file."}, status=500)
    elif request.method == "GET":
        # Fetch and return the last processed data from the database
        data_list = list(ProcessedData.objects.values())  # Convert QuerySet to list for JSON serialization
        return JsonResponse({"columns": data_list})  # Return processed data
    else:
        return JsonResponse({"error": "Method not allowed."}, status=405)  # Error for unsupported methods
