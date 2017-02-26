# Actor Network
The web application alows users to search the movie and actor database. Currently the IMDB data is being used as the data source. The following are the provided functionality: 

  - search a movie
  - displays the movie details as fetched from the data source
  - search an actor
  - displays the actor details as fetched from the data source
  - compute and plot a network graph for the actor, which represents how much the actor is related to his co-actors. 

### Tech Stack
* AngularJS - Frontend for the web app
* D3.js and nvd3 by krispo - Plotting of network graph
* bootstrap - Styling of the web app
* Django - Backend api's for the web app coded using python 2.7

### Installation
* Setup the virtual environment using the requirement.txt file.
* Run the django server on  port 8000. (hosting backend)
* Run the simplehttpserver on port 8080. (hosting frontend)
* Launch the web app on a browser with this url -> localhost:8080

### Future work
Create a local database for the movies and actor data. So that the latency for creation of the network graph is minimised.