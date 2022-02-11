# What is this Project

This is an example for data-modelling in MongoDB

The app is purposefully left unfinished. If you would like to use this for your own learning, please fork the repository and complete it.

# Connecting your own MongoDB instance

To use this project, you will need to create your own instance of a MongoDB Atlas cluster. To do this, go to https://www.mongodb.com/cloud/atlas/register

From there, register an account and select the free tier.

You'll need to add a `secrets.json` file to the project under the parent directory. In this file, add:

``` json
{
    "uri": "mongo_connection_string_goes_here"
}
```

Substitute your own connection information.