<h1 align="center">Voter app</h1>
<br></br>
# Description
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
```
## Running & Debugging
The project can be executed in multi-form.The Server Socket, the Manager and the Voter app can be executed at the same time
because they where implemented by threads.
<p></p>
The following sub-tittle will show how execute the application: 

### The Server Socket,  The Manager and The Voter app
```shell
    $ python3 main.py server manager voter
```
Note: The order of execution does not import
### The Server Socket
```shell
    $ python3 main.py server
```
### The Manager app
```shell
    $ python3 main.py manager
```
### The Voter app
```shell
    $ python3 main.py voter
```
Note: The other class / componnents in the project can be executed and tested alone.
