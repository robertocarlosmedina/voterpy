<h1 align="center">Server</h1>
<h2>Description</h2>
This server sockets will use json as data base, and serve their content. And all the commands, like post, get, ..., are all implemented by pure code.

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
## Commands that the server will responde:

### - Get
This commands can be use to get all data from the server, and the menssage sent relative to this commands would be like:
```shell
    $ connectingToServer("voters/get")
```
The logic is like: message = "voters/get" if we split the message in "/" we have <bold>"voters"</bold> and <bold>"get"</bold>, what means that the
data base is voters and the request method is get.

### - GetById
This commands has the same function as the Get, but it differentiates in the fact that it will return a specific value from the server
that matches the specified id.
```shell
    $ connectingToServer("voters/getById foqwfojqwjfo1221ij1221")
```
The logic is like: message = "voters/get" if we split the message in "/" we have "voters", "get" and "foqwfojqwjfo1221ij1221", what means that the
data base is voters, the request method is getById and the is "foqwfojqwjfo1221ij1221".

### - PutById
This commands will change a value already stored on the server according to the id.
```shell
    $ serverConectAndSend("voters/putById irhfirh32391eqweqw,name,Roberto")
```
The logic is like: message = "voters/putById irhfirh32391eqweqw,name,Roberto" if we split the message in "/" we have "voters", "putById",
and "irhfirh32391eqweqw,name,Roberto" what means that the data base is voters, the request method is putById where the id is "irhfirh32391eqweqw",
the atribuit that will be change is "name" and the new value is ""Roberto.

### - Post
This commands will store a new value in the server's data base.
```shell
    $ connectingToServer("voters/post atribute1=value,atribute2=value,atribute3=value")
```
The logic is like: message = "voters/post atribute1=value,atribute2=value,atribute3=value" if we split the message in "/" we have "voters", "post",
and "atribute1=value,atribute2=value,atribute3=value" what means that the data base is voters, the request method is post, and the atributes and value
are the ones that are passed like showed in this string "atribute1=value,atribute2=value,atribute3=value".

### - Delete
This commands will delete an value store in the server's data bases.
```shell
    $ connectingToServer("voters/delete eewqfqwfqwgehre45t56261")
```
The logic is like: message = "voters/delete id" if we split the message in "/" we have "voters", "delete",
and "eewqfqwfqwgehre45t56261" what means that the data base is voters, the request method is delete, and the value to be deleted is
the one how was the id "eewqfqwfqwgehre45t56261".

### - DeleteAll
This commands will delete all the value stored in a data base in the server.
```shell
    $ connectingToServer("voters/deleteAll)
```
The logic is like: message = "voters/deleteAll" if we split the message in "/" we have "voters" and "deleteAll" what means that the 
data base is voters, the request method is deleteAll, and all the value store are going to be deleted.
