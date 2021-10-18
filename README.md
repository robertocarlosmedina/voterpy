<h1 align="center">VoterPy</h1>
<h2>Description</h2>
Application that allows the client to poll and control votes related to an election. 

<!-- # Main objective -->

## Dependences / libraries use:
The libraries that i use are the following one's:
```shell
    $ import socket
    $ import request
    $ import Thread
    $ import pygame
    $ import json
    $ import os
    $ import re
```
## Running & Debugging
The project can be executed in multi-form.The Server Socket, the Manager and the Voter app can be executed at the same time
because they where implemented by threads.

The following sub-tittle will show how execute the application: 
### The Front-App 

```shell
    $ python3 main.py
```
This will open a windows whit visual interface that will allow the user to chose what app he wants to start
### The Server Socket,  The Manager and The Voter app
```shell
    $ python3 main.py server manager voter
```
Note: The order of execution does not matters 
### [The Server Socket](https://github.com/RobertoCarlosMedina/voterpy/tree/main/server)
```shell
    $ python3 main.py server
```
### [The Manager app](https://github.com/RobertoCarlosMedina/voterpy/tree/main/manager)
```shell
    $ python3 main.py manager
```
### [The Voter app](https://github.com/RobertoCarlosMedina/voterpy/tree/main/voter)
```shell
    $ python3 main.py voter
```
Note: The other class / componnents in the project can be executed and tested alone.

## Code Of Conduct
This project implement the [Contributor Covenant Code of Conduct](https://github.com/RobertoCarlosMedina/voter-app/blob/main/CODE_OF_CONDUCT.md), read it before any contribution.

## MIT Licence
This projet implement the [MIT Licence](https://github.com/RobertoCarlosMedina/voter-app/blob/main/LICENSE), please read it before use this project.

Copyright © 2021 Roberto Carlos
