# aching_wheels
Cerebro Capstone Project
## Project Overview
*This project seeks to create a social-media platform to allow citizens to collaborate and aid law enforcement to help find a missing person*
The missing persons will be entries on a DRF. Each missing person will be displayed as a "board" and users will be able to post to the board to collaborate.

Later features may see a chat for users to communicate directly, and the ability for users to vote to "pin" a post to the top of the board
that is a valuable clue to users and law enforcement.

**Frameworks used:**
 - Pillow, to display images
 - Materialize, to make everything look real good
 - Googlemaps, to display a map of clues and key locations for the subject
 - DRF, to create an API of all the missing persons
 - Chatsocket (maybe?), to enable users to chat directly

## Functionality

When the user enters the site, if they are authenticated, they will move directly to the home page showing a board of the last 5-10 persons who have gone missing. If they are not authenticated, they will be prompted to login or register.

On the home screen, they will be able to search for the missing person they wish to collaborate on, click on that person and be taken to their board.

The "board" of each missing person will display their key info, a photo, and a map with key locations, while user posts can be found below.

## Data Model

**Models:**
 - CustomUsers:
	 - fields: profilepic
 - Missing Persons:
	 - fields
		 - First Name (charfield)
		 - Last Name (charfield)
		 - description of disappearance (charfield)
		 - height
		 - weight
		 - race
		 - hair color
		 - eye color
		 - Last seen location
		 - Last seen wearing/driving
		 - Present-day sketch (if applicable)

## Schedule
- week one: set up Django project, user auth system, and API of all missing persons 
- week two: vue app that displays missing persons and posts from people trying to collaborate on them 
- week three: Make it look reall really good (possibly add the "pin" feature for valuable posts and/or chat feature for users attempting to directly collaborate)
