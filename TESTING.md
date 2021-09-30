# Manual Testing
This details the steps for manually testing the system through specified
interactions and expected results.

## Admin Page
The admin page should allow administrators to specify the metrics that reviewers will use to rate applicants.

### Manual Testing Instructions

TO-DO: Add testing instructions.

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