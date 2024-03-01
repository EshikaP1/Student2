---
toc: False
comments: True
layout: post
title: NTM REVIEW
description: Me and my team worked on a fitness page in order to support a more healthy way of living. I worked on the drink page (Css, frontend, and backend), login page (backend+frontend), and deployment. In the drinks page, I was able to run a get command in the backend to display my data which I had stored in a SQlite file. I was able to call upon specific drinks and get the calories they hold. I was also able to use the Create and Delete commands to create and delete a drink. I was able to add an edit pop up function, however I have yet to complete the frontend and backend code for it. I also struggled in deployment as we had issues running ./migrate.sh. Debugging was a hard task yuuet in the end deployment was sucessful! 
type: hacks
courses: {'compsci': {'week': 17}}
---
<style>
  table {
    width: 100%;
    border-collapse: collapse;
  }

  th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }

  img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 0 auto;
  }
</style>

| **Collegeboard Requirements**                                    | **My Drinks API!**                                                                                       |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| **Input Instructions**:   Instructions for input from one of the following: the user, a device, an online data stream, a file.     | In the drinks api I created, I was able to promt a user for a drink so that they could get a calorie. <img alt="Extensions" src="{{site.baseurl}}/images/drink1.png"  width="250">  <img alt="Extensions" src="{{site.baseurl}}/images/Drink_GET.png" title="VS Code Marketplace" width="700" height="200">|
| **Use of Collection**: Use of at least one list (or other collection type) to represent a collection of data that is stored and used to manage program complexity and help fulfill the users purpose.                                           |I coded a segment to translate my JSON file to initilize in a .db file. Utilizing SQLite tables, I was able to effectively store my data so it is easy to access and call upon. <img alt="Extensions" src="{{site.baseurl}}/images/Database_Drink.png"  width="250"> |
| **Procedure Definition** : At least one procedure that contributed to the program’s intended purpose where you have defined: the name, return type, one or more parameters.                                        | Using CRUD operations, I was able to code a frontend which allows the user to delete a row based off of an onclick event which then prompts the user for a confirmation on whether to delete the slected item or not. It will then refresh the page, providing the table with the drink delted both on the web page and in backend SQlite table. <img alt="Extensions" src="{{site.baseurl}}/images/DELTE_DRINK.png"  width="250"> |
| **Algorithm Design** :  An algorithm that includes sequencing, selection, and iteration that is in the body of the selected procedure. | MY code itterates over the JSON database in order to convert into an SQlite databse for easy acess. Here we use for and if loops to do the selected procedure. <img alt="Extensions" src="{{site.baseurl}}/images/JSON_covertcode.png"  width="250">  |
| **Procedure Calls**: Calls to your student-developed procedure.                                           | In the frontend, I am using a fetch command when the page is reloading. It calls to the backend and adds console errors if they occur. <img alt="Extensions" src="{{site.baseurl}}/images/Procedure_Drink.png"  width="250">     |
| **Output Instructions**: Instructions for output (tactile, audible, visual, or ) based on input and program functionality.                                          | The console will provide a message that will be sotred if the code for delteting a row ran. Also, the user can see a page to confirm whether or not they want to delte the drink. <img alt="Extensions" src="{{site.baseurl}}/images/DELETE_CONFIRM.png"  width="250"> 

### Login code I worked with:

<img alt="Extensions" src="{{site.baseurl}}/images/LOGIN_CODE.png"  width="250"> 
