# Salesforce-Import-Knowledge-Articles-in-Bulk
This Python script automates the extraction of Question and Answer pairs from a CSV file. It converts the text content of designated cells (e.g., the 'Answer' column and 'Question' column) into individual HTML files, formatted for seamless bulk import into Salesforce Knowledge Articles, specifically populating Rich Text Area fields.

Note: 
Upload CSV with only Question and Answer Columns.
The CSV File may have '\', replace them all with '/'.
Make sure you don't have underscores( _ ) or Brackets ( ) in Text Field like URLLink. 
