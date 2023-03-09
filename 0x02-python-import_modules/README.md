#### Python - import & modules

#### Modules
A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable __name__. 
A module can contain executable statements as well as function definitions. These statements are intended to initialize the module. They are executed only the first time the module name is encountered in an import statement. 1 (They are also run if the file is executed as a script.)
#### Importing
The process by which Python code in one module is made available to Python code in another module.
Python code in one module gains access to the code in another module by the process of importing it. The import statement is the most common way of invoking the import machinery, but it is not the only way. Functions such as importlib.import_module() and built-in __import__() can also be used to invoke the import machinery.
The basic import statement (no from clause) is executed in two steps:

find a module, loading and initializing it if necessary

define a name or names in the local namespace for the scope where the import statement occurs.
