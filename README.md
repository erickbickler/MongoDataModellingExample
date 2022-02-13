# What is this Project

This is an example of data-modeling in MongoDB created for an informational lecture on NoSQL Databases

The app is purposefully left unfinished. If you would like to use this for your own learning, please fork the repository and complete it.

A finished version of the project is located in the `finished_project` branch. This models the remaining objects/queries listed below. Keep in mind this
is not a definitive solution, and is only one way of doing it. Feel free to be creative!

# Connecting your own MongoDB instance

To use this project, you will need to create your own instance of a MongoDB Atlas cluster. To do this, go to https://www.mongodb.com/cloud/atlas/register

From there, register an account and select the free tier.

You'll need to add a `secrets.json` file to the project under the parent directory. In this file, add:

``` json
{
    "uri": "mongo_connection_string_goes_here",
}
```

Substitute your own connection information.

# Running the app

Once you have your MongoDB cluster initialized, you need to create the pre-seeded data.

To do this, run:
``` bash
python ./src/initialize_data.py
```

After doing that, the default database will be created with example data. You can then run:

``` bash
python ./src/main.py
```

To run the application in the command line app.

# The Data

The data is built on the NDSU chapter of the ACM. All preseeded data is example data and any correlation with real world people is purely coincidental.

## Objects

- Members
- Special Interest Groups (SIGS)
- EC Board
- Snacks
- Arcade Scores
- Weekly Minutes

Note, as this is purposefully left unfinished, only the following objects are currently modeled:

- Members
- SIGs
- Arcade Scores

# Completing the Application

Your goal is to complete the application by modeling the remaining objects and writing the queries to add/update them. You can do this by adding your own functions to main.py
that run the queries, and add those functions to the command line interface selection. Feel free to play around with your own ideas, the goal here is to learn about how 
data can be modeled/queries in a NoSQL format. You don't have to model the objects I list. Be creative!