CS235 Podcast Library
This is a start of a web app that can be used for browsing and viewing different podcasts. Currently, it can only hold a a small set of podcast items that have been manually added to the project.
This project uses HTML and Jinja templates to create a home page, podcast catalogue, navbar and podcast description using several SOLID design principles.

home.html displays the podcast library.
podcastCatalogue.html displays the available podcasts.
podcastDescription.html displays info about the podcast and the best episode.
navbar.html provides navigation for the different pages.

This project strongly uses the SOLID design principles:
It used the Single Responsibility Principle the best, as each individual html page is responsible for it's own thing, with the navbar.html responsible for navigation between pages, the Home page only displaying and searching podcast items, the podcastCatelogue.html only displaying the catalogue and the podcastDescription.html displaying detailed podcast info. 
It can be improved by only using a template and providing the podcast info separately in a different data file, which can be easily updated with new podcasts or removing older podcasts with no change to the actual code.
Currently, there is also evidence supporting the Open/Closed Principle as there are code that is reused such as the navbar.html, and this can be used for other files to improve the code.
The project can also be improved using the Dependency Inversion Principle to instead use data that is provided than data currently in the code.
