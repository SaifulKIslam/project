# Random car generator 

## Contents
- [Brief](#brief)
    - [Objective](#obj)
    - [Project Approach](#approach)
- [Architecture](#arch)
    - [Service architecture](#soa) 
    - [Container architecture](#cla)
- [Continuous Integration pipeline](#ci)
- [Testing](#test_)
- [Risk Assessment](#risks)
- [Project Planning & Tracking](#use_case)
- [Future Improvements](#improve)

<a name="brief"></a>
## Brief

<a name="obj"></a>
### Objective
The objective of this prohect is to create an application that generates “Objects” upon a set of predefined rules.
These “Objects” can be from whatever domain you wish.

<a name="approach"></a>
### Project Approach
To meet the projects model requirements, I decided to create an application with 4 services that communicate with eachother to generate a random car for the user. 

#### Service 1
The core service is to perform a **GET request on services 2, 3** and a **POST request on service 4**. Service 1 communicates with service 2, 3, 4 & presists some data a mysqldatabase.The responses given by service 2, 3 & 4 are then used by service 1 to display back to the user via HTML.

**routes located:  service1/application/routes.py**
```bash
@app.route('/', methods=['GET','POST'])
def index():
    #get make
    make = requests.get("http://car_service2:5001/make")
    #get shape
    shape = requests.get("http://car_service3:5002/shape")
    #post model
    info = str(make.text) + " " + str(shape.text)
    model = requests.post("http://car_service4:5003/model", data=info)


    return render_template('index.html', title='model shape', make=make.text, shape=shape.text, info=info, model=model.text)
```

#### Service 2
Service 2 generates a random car make. I assigned 3 possible variations to this service. one of the 3 variatiosn will be chosen randomly. This service will send a GET request. 

**routes located:  service2/application/routes.py**
```
@app.route('/make', methods=['GET'])
def make():
    
    makes = ["Audi", "BMW", "Mercedes"]
    make = makes[random.randrange(0,3)]

    return Response(make, mimetype="text/plain")
```

#### Service 3
Service 3 generates a random shape to go with the selected car make. There are 3 variations for this service also and again is randomly generated. This again is a GET request.

**routes located:  service3/application/routes.py**
```bash

@app.route('/shape', methods=['GET'])
def team():

    teams = ["Hatchback", "Saloon", "SUV"]

    team = teams[random.randrange(0,3)]
    
    return Response(team, mimetype="text/plain")
```

#### Service 4
Service 4 is used to generate a random car more which coincides with both service 2 (make of the cra) and service 3 (shape of the car). Service 4 will then return the car model back to service 1 as a POST response to display to the user. 

**routes located:  service4/application/routes.py**

@app.route('/model', methods=['GET','POST'])
def model():

    info = request.data.decode('utf-8')
    data = info.split(" ")
    shape = data[0]
    make = data[1]

    if make == "Audi":
        if shape == 'Hatchback':
            model = 'A3'
        elif shape == 'Saloon':
            model = 'A6'
        elif shape == 'SUV':
            model = 'Q7'
    elif make == "BMW":
        if shape == 'Hatchback':
            model = '1-Series'
        elif shape == 'Saloon':
            model = '5-Series'
        elif shape == 'SUV':
            model = 'X5'
    elif make == "Mercedes":
        if shape == 'Hatchback':
            model = 'A-Class'
        elif shape == 'Saloon':
            model = 'E-Class'
        elif shape == 'SUV':
            model = 'GLE'
    else:
        return "model not found"

    
    return Response(model, mimetype="text/plain")
``'

<a name="arch"></a>
## Architecture

<a name="soa"></a>
### Service Architecture 
Below is the service architecture of my application. 

<img src="/images/service.png" alt="" width="100%" height="100%"/>

<a name="cla"></a>
### Container level architecture
Below is the Container architecture for my application:

<img src="/images/conatiner.png" alt="" width="100%" height="100%"/>

<a name=ci></a>
## CI Pipeline
I had issues connecting to Jenkins.

<img src="/images/jenkins.png" alt="" width="100%" height="100%"/>

<a name="test"></a>
## Testing
In teh initial staged my test coverage was high; however later on when my project developed issues i re-ran the tests and my coverage was low.


<a name=risks></a>
## Risk Assessment
I have thought of a number of risks that my project may face and have categorised them below to analyse the risk, its impact, likelihood and the appropriate response to that risk. The risks can be seen as a combination of technical risks associate with the development side of the project and general risks that will directly or indirectly impact the project. I also revisted the risks and wrote furtehr comments.

<img src="/images/Risk_assessment.png" alt="" width="100%" height="100%"/>

<a name="use_case"></a>
## Project Planning & Tracking
I was unabel to carry out my full Project Plan as i faced issues. 

<img src="/images/plan.png" alt="" width="100%" height="100%"/>

<a name="improve"></a>
## Future Improvements

- Solve issues to compelete project on time. 
- 
