# What is this Project

This is an example for data-modelling in MongoDB

The app is purposefully left unfinished. If you would like to use this for your own learning, please fork the repository and complete it.

# Connecting your own MongoDB instance

To use this project, you will need to create your own instance of a MongoDB Atlas cluster. To do this, go to https://www.mongodb.com/cloud/atlas/register

From there, register an account and select the free tier.

You'll need to add a secrets.json file to the project under the parent directory. In this file, add:

``` json
{
    "uri": "mongo_connection_string_goes_here"
}
```

Substitute your own connection information.

# Running the Application

To start, `cd mongo_example` will bring you to the react project directory in your terminal

In the react project directory, run `npm install` to install missing node dependencies

Then you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).