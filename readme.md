# Product Realization - Intelaegis

The idea of this development project was to deliver a client-server modeled app. The server was created to provide a means of communication between all the clients, similar to a star topology in computer networks. The clients can then communicate to the server with any concerns they may have, which is when the server will choose to distribute those concerns.

All coding was done in python using a couple imports throughout multiple scripts. There are two main scripts, client.py, as well as, server.py. The client.py script is used by school administrators or teachers to establish emergency events that have occurred. Those events include: Lock Out, Shelter in Place, Evacuate, Medical, Lock Down, & Active Shooter. Each event has its own distinct characteristics and asks the client different questions depending on the responses. The server.py script is used to administrate all events any clients shall make. Those actions can include: informing other clients connected to the server that an emergency has occurred, if an all clear has been issued, and current emergency status whether an emergency is happening or not. The server is there to act as a means to distribute valuable information in a timely manner.

A configuration file was created in json format to allow for a more robust system. The configuration file can be manipulated to accommodate additions to the client side app. For example: login information or other important data.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
- Python 3+
- Terminal Tool
- 1MB of free space
- Configuration file
```

### Installing

#### Get server running:
```
git clone "git url"
cd REPO_FOLDER
python3 server.py
```

#### Get client running:
```
git clone "git url"
cd REPO_FOLDER
python3 client.py
```

## Running the tests

The huge advantage of using Python to write scripts is the ability to test what you code. As progress was made throughout the sprints more and more time was required to be allocated towards testing. By the end of the project almost all of my time was spent testing the scripts. While there was no set test plan throughout the project I did follow some important guidelines. The guidelines are listed below:
```
- Test all new features after every sprint. 
- Regression test old features as code was changed. 
- Test as many edge cases as possible. 
- Make changes accordingly if problems were found. 
```
In other projects test plan features were required. For example, in Java, jUnit tests were typically required to test the test cases. Test cases, scripts and reports were not mandatory because Python is such an efficient language to script in. 

## Deployment
- The python scripts work on both Windows and Mac OS machines.
- Depending on the server location, the host may need to be changed inside client.py.
- See below for the diagrams of the system.

## Authors
- Will Paltz - wcpaltz@uwm.edu

## License
- This project is licensed under Tom Dean and Intelaegis.

## Acknowledgments
- Thank you Tom Dean for providing Product Realization with such a cool project! His direction and help was much appreciated!
