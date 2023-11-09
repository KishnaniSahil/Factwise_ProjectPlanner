
import datetime
import json
import os
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from manageusersapp.models import Board, Team, User , Task
# Create your views here.

def home(request):
    return render(request , "index.html")

def success_page(request):
    return HttpResponse("<h1> This is success page</h1>")
@csrf_exempt
def create_user(request):
     if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        display_name = data.get("display_name")

        # Check if a user with the same name already exists
        if User.objects.filter(name=name).exists():
            return JsonResponse({"error": "User name already exists."}, status=400)

        # Create a new user and save it to the database
        user = User(name=name, display_name=display_name)
        user.save()

        # Return the user's ID in the response
        return JsonResponse({"id": user.id})

     else:
        return JsonResponse({"error": "Invalid request method."}, status=405)
     
def list_users(request):
    if request.method == "GET":
        # Retrieve all users from the database
        users = User.objects.all()

        # Serialize user data into JSON format
        user_data = [
            {
                "name": user.name,
                "display_name": user.display_name,
                "creation_time": user.creation_time.strftime('%Y-%m-%d %H:%M:%S.%f'),
            }
            for user in users
        ]

        # Return the JSON response
        return JsonResponse(user_data, safe=False)

    else:
        return JsonResponse({"error": "Invalid request method."}, status=405) 

def describe_user(request):
    if request.method == "GET":
        user_id = request.GET.get("id")

        if user_id is None:
            return JsonResponse({"error": "User ID is required as a query parameter."}, status=400)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found."}, status=404)

        # Serialize user data into JSON format
        user_data = {
            "name": user.name,
            "display_name": user.display_name,
            "creation_time": user.creation_time.strftime('%Y-%m-%d %H:%M:%S.%f'),
        }

        # Return the JSON response
        return JsonResponse(user_data)

    else:
        return JsonResponse({"error": "Invalid request method."}, status=405)
@csrf_exempt
def update_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_id = data.get("id")
        user_data = data.get("user")

        if not user_id or not user_data:
            return JsonResponse({"error": "User ID and user data are required."}, status=400)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found."}, status=404)

        # Update the user's display name
        display_name = user_data.get("display_name")
        if display_name is not None:
            if len(display_name) <= 128:
                user.display_name = display_name
            else:
                return JsonResponse({"error": "Display name can be at most 128 characters."}, status=400)

        # Save the updated user to the database
        user.save()

        return JsonResponse({"message": "User updated successfully."})

    else:
        return JsonResponse({"error": "Invalid request method."}, status=405)
@csrf_exempt
def get_user_teams(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_id = data.get("id")

        if not user_id:
            return JsonResponse({"error": "User ID is required."}, status=400)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found."}, status=404)

        # Retrieve teams that the user is a member of
        user_teams = Team.objects.filter(users__id=user_id)

        # Serialize team data into JSON format
        team_data = [
            {
                "name": team.name,
                "description": team.description,
                "creation_time": team.creation_time.strftime('%Y-%m-%d %H:%M:%S.%f'),
            }
            for team in user_teams
        ]

        # Return the JSON response
        return JsonResponse(team_data, safe=False)

    else:
        return JsonResponse({"error": "Invalid request method."}, status=405)
    
@csrf_exempt
def create_team(request):
    if request.method == "POST":
        data = json.loads(request.body)
        team_name = data.get("name")
        description = data.get("description")
        admin_id = data.get("admin")

        # Check if the team name is unique
        if Team.objects.filter(name=team_name).exists():
            return JsonResponse({"error": "Team name already exists."}, status=400)

        # Check if the admin user exists
        try:
            admin_user = User.objects.get(id=admin_id)
        except User.DoesNotExist:
            return JsonResponse({"error": "Admin user not found."}, status=404)

        # Create a new team and save it to the database
        team = Team(name=team_name, description=description, admin=admin_user)
        team.save()

        # Return the team's ID in the response
        return JsonResponse({"id": team.id})

    else:
        return JsonResponse({"error": "Invalid request method."}, status=405)      

def list_teams(request):
    if request.method == "GET":
        teams = Team.objects.all()

        # Serialize team data into JSON format
        team_data = [
            {
                "name": team.name,
                "description": team.description,
                "creation_time": team.creation_time.strftime('%Y-%m-%d %H:%M:%S.%f'),
                "admin": team.admin.id,
            }
            for team in teams
        ]

        # Return the JSON response
        return JsonResponse(team_data, safe=False)

    else:
        return JsonResponse({"error": "Invalid request method."}, status=405)  
   
@csrf_exempt
def describe_team(request):
    if request.method == "POST":
        data = json.loads(request.body)
        team_id = data.get("id")

        if not team_id:
            return JsonResponse({"error": "Team ID is required."}, status=400)

        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return JsonResponse({"error": "Team not found."}, status=404)

        # Serialize team data into JSON format
        team_data = {
            "name": team.name,
            "description": team.description,
            "creation_time": team.creation_time.strftime('%Y-%m-%d %H:%M:%S.%f'),
            "admin": team.admin.id,
        }

        # Return the JSON response
        return JsonResponse(team_data)

    else:
        return JsonResponse({"error": "Invalid request method."}, status=405) 
    
@csrf_exempt
def update_team(request):
    if request.method == "POST":
        data = json.loads(request.body)
        team_id = data.get("id")
        team_data = data.get("team")

        if not team_id or not team_data:
            return JsonResponse({"error": "Team ID and team data are required."}, status=400)

        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return JsonResponse({"error": "Team not found."}, status=404)

        # Check if the team name is unique
        new_name = team_data.get("name")
        if new_name and new_name != team.name and Team.objects.filter(name=new_name).exists():
            return JsonResponse({"error": "Team name already exists."}, status=400)

        # Update team details
        if new_name:
            team.name = new_name
        description = team_data.get("description")
        if description is not None:
            if len(description) <= 128:
                team.description = description
            else:
                return JsonResponse({"error": "Description can be at most 128 characters."}, status=400)
        admin_id = team_data.get("admin")
        if admin_id:
            try:
                admin_user = User.objects.get(id=admin_id)
                team.admin = admin_user
            except User.DoesNotExist:
                return JsonResponse({"error": "Admin user not found."}, status=404)

        # Save the updated team to the database
        team.save()

        return JsonResponse({"message": "Team updated successfully."})

    else:
        return JsonResponse({"error": "Invalid request method."}, status=405)        

@csrf_exempt
def add_users_to_team(request):
    if request.method == "POST":
        data = json.loads(request.body)
        team_id = data.get("id")
        user_ids = data.get("users")

        if not team_id or not user_ids:
            return JsonResponse({"error": "Team ID and user IDs are required."}, status=400)

        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return JsonResponse({"error": "Team not found."}, status=404)

        added_users = []
        for user_id in user_ids:
            try:
                user = User.objects.get(id=user_id)
                team.user_set.add(user)
                added_users.append(user.name)
            except User.DoesNotExist:
                return JsonResponse({"error": f"User with ID {user_id} not found."}, status=404)

        if added_users:
            return JsonResponse({"message": f"Users {', '.join(added_users)} added to the team."})
        else:
            return JsonResponse({"message": "No users added to the team."})

    else:
        return JsonResponse({"error": "Invalid request method."}, status=405)
    
@csrf_exempt
def list_team_users(request):
    if request.method == "POST":
        data = json.loads(request.body)
        team_id = data.get("id")

        if not team_id:
            return JsonResponse({"error": "Team ID is required."}, status=400)

        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return JsonResponse({"error": "Team not found."}, status=404)

        users_in_team = team.user_set.all()
        user_list = []

        for user in users_in_team:
            user_data = {
                "id": user.id,
                "name": user.name,
                "display_name": user.display_name
            }
            user_list.append(user_data)

        return JsonResponse(user_list, safe=False)

    else:
        return JsonResponse({"error": "Invalid request method."}, status=405)

@csrf_exempt    
def create_board(request):
    if request.method == "POST":
        data = json.loads(request.body)

        # Extract data from the JSON request
        board_name = data.get("name")
        description = data.get("description")
        team_id = data.get("team_id")
        creation_time = data.get("creation_time")

        if not board_name or not team_id:
            return JsonResponse({"error": "Board name and team ID are required."}, status=400)

        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return JsonResponse({"error": "Team not found."}, status=404)

        if len(board_name) > 64:
            return JsonResponse({"error": "Board name exceeds the maximum length of 64 characters."}, status=400)

        if len(description) > 128:
            return JsonResponse({"error": "Description exceeds the maximum length of 128 characters."}, status=400)

        # Check if a board with the same name already exists in the team
        if Board.objects.filter(name=board_name, team=team).exists():
            return JsonResponse({"error": "Board name must be unique within the team."}, status=400)

        # Create and save the board
        board = Board(name=board_name, description=description, team=team, creation_time=creation_time)
        board.save()

        return JsonResponse({"id": board.id})

    else:
        return JsonResponse({"error": "Invalid request method."}, status=405)   
    
@csrf_exempt  
def add_task(request):
    if request.method == "POST":
        data = json.loads(request.body)

        # Extract data from the JSON request
        title = data.get("title")
        description = data.get("description")
        user_id = data.get("user_id")
        board_id = data.get("board_id")
        creation_time = data.get("creation_time")

        if not title or not user_id or not board_id:
            return JsonResponse({"error": "Title, user ID, and board ID are required."}, status=400)

        try:
            board = Board.objects.get(id=board_id)
        except Board.DoesNotExist:
            return JsonResponse({"error": "Board not found."}, status=404)

        if len(title) > 64:
            return JsonResponse({"error": "Task title exceeds the maximum length of 64 characters."}, status=400)

        if len(description) > 128:
            return JsonResponse({"error": "Description exceeds the maximum length of 128 characters."}, status=400)

        if board.status != "OPEN":
            return JsonResponse({"error": "Tasks can only be added to an OPEN board."}, status=400)

        # Check if a task with the same title already exists on the board
        if Task.objects.filter(title=title, board=board).exists():
            return JsonResponse({"error": "Task title must be unique within the board."}, status=400)

        # Create and save the task
        task = Task(title=title, description=description, user_assigned_id=user_id, board=board, creation_time=creation_time)
        task.save()

        return JsonResponse({"id": task.id})

    else:
        return JsonResponse({"error": "Invalid request method."}, status=405)    
     
@csrf_exempt 
def update_task_status(request):
    if request.method == "POST":
        data = json.loads(request.body)

        # Extract data from the JSON request
        task_id = data.get("id")
        status = data.get("status")

        if not task_id or not status:
            return JsonResponse({"error": "Task ID and status are required."}, status=400)

        # Check if the provided status is valid
        valid_statuses = ["OPEN", "IN_PROGRESS", "COMPLETE"]
        if status not in valid_statuses:
            return JsonResponse({"error": "Invalid status. Status must be OPEN, IN_PROGRESS, or COMPLETE."}, status=400)

        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return JsonResponse({"error": "Task not found."}, status=404)

        # Update the task status
        task.status = status
        task.save()

        return JsonResponse({"message": "Task status updated successfully."})

    else:
        return JsonResponse({"error": "Invalid request method."}, status=405) 
     
@csrf_exempt 
def list_boards(request):
    if request.method == "POST":
        data = json.loads(request.body)

        # Extract the team ID from the JSON request
        team_id = data.get("id")

        if not team_id:
            return JsonResponse({"error": "Team ID is required."}, status=400)

        try:
            # Retrieve a list of boards for the specified team
            boards = Board.objects.filter(team_id=team_id)
        except Board.DoesNotExist:
            return JsonResponse({"error": "Team not found or has no boards."}, status=404)

        # Prepare the response data
        board_list = [{"id": board.id, "name": board.name} for board in boards]

        return JsonResponse(board_list, safe=False)

    else:
        return JsonResponse({"error": "Invalid request method."}, status=405)      

@csrf_exempt 
def export_board(request):
    if request.method == "POST":
        data = json.loads(request.body)

        # Extract the board ID from the JSON request
        board_id = data.get("id")

        if not board_id:
            return JsonResponse({"error": "Board ID is required."}, status=400)

        try:
            # Retrieve the board with tasks
            board = Board.objects.get(id=board_id)
            tasks = Task.objects.filter(board=board)
        except Board.DoesNotExist:
            return JsonResponse({"error": "Board not found."}, status=404)

        # Create a text file in the "out" folder and write board details and tasks to it
        out_folder = "out"
        os.makedirs(out_folder, exist_ok=True)  # Ensure the "out" folder exists

        out_file_name = f"board_{board_id}_export.txt"
        out_file_path = os.path.join(out_folder, out_file_name)

        with open(out_file_path, "w") as out_file:
            out_file.write(f"Board Name: {board.name}\n")
            out_file.write(f"Board Description: {board.description}\n\n")

            out_file.write("Tasks:\n")
            for task in tasks:
                out_file.write(f"- Title: {task.title}\n")
                out_file.write(f"  Description: {task.description}\n")
                out_file.write(f"  Status: {task.status}\n\n")

        return JsonResponse({"out_file": out_file_name})

    else:
        return JsonResponse({"error": "Invalid request method."}, status=405)
