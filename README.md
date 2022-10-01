## Decorator
    decorator is function that takes another function
    as a argument and extend the behavior of latter function with explicitly modifying it.


## oops 
    1.in python all are object 
    2. There four ways to write code
        imperative
        functional
        procedural
        object
    3. commonly we use procedure and object oriented program

## Difference in procedure & Object

    ## Procedure
        1. It divided into functions , each function dedicated to specific task, each 
            executed sequenial order
        2. It's used only smaller task. If task bigger code also big , DEBUGGING take longer
        3. Sequrity is not
        4. Access modifier's not present
        5. Top-Down approach  -> This one follows big problems are 
            divided to small chunk of code then small problems Debugged and integrated 

    ## Object
        1. It divided to objects 
        2. It's used to bigger tasks
        3. Data Sequirty is available (Encapsulation)
        4. Access modifiers are avaliable , 
            like  .. private, public, prodected those where used in inheritence
        5. Bottom-up approach -> First solve the small problems in fundametal level 
            then integrate with complete solution

## Class

    Class is an object constructor or blueprint from which object created
    Class are the user defined blue prints that used to create object
    Memory not allocated While class is created

## Object
    Object is instance of class
    Object is the real world entity of class
    When objected created for class, then it will create memory 

    Process of creating Object is called *instantiation*
    
    1. State
            attributes of object, different states for each obj
    2. behaviour
            methods of object , Both diff and similarity of functionality in each object
    3. identity
            Each  object had the own name(unique)

## Encapsulation
    Bundling data member and function inside single class
    Bundling data member and function inside the class is used to data hiding
    Ex :
        We use more module to easy to code, we know where we use these module and how to use, but we don't know how it's working 
        and how to use them in efficient way , This is encapsulation
    Encapsulation is wrap up the data and methods in single units

    Advantage:
        Well defined and readable code
            ex , User don't need to know archetecure for code , they use app in efficintly
        Prevent Modefication/ Deletion
            ex, using Numpy module, if we change that module core function, it will affetec all numpy users, But encapsulation doesn't 
                provide the option
        Sequrity:
            Encapsulation achieved through the access modifiers, so we data should be in sqcurely

    ## Access modifiers :
        ---------------------------------------------------------------------------------------------
        Access Modeifers |   Access from own class | Access from derived Class | Access from object |
        ---------------------------------------------------------------------------------------------
        Private          |      YES                |         NO                |        No          |
        ---------------------------------------------------------------------------------------------
        Protected        |      YES                |         YES               |        NO          |
        ---------------------------------------------------------------------------------------------
        Public           |      YES                |         YES               |        YES         |
        ---------------------------------------------------------------------------------------------

    ## Name mangling
        Name mangling represend _clasName__identifier(private variable/private method)
        name managling is while we can't access the private variable/method using object.
        Those time we can access three ways
            1. dir()
                ex: dir(object name for created class) it shows all include private variable / method also
            2. Through varible
                ex:  obj._className__valiable
            3. Method over-riding

## Inheritance

    ability to  inherit feature/ attribute/ methods from already definied class.
    
    Advantage 
        Modular code base
        code reusablity
        less development
    
    Disadvantage
        decrease the escution speed
        Tightly coupled class

    super():
        to access / initiate the parent class methods/ attribute 
        super(parenClass, objcet)
        This is an code reuasblity advantage