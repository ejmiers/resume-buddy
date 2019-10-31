## Contributing 
Contributions are welcomed (and needed!). The ways you can get involved in the project are described below:
  
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
  * Remove any superfluous imports. Where possible, import specific functions from a package instead of importing the entire package. If you need to add a new import to the project:
    * Update the 'requirements.txt' file after installing the package. This can be done through the command: `pip3 freeze > requirements.txt`
    * Document the package in the README under the [Tech Details](#README.md#Tech-Details) section.
    * Create a justification for the new package from within the pull request.
  * If any I/O should be performed, do this using a `with` statement. This ensures that I/O streams will be properly handled. Include exception handling where necessary.
  * Try not to repeat code. If you find yourself repeating code, write a function!  

* **HTML and JINJA2 Conventions and standards**
