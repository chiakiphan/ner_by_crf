1. Structured
    
    main: for process (Don't changes if not necessary)
    
    app.py: for define api

2. Change  

    Can change port, host or method in app.py    
   
    Or command line: 

        flask run --host=<your-host> --port=<your-port>

3. Run
    
    Send request
        
        http://host:port/product?sentence=<your-sentence>
    
    Returned:
        
        Words are product names that are already capitalized
    
    Example:
    
        Request:
        
            http://0.0.0.0:9090/product?sentence= bán dầu gội đầu Sunsilk k hả shop ?
        
         Result:
         
            "bán DẦU GỘI ĐẦU SUNSILK k hả shop ?"
      