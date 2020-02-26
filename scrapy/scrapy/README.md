# Hi Scrapy Project start on

![scapy](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRU049A3Niy-PO0xC7mf_Plil2kVeyKf_b-yWDHE0mxJqZ7OH93)


# CLI


        $ cd < root folder >
        
        $ pip install Scrapy
        
        $ scrapy startproject < project_name >
        
        $ scrapy startproject QsSpider
        
        after create pkg
        
        $ cd to down level pkg
        
        $ scrapy crawl < spider name >


# Project Srutcture

        
                         upper level      down level
        < root folder > - < pkg name > - < pkg name > 
                                    
                                       - scrapy.cfg        
                                                      - < spiders >         ---  __ init __ .py  
                                                         
                                                      -  __  init  __ .py   ---  < new_module_script > --- name = ' spider_name '
                                                                                
                                                      - items.py
                                                                                
                                                      - middlewares.py
                                                                                
                                                      - pipelines.py
                                                                                
                                                      - settings.py  
        
        
        
        
        
        

