from bottle import *
import os

@route("/")
def vid():
    return """
        <!DOCTYPE html>
               <html>

                   <body>
                       <ul>
                           <li><a href="/a">Project A</a></li>
                           <li><a href="/b">Project B</a></li>
                       </ul>

                   </body>
               </html>
               
               """






@route("/a")
def vid():
    return """
        <!DOCTYPE html>
               <html>

                   <body>
                       <ul>
                           <li><a href="/1">Dragon Age Origin</a></li>
                           <li><a href="/2">Dragon Age 2</a></li>
                           <li><a href="/3">Dragon Age Inquisition </a></li>
                           <li><a href="/">Back</a></li>
                       </ul>

                   </body>
               </html>



        """



@route("/1")
def vid():
    return "Dragon Age Origin Works" """
        <!DOCTYPE html>
               <html>

                   <body>
                       <ul>
                           <li><a href="/a">Back</a></li>
                       </ul>

                   </body>
               </html>



        """


@route("/2")
def vid():
    return "Dragon Age 2 Works" """
        <!DOCTYPE html>
               <html>

                   <body>
                       <ul>
                           <li><a href="/a">Back</a></li>
                       </ul>

                   </body>
               </html>



        """

@route("/3")
def vid():
    return "Dragon Age Inquisition Works" """
        <!DOCTYPE html>
               <html>

                   <body>
                       <ul>
                           <li><a href="/a">Back</a></li>
                       </ul>

                   </body>
               </html>



        """




@route("/b")
def vid():
    return """
    <a href="/b1"><img src="pictures/Dragon_Age_Origin.jpg"></a>
    <a href="/b2"><img src="pictures/Dragon_Age_2.jpg"></a>
    <a href="/b3"><img src="pictures/Dragon_Age_Inquisition.jpg"></a>
    <li><a href="/">Back</a></li>
    
    """

@route("/b1")
def vid():
    return "You picked Dragon Age Origin " """
            <!DOCTYPE html>
                   <html>

                       <body>
                           <ul>
                               <li><a href="/b">Back</a></li>
                           </ul>

                       </body>
                   </html>



            """

@route("/b2")
def vid():
    return "You picked Dragon Age 2 " """
            <!DOCTYPE html>
                   <html>

                       <body>
                           <ul>
                               <li><a href="/b">Back</a></li>
                           </ul>

                       </body>
                   </html>



            """

@route("/b3")
def vid():
    return "You picked Dragon Age Inquisition " """
            <!DOCTYPE html>
                   <html>

                       <body>
                           <ul>
                               <li><a href="/b">Back</a></li>
                           </ul>

                       </body>
                   </html>



            """





@route('/pictures/<filename>')
def server_static(filename):
    return static_file(filename, root="./pictures")

@error(404)
def error404(error):
    return '<p>This webside dose not exist</p><a href="/">back</>'

run(host='0.0.0.0', port=os.einviron.get('PORT'))
