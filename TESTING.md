# Manual Testing
This details the steps for manually testing the system through specified
interactions and expected results.

## Admin Page
The admin page should allow administrators to specify the metrics that reviewers will use to rate applicants.

### Manual Testing Instructions

TO-DO: Add testing instructions.

## Review Admin Pages
The review admin pages should allow an administrator to create and delete review metrics.
- Step 1
    - User Action:
    
        Click on the System -> Settings button in the upper right hand corner to go to the settings list.
        
    - Expected Result:
    
        A list of settings shows up.
        
- Step 2
    - User Action:
    
        Click on the "Set review metrics" button in the list.
        
    - Expected Result:
    
        A review metrics list page shows up, empty, with a button saying "Create review metric".
        
- Step 3
    - User Action:
    
        Click on the "Create review metric" button.
        
    - Expected Result:
    
        A review metric creation page shows up with a text box for entering comma-separated values.

- Step 4
    - User Action:
    
        Click on the "Create review metric" button.
        
    - Expected Result:
    
        A review metric creation page shows up with a text box for entering comma-separated values.

- Step 5
    - User Action:
    
        Enter a,b,c,d in the text box and click the Submit button.
        
    - Expected Result:
    
        User should be returned to the review metrics list page, now with 4 metric objects listed.

- Step 6
    - User Action:
    
        Enter localhost/admin in the url box.
        
    - Expected Result:
    
        Django admin page should be displayed.
        
- Step 7
    - User Action:
    
        Scroll down to click Metrics under the Documents heading.
        
    - Expected Result:
    
        The same 4 metric objects should be listed, with a dropdown menu above next to a button reading "Go".
        
- Step 8
    - User Action:
    
        Click on each metric object to see its name. Press the back button on the browser to return and select the next metric object.
        
    - Expected Result:
    
        The metric objects should be named a, b, c, and d.
        
- Step 9
    - User Action:
    
        Delete the metric objects by selecting the four checkboxes to their lefts, selecting "Delete selected metrics" from the dropdown menu above, and clicking "Go" next to the dropdown menu.
        
    - Expected Result:
    
        A display will ask if you're sure.

- Step 10
    - User Action:
    
        Select "Yes, I'm sure"
        
    - Expected Result:
    
        The metrics will be successfully deleted according to a green banner that appears on the page.
        
- Step 11
    - User Action:
    
        Return to localhost/documents/metriclist
        
    - Expected Result:
    
        There will be no metrics displayed. 
        
        **Note:** This means the metrics aren't present for review page testing. Please repeat steps 3-5 to set up for review page testing.

## Review Page
The review page should allow reviewers to assign reviews to applicants based on predefined metrics created by the admin.

### Manual Testing Instructions

**Prerequisite:** Please first create a set of metrics that will be used to evaluate the applicants by following the Manual Testing Instructions for the Admin Page. Only follow the steps below after you have confirmed that the evaluation metrics are created.

- Step 1
    - User Action:

        Click on the 'Documents -> New document' button in the left sidebar to go to the document upload page.
    
    - Expected Result:

        A document upload page shows up.
    
- Step 2
    - User Action:

        Upload an applicant resume (can be any .pdf file) in the document upload page.
    
    - Expected Result:

        The uploaded applicant resume shows up in the 'All documents' page, which you can go to by clicking the 'Documents -> All documents' button on the left sidebar.

- Step 3
    - User Action:

        Go to the 'All documents' page by clicking the 'Documents -> All documents' button on the left sidebar, if you are not already there.
    
    - Expected Result:

        The 'All documents' page shows up

- Step 4
    - User Action:

        Click on the link on your uploaded document.
    
    - Expected Result:

        The preview page for your uploaded document shows up.

- Step 5
    - User Action:

        Click on the 'Review' button on the right sidebar.
    
    - Expected Result:

        A review form for the applicant with this resume shows up.

- Step 6
    - User Action:

        Fill out all the required fields in the review form. In addition, fill out the 'Additional Comments' text box. Feel free to enter abitrary values.

        Once all fields in the review form are filled out, click the 'Save' button at the end of the form.

    - Expected Result:

        Your saved review should show up under Django's admin page for the 'Review' table, which is located at http://\<container_ip_address\>/admin/documents/review/.

        You should check to make sure that all fields in the saved review match with the values you entered.
