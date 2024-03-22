from django.db import models

class ProcessedData(models.Model):
    columnName = models.CharField(max_length=255)  # Stores the name of the column from the dataset
    dataType = models.CharField(max_length=255)  # Stores the data type of the column (e.g., 'int', 'string')
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically sets the date and time when a record is created

    def __str__(self):
        return self.columnName  # Returns the name of the column when the model instance is printed
