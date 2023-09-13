# Assignment 2

Link to the app -> [Click Here!](https://adam-inventory.adaptable.app/main/)

## Questions:
### 1. Create a new Django Project
1. Create a new Django Project
    - First we need to create a virtual environment by executing the following command:
    ```
    python -m venv env
    ```
2. After that we need to activate the virtual environment by executing the following command:
    - Windows
    ```
    env\Scripts\activate.bat
    ```
    - Mac OS
    ```
    source env/bin/activate
    ```
3. Create a `requirements.txt` in the project directory to install all the dependencies that are needed

4. To install all the dependencies to the virtual environment is by running this command:
	```
	py -m pip install requirements.txt
	```

5. Last but not least, try to run the project by running the following command:
	```
	django-admin startproject Assignment2 .
	```

### 2. Create an app with the name main.
1. Create a new Django App
    ```
    py manage.py startapp main
    ```
2. Create a directory named templates in the main app, and then create a file named main.html

3. Add a simple code to the main.html file with this following code:
   ```
   <h1>{{ appname }}</h1>

    <h5>Name:</h5>
    <p>{{ name }}</p>

    <h5>Class:</h5>
    <p>{{ class }}</p>
   ```

4. Add this method the views.py to  fill all the variables that are in the main.html file(appname, name, class)
    ```
    def show_main(request):
    context = {
        'appname': 'Adam Inventory',
        'name': 'Adam Muhammad',
        'class': 'KKI'
    }

    return render(request, 'main.html', context)
    ```

### 3. Create a URL routing configuration to access the main app.
1. Edit `urls.py` in the main app to configure the routing with this configuration:
    ```
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
2. Configure app routes to the main project
    - edit `urls.py` in Assignment2(project directory) with this code:
    ```
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('main/', include('main.urls')),
    ]
    ```
3. Register the app to the project by editting the `settings.py` file in Django project directory:
    - add the app name to **INSTALLED_APPS** variable, the code will be look like this:
        ```
        INSTALLED_APPS = [
            ...
            'main',
            ]
        ```
    - edit **ALLOWED_HOSTS** variable to:
        ```
        ALLOWED_HOSTS = ["*"]
        ```
      as a development purpose only we allow all the host to access the website
### 4. Create a model in main app
1. Add the mandatory attributes such as name with ChardField data type, amount with IntegerField data type, description with TextField data type, and additional attributes, the code should look like this:
    ```
    from django.db import models

    class Item(models.Model):
        name = models.CharField(max_length=255)
        amount = models.IntegerField()
        price = models.DecimalField(max_digits=19, decimal_places=2)
        category = models.TextField()
        description = models.TextField()
    ```
### 5. Diagram Flow.
<img src="./assets/flowPbP.png">

First, user make a request to Django-Based website, and then it will trigger `urls.py` to find wich route that user want to access for example, if user make a request with a route(url) `localhost:8000/main` then after that it will trigger the `views.py` to find wich method that routes associated, after that render the html file and `views.py` could be communicate with `models.py` if the html file needs any data to be rendered. After `models.py` communicate with Database then the models return the data to `views.py` and display it to html file that was requested.


### 6. Purpose of a virtual environment, can we create a Django web app without a virtual environment?
A virtual environment in the context of Python is a self-contained directory that contains its own Python interpreter and a set of libraries. Its primary purpose is to isolate Python projects and their dependencies, ensuring that each project has its own clean and independent environment. Regarding Django web apps: While it is technically possible to create a Django web app without a virtual environment, it is highly discouraged for the reasons mentioned above. Django projects often rely on specific versions of Django and other Python packages, and using a virtual environment ensures that you can manage these dependencies without interfering with other Python projects on your system.

### 7. What is MVC, MVT, and MVVM? Explain the differences between the three.
MVC (Model-View-Controller), MVT (Model-View-Template), and MVVM (Model-View-ViewModel) are architectural patterns used in software development to structure the code and separate concerns in an application.
While they share some similarities, they have distinct differences in how they organize and manage the components of an application:
#### 1. MVC (Model-View-Controller):
- Model: Represents the application's data and business logic. It encapsulates the data and defines how it can be accessed and manipulated.
- View: Responsible for displaying the data to the user. It presents the information and interacts with the user interface.
- Controller: Acts as an intermediary between the Model and the View. It receives user input from the View, processes it, and updates the Model or the View accordingly. It handles the application's flow and logic.

**Differences**
- MVC is typically associated with traditional server-side web applications, desktop applications, and GUI frameworks.
- The Controller plays a central role in managing user input and application flow.
- MVC does not prescribe a specific template engine for rendering views.

#### 2. MVT (Model-View-Template):
- Model: Similar to MVC, it represents the application's data and business logic.
- View: In MVT, the View is responsible for defining how data is presented to the user. However, in some frameworks like Django (a Python web framework), the View also handles some of the controller's responsibilities.
- Template: The Template in MVT is responsible for defining the structure and layout of the user interface. It specifies how data should be displayed but doesn't contain application logic.

**Differences**
- MVT is closely associated with web frameworks like Django and Ruby on Rails, where the Template system is a key part of rendering web pages.
- The Template separates the presentation logic from the View and is focused on defining the HTML structure.
- In some MVT frameworks like Django, the View includes routing and some controller-like functionality.

#### 3. MVVM (Model-View-ViewModel):
- Model: Represents the application's data and business logic, similar to MVC and MVT.
- View: Represents the user interface, just like in MVC and MVT.
- ViewModel: Sits between the View and the Model. It contains the presentation logic and exposes data and commands that the View can bind to. The ViewModel is responsible for transforming and formatting the data for display.

**Differences**
- MVVM is commonly used in client-side application development, especially with frameworks like Angular.
- The ViewModel is the central component in MVVM, separating the View from the Model and containing most of the presentation logic.
- Data binding is a key concept in MVVM, allowing automatic synchronization between the ViewModel and the View.