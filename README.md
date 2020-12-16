# Fitness-tracker-MS3
Interactive fitness tracker for educational purposes only. Materialise styling template has been used for this project.

Fitness tracker can be accesses here:
https://fitness-ms3-samanthasimmons.herokuapp.com/

Fitness Tracker requires a login, however there is a test account user if you dont want to create an account
Username: TesterAccount
Password:test123

## UX & UI
both desktop and mobile friendly, on accessing the login screen, you can either enter the below credentials or create your own user. The aim with the FitnessTracker is for users, to add, manage, and view all of their workouts, when editing a workout the input value is set to what was initially saved for ease of editing. 

The design is based around being clean and concise for usability, as the main focus of the site, utilising the styling template materialise.

### Wireframe
 my Wireframes can be viewed [here](https://xd.adobe.com/view/4744aed7-1936-4de1-827a-5927a5d2836f-1217/)


## Technologies Used

Python - used as the backend language to connect what the user sees and the data they have input
Flask - framework used to simplify python for faster builds
Jinja - used for creating templates that dynamically show information found in MongoDB
MongoDB - database for storing all user input
HTML5 - used to semantically structure website
CSS3 - used for styling of HTML
Javascript - used in conjunction with jQuery to create an interactive user experience
jQuery - used in conjunction with Javascript to create an interactive user experience
Materialise - used for quick, responsive styling
Pixabay - used for free stock photos

## User stories

1) "Fitmess Tracker has alot of potentially for a future application, very easy to use and navigate though, its great to be able to see my workouts in one place"

2) "I typically do different forms of working out and having a place to track all my workouts in one place is amazing, completed by allowing users to select from a wide range of different sports/workouts when adding it their dashboard, or even adding there own!"

## Strategy

As the target audience is broad for the fitness industry, from ultra marathon runners, to you average daily walker, I have kept the interface clean and ease of navigation. Users can quickly login in, see there dashboard with all there recent workouts logged and add new ones. As you can track your fitness, it helps users see when they was last active.

## Structure

Responsiveness and clarity were my goal for this site. It is not feature heavy because I don't want to over complicate something that should be simple.

## Features

This project is built with Python, Flask, Jinja, CSS, Materialize, and JQuery and uses MongoDB to store user input. I chose to use Materialize to keep a nice, clean grid feel to the site.

- Flask is used to quickly build reusable templates that pulls information from MongoDB and allows the user to create, read, update, or delete information that is stored.

- CRUD Functionality - users can create, read, update and delete all workouts on there dashboard area

- Dashboard blocks -  users can easily see and scroll through workouts they have added which are displayed in a card block formats 

- Login - Users must create a unique login to access the fitness tracker, which will display that users workouts. 

- Imagery - I did have the functionality of images you upload to your workout then appearing within your “workout block area” however after recently discovering its poor practice to upload imagery into mongoldb as this could impact the database loadtimes, I decided to move this into a future feature.

- Requesting a partner - as this is a workout tracker, I thought potentially would be great to also have the functionality to request a partner, say for a game of tennis, or a sport you cant, or don’t wish to do alone. Such as asking for a running partner for certain days of the week. To help keep you both motivated.

## Future Features

With fitness industry scaling massively at the moment, the lists of future features could be endless, from infographic charts, to social interactions.

- Social interactions, this fitness tracker could be adapted into a social platform where you can add friends, and follow each other for additional motivational purposes
- Having a random selector on the imagery that uploads with your workout would be a great feature too rather than having one selected static image - i have tried to implement this, however i have struggled getting this to work, and due to the time of year, have found lack of support to get this issue resolved, and further understanding of the resolution.
- I would like to integrate the website with additional sports watches and phone trackers to automatically upload once you have completed your workout
- It would be great if we could have a data chart of tracking when a user is workout out too much or not enough, so it helps to set daily targets to hit
- Gps tracking - would be able to track the users distance again this would probably work better by using a fitness tracking device, but also so you could implement maps into each users workout so they can see and potentially map out new routes if needed.
- Tracking calorie expenditure to see if your eating enough for your training methods
- Add in the ability to type password in again to delete a workout rather than just deleting 

## Testing

All tests have been run manually through the console in google chrome. I have also utilising the debugger; on the lines the errors are appearing in the try and break down these errors further. Along with running the code through a syntax validator to pick up errors. I found the debugger; test and debug tool to be the most efficient with breaking down problems, utilising the console/sources.

I have also had family members testing out the fitness tracker, and playing with the intereactions of creating and deleting features, to get feedback on the usibility and functions.

Found bugs/ errors

issue 1 - Matching workouts created by to a users dashboard, as initially when you logged in you could see all workouts created by all users, rather than just your own 

issue 2 - Heroku created a number of bugs for me to resolve, typically due to my inexperience with using Heroku, along with using VSC as my desired platform to build in. 

issue 3 - CERTIFICATE_VERIFY_FAILED which i initally thought was linked to the IP whitelist, however the connection string for MONGO_URI required some additional arguments in to successfully establish a connection with the database.
https://pythonise.com/categories/python/connecting-to-a-microsoft-azure-cosmos-db-with-python-and-the-mongodb-ap

Mentor review - Overall positive feedback from my mentor, Jonathon he suggested looking into different ways imagery could be added such as a src outside of the website  which you could like to, however as it wasn’t a requirement for this project I decided not to make it a focal point.

Manual testing for css styling was done through the live preview port, in visual code.

## Device/Browser Testing

Used Chrome Dev tools to test the responsiveness of this project on multiple devices
Check browser compatibility in Firefox, Chrome, and Safari

## Outstanding Issues
Opponant Request - needs linking up properly, and then posting to a feed html, this was an idea which would need further work

Challenge a friend - also needs some additional work, where you can email friends and invite them into the platform, this is where I do believe having "feed like area" full of the challenges, and opponant requests that have been made.

One main issue outstanding is to get an image to randomly upload when adding a workout using the chose function in java, but i think as i spend so much time around the image functionality with this project, I wanted to submit as i have gone over my allocated project timeframe.

From testers feedback i also have the suggestion of adding a pop up element with a notification, to ensure you want to delete your workout. 

## Database Structure

Database structure these can be accessed in my github project.
screenshot1.png
screenshot2.png

## Deployment

The site is hosted using Heroku, any additional or new commits will automatically be updated as this links to my master branch.
Deploy to Heroku

Detailed instructions for deploying to Heroku can be found [here](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true)


## Local Deployment

To create a local copy of this repository, follow these steps:

Go to my repo
Click the "Clone or Download" button on the top-right of the page
Click the copy icon to copy the HTTPS link
Open terminal
Change the current directory to the location where the cloned directory will be made
Type git clone <cloned URL> with the cloned URL being the URL you copied in step 3 and run the command
For more information check out GitHub's guide to cloning a repo here.


## Acknowledgement
Free imagery resource [pixabay](https://pixabay.com/images/search/workout/)


Onload Attribute isn't supported on all elements in particular it won't work on a div tag, here's a list of where it's valid to use: https://www.w3schools.com/tags/ev_onload.asp