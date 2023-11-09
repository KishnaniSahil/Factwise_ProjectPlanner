# Factwise_ProjectPlanner
Team Project Planner Tool
The Team Project Planner Tool is a web application for managing teams, project boards, and tasks 
within those boards. It provides a set of APIs to perform various operations. This README will help 
you understand how to use the application and the main components involved.
Key Features
User Management
Create a User
You can create a new user by making a POST request to /create_user/. Provide user details in a JSON 
format, including the user's name and display name. The API will return the user's unique ID.
List All Users
To retrieve a list of all users, make a GET request to /list_users/. This will return a JSON list of user 
information, including name, display name, and creation time.
Describe User
Use the /describe_user/ endpoint to get detailed information about a specific user. Send a JSON 
request with the user's ID, and the response will include their name, description, and creation time.
Update User
You can update a user's display name by sending a JSON request with the user's ID and the new 
display name to the /update_user/ endpoint.
Get User's Teams
To retrieve a list of teams that a user is a member of, use the /get_user_teams/ endpoint. Provide 
the user's ID in the request to get a list of teams the user belongs to.
Team Management
Create a Team
You can create a new team by making a POST request to /create_team/. Provide the team's name, 
description, and the ID of the team admin. The API will return the team's unique ID.
List All Teams
To retrieve a list of all teams, make a GET request to /list_teams/. This will return a JSON list of team 
information, including name, description, creation time, and the admin's ID.
Describe Team
Use the /describe_team/ endpoint to get detailed information about a specific team. Send a JSON 
request with the team's ID, and the response will include the team's name, description, creation 
time, and the admin's ID.
Update Team
You can update a team's name, description, or admin by sending a JSON request with the team's ID 
and the updated details to the /update_team/ endpoint.
Add/Remove Users from Team
To add or remove users from a team, send a JSON request with the team's ID and the list of user IDs 
to the /add_users_to_team/ or /remove_users_from_team/ endpoint.
List Team Users
Retrieve a list of users who are members of a specific team by sending a JSON request with the 
team's ID to the /list_team_users/ endpoint.
Project Board Management
Create a Board
You can create a new project board by making a POST request to /create_board/. Provide the 
board's name, description, team ID, and creation time. The API will return the board's unique ID.
Close a Board
To close a project board, send a JSON request with the board's ID to the /close_board/ endpoint. The 
board's status will be set to CLOSED if all tasks are marked as COMPLETE.
Add Task to Board
You can add a new task to an open board by sending a JSON request with the task's title, description, 
user ID, and creation time to the /add_task/ endpoint. The API will return the task's unique ID.
Update Task Status
Change the status of a task by sending a JSON request with the task's ID and the desired status 
(OPEN, IN_PROGRESS, or COMPLETE) to the /update_task_status/ endpoint.
List Open Boards for a Team
Retrieve a list of open boards for a specific team by sending a JSON request with the team's ID to the 
/list_boards/ endpoint. This will return a list of board IDs and names.
Export Board
To export a board in a presentable view, use the /export_board/ endpoint. Send a JSON request with 
the board's ID, and the API will create a text file with a name you can specify in the response.
Models
User
• name (max 64 characters): The user's name.
• display_name (max 64 characters): The user's display name.
• creation_time: The user's creation timestamp.
Team
• name (max 64 characters): The team's name.
• description (max 128 characters): Description of the team.
• creation_time: Team's creation timestamp.
• admin: User who is the admin of the team.
Board
• name (max 64 characters): The project board's name.
• description (max 128 characters): Description of the board.
• creation_time: Board's creation timestamp.
• team: Team to which the board belongs.
• status: Status of the board (OPEN or CLOSED).
Task
• title (max 64 characters): The task's title.
• description (max 128 characters): Description of the task.
• creation_time: Task's creation timestamp.
• user_assigned: User to whom the task is assigned.
• status: Status of the task (OPEN, IN_PROGRESS, or COMPLETE).
With these APIs and models
