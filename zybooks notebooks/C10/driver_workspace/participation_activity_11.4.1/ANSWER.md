1) Importing a module executes the statements contained within the imported module.
True. 
When a module is imported, the code in the global scope of that module is executed. This can lead to unintended side effects if the module contains statements that perform actions (e.g., print statements, input statements) when imported
2) The value of the __name__ variable of the executing script is always "__main__".
True.
The __name__ variable is a special built-in variable in Python that is automatically set to "__main__" when the file is executed as the main program. If the file is imported as a module, __name__ is set to the name of the module instead.
3) If a module is imported with the statement import MyMod, then MyMod.__name__ is equal to "__main__".
False.
When a module is imported, the __name__ variable of that module is set to the name of the module (e.g., "MyMod"), not "__main__". The __name__ variable is only set to "__main__" for the file that is being executed as the main program, not for imported modules.

# Participation Activity 11.4.1
1) True
2) True
3) False