# UltimateToDo
This is a CRUD function api for todo list.

###  Mongodb files structure

#### User Table
     {
        "id": 1,
        "name": "Awais Akram",
        "password": "awais64",
        "username": "awais"
     }
#### ToDo Table
     {
     "_id": {
        "$oid": "5b765e67fb6fc066d426f8bc"
     },
        "taskid": 1,
        "userid": 1,
        "title": "assignment",
        "note": "this is my first task",
        "setdate": "Fri, 17 Aug 2018 10:32:30 GMT",
        "duedate": "Sat, 17 Aug 2018 10:32:30 GMT",
        "done": false
     }
     
# Test cases for this app 
Install Postman sofware to execute all test cases

## Case 01
### Title: 
   Add User
### Description:
   In this test case we will add a new user if it is not in database.
### Steps:
   1) In Postman set request method to POST and enter localhost address of api.
   2) In body of request write method with json object you want to save.
       
            {
              "name": "Awais Akram",
              "username": "awais",
              "password": "awais64"
            }
       
   3) Click on submit button to add user.

## Case 02
### Title: 
   Login
### Description:
   In this test case we will login a user.
### Steps:
   1) In Postman set request method to POST and enter localhost address of api.
   2) In body of request write method with json object you want to login with.
        
            {
              "username": "awais",
              "password": "awais64"
            }   
   
   3) Click on submit button to login.

## Case 03
### Title: 
   Get All Task
### Description:
   In this test case we will retrieve all task of a user.
### Steps:
   1) In Postman set request method to GET and enter localhost address of api.
   2) Because it is GET method on object will be pass.
   3) Click on submit and all task of a user will retrieve.
   
## Case 04
### Title: 
   Get Task by id
### Description:
   In this test case we will retrieve only one task of a user by giving an id.
### Steps:
   1) In Postman set request method to GET and enter localhost address of api and also id of a task.
   2) Because it is GET method on object will be pass.
   3) Click on submit and one task of a user will retrieve.

## Case 05
### Title: 
   Update Task by id
### Description:
   In this test case we will update task of a user by giving an id.
### Steps:
   1) In Postman set request method to PUT and enter localhost address of api and also id of a task.
   2) In body of PUT request method body write json object you want to set as updated data in DB.
   
              {
                "title": "My updated task",
                "note": "this is my first updated  task that I will do  ",
              }
   
   3) Click on submit and data of task is updated.

## Case 06
### Title: 
   Delete Task by id
### Description:
   In this test case we will delete task of a user by giving an id.
### Steps:
   1) In Postman set request method to DELETE and enter localhost address of api and also id of a task.
   2) In body of DELETE request method only id is used to delete the document.
   3) Click on submit and document is delete.



          
