# Resume-Buddy
Who manually reviews resumes anymore? In an increasingly automated world, companies have opted to automate the hiring process by utilizing tools that will parse resumes. Only resumes that match to certain keywords within a job requisition will be flagged for manual review by a recruiter.  
  
As a result, I often hear employee recruiters reccommend that applicants create mulitple resumes with each one being tailored specifically to a particular job requisition. This will give the applicant the best opportunity to have their application flagged for further consideration by the automated system. Creating customized resumes for every job application is inefficient use of time for a potentially marginal increase in "return on investment" when applying to jobs. The time spent creating custom resumes could be spent identifying more job opportunities, refining skills, or practicing for an imminent job interview. What if there was a better way?  
  
Introducing Resume-Buddy, a tool designed to automate the process of tailoring your resume to custom job requisitions. Instead of creating several resumes for specific applications, create just one master resume that contains all of your skills, projects, career experiences, coursework, certificates, and honors/awards that are relavent to the jobs you are applying for. Then submit the requisition url to Resume-Buddy. Resume-Buddy will then scrape the online job requisition for pertinent keywords, and will construct a new resume based on the keyword matches between the job requisition and your master resume. Resume-Buddy will then rate the strength your tailored resume, letting you know how likely it is to be flagged for review, and what you can add to the resume to strengthen it further.  
  
## Tech Details
Resume-Buddy is intended to be a web-application connected to a database (to be specified later). It utilizes the python "flask" microframework as its backend with HTML, javascript, and the jinja2 templating engine on the backend. Bootstrap CDN is currently being used for page styling. The following tools and packages are being used in Resume-Buddy (versions can be seen in the 'requirements.txt' file:  
* python 3.8: https://www.python.org/
  * Server code is written in python  
* Beautiful Soup 4: https://www.crummy.com/software/BeautifulSoup/
  * Will be used for webscraping  
* Flask: http://flask.palletsprojects.com/en/1.1.x/
  * Microframework used for web-application development  
* Flask-Bcrypt:https://flask-bcrypt.readthedocs.io/en/latest/
  * Hashing library used to encrypt user passwords that are stored in a database  
* Flak-Login: https://flask-login.readthedocs.io/en/latest/
  * User-session management  
* Flask-SQLAlchemy: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
  * Object Relational-Mapping (ORM) style interface between flask application and the relational database  
* Flask-WTF: https://flask-wtf.readthedocs.io/en/stable/
  * Object-Oriented form creation for flask  
* lxml: https://lxml.de/
  * XML and HTML processing  
* Requests: https://requests.kennethreitz.org/en/master/
  * HTTP request handling  
  
## Getting Started  
Follow the steps below for setting up your environment and installing.  
  
## Contributing 
Contributions are welcomed (and needed!). Below are some ways you can get involved in this project:  
  
* **Feature Development** - Help develop functional or miscellaneous features. Document all code additions and create a pull request with an explanation and justification for the addition. Make sure code conforms to conventions and standards used throughout this project. If there are pre-existing testcases, make sure they still pass prior to opening a pull request.  
* **Bug Reporting and Bugfixes** - Report bugs discovered in code. Create an issue that documents the description of the bug and instructions on how to reproduce it. Use screenshots where necessary. If you produce a bugfix, document all changes to code and open a pull request. Ensure that changes conform to established code conventions and that testcases (if any) are passing prior to opening a pull request.  
* **Testing** - Write testcases for code. Tests should follow the same conventions that feature code uses. Document testcases and open a pull request.  
* **Documentation** - Write and maintain documentation for the project and code. This includes code comments, READMEs, and feature guides. Create a pull request with an explanation for the needed documentation change (or addition).  
  
### Standards and Conventions  
Code styling, documentation, and branch development should generally follow these standards to ensure consistency accross the project. These conventions are described below:  

* **Python Code Conventions and Standards**
  * functions and variables are written in camel-case. An example of a variable written in this style: `thisVariableIsInCamelCase`. A function written in this style looks like this: `thisFunctionIsInCamelCase()`
  * class names are written in pascal case. An example of a class name in this style: `ThisClassIsInPascalCase`
  * flask defined routes are lowercase and hyphenated. Example: `/this-is-a-route`
    * Any route that requires a variable to be passed should be done like this: `/variable='<variable>'`
    * Sub-routes are allowed. This can be done like this: /parent-route/sub-route
  * Whitespace should be used for clarity where needed. Do not include large blocks of whitespace.
  * Any major blocks of code should be appropriately commented, describing what the block does. Trivial code lines do not have to require comments.
  * All functions and classes should be documented using Google-Style Docstrings. This should document the function or class' purpose, any arguments, any attributes, and any return values. An example of this style is described here: https://www.datacamp.com/community/tutorials/docstrings-python#sixth-sub
  * Remove any superfluous imports. Where possible, import specific functions from a package instead of importing the entire package.
  * If any I/O should be performed, do this using a `with` statement. This ensures that I/O streams will be properly handled. Include exception handling where necessary.
  * Try not to repeat code. If you find yourself repeating code, write a function!  

* **HTML and JINJA2 Conventions and standards**
  * 
  *
  
  
  
  
