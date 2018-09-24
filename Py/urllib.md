#### urllib.request

>
    1. urllib.request.urlopen()

        params:
               1. url => string or request object
               2. data => send to the server data
               3. timeout => connection timeout
               4. context =>  ...
               5. cadefult => ...
        methods:
               1. getcode() => return Http status code
               2. info() => return website information
               3. getulr() => return website url
               4. read() => return rawl html
    
    2. urllib.request.install_opener(opener)

    3. urllib.request.build_opener() => return an opener director instance which
                                        class the handlers in ther order given
    
    4. urllib.request.Request()

        params:
               1. url => url address
               2. data => must be on object spacifying additional data to the server or None if no such data is needed
               headers => ...
        
        note:
               