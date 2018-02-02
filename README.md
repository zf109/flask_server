# API server template

## Synopsis

This is a simple template that can be imported to crate a simple API backend server, to serve any process/contents.

## Example

To run the code, in command line type:
```
    $python backend_server.py
```
If server is running successfully, you will see something like:
```
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger pin code: 614-061-919    
```
To check if it is running properly, click [here](http://localhost:5000/api/simple) 
you should see a string like 
```
    "Now you get me!"
```
**Note** that if the IE browser is used, you will see a downloaded text file with the above string.
This is basically the result of a GET method.

In this template, PUT method will allow you to send a string variable to the backend_server
and then the ```simple_process``` will run through the text and return ```"I have received '<input_string>' and I print this out"```.

To test the PUT method, open another console (command window). In the shell type
```
    curl http://localhost:5000/api/simple -d "data='this is me'" -X PUT
```
The result would be:
```
    "I have received 'this is me' and I print this out"
```
Feel free to take this template and wrap your code in ```simple_process```

If there is any problem please contact Zhe Feng(zfeng@deloitte.co.uk)
