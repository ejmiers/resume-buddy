# Resume-Buddy
Who manually reviews resumes anymore? In an increasingly automated world, companies have opted to automate the hiring process by utilizing tools that will parse resumes. Only resumes that match to certain keywords within a job requisition will be flagged for manual review by a recruiter.  
  
As a result, I often hear employee recruiters reccommend that applicants create mulitple resumes with each one being tailored specifically to a particular job requisition. This will give the applicant the best opportunity to have their application flagged for further consideration by the automated system. Creating customized resumes for every job application is inefficient use of time for a potentially marginal increase in "return on investment" when applying to jobs. The time spent creating custom resumes could be spent identifying more job opportunities, refining skills, or practicing for an imminent job interview. What if there was a better way?  
  
Introducing Resume-Buddy, a tool designed to automate the process of tailoring your resume to custom job requisitions. Instead of creating several resumes for specific applications, create just one master resume that contains all of your skills, projects, career experiences, coursework, certificates, and honors/awards that are relavent to the jobs you are applying for. Then submit the requisition url to Resume-Buddy. Resume-Buddy will then scrape the online job requisition for pertinent keywords, and will construct a new resume based on the keyword matches between the job requisition and your master resume. Resume-Buddy will then rate the strength your tailored resume, letting you know how likely it is to be flagged for review, and what you can add to the resume to strengthen it further.  
  
## Tech Details
Resume-Buddy is intended to be a web-application connected to a database (to be specified later). It utilizes the python "flask" microframework as its backend with HTML, javascript, and the jinja2 templating engine on the backend. Bootstrap CDN is currently being used for page styling. The following tools and packages are being used in Resume-Buddy (versions can be seen in the 'requirements.txt' file:  
* python 3.8: https://www.python.org/  
** Server code is written in python  
* Beautiful Soup 4: https://www.crummy.com/software/BeautifulSoup/  
** Will be used for webscraping  
* Flask: http://flask.palletsprojects.com/en/1.1.x/  
** Microframework used for web-application development  
* Flask-Bcrypt:https://flask-bcrypt.readthedocs.io/en/latest/  
** Hashing library used to encrypt user passwords that are stored in a database  
* Flak-Login: https://flask-login.readthedocs.io/en/latest/  
** User-session management  
* Flask-SQLAlchemy: https://flask-sqlalchemy.palletsprojects.com/en/2.x/  
** Object Relational-Mapping (ORM) style interface between flask application and the relational database  
* Flask-WTF: https://flask-wtf.readthedocs.io/en/stable/  
** Object-Oriented form creation for flask  
* lxml: https://lxml.de/  
** XML and HTML processing  
* Requests: https://requests.kennethreitz.org/en/master/
  * HTTP request handling  
  
## Getting Started  
