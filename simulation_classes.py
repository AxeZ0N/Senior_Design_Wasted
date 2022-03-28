import pandas as pd
from typing import Any


class Cell:
    
    """
    This is a class to deal with the cell level of the manufacturing prepossess should be full implemented not fully tested as of now
    Attributes:
            name (String): name of cell \n
            number_of_Mahines (int): number of machines in the cell \n
            machines(List): list of machines in the cell \n
            events(list): events to be plotted WIP    
    """

    def __init__(self, number=0, name="", list=[], events=[]):
        """
            The constructor for cell class
      
            Parameters:
                  name (String): name of cell. \n
                  number (int):number of machines in the cell.\n
                  list (List): list of machines in the cell. \n
                  events (list): events to be plotted WIP. \n
      
        """

        self.name = name
        self.number_of_Machines = number
        self.machines = list
        self.events = events

    def setName(self, name=""):
        """
        setter for the name Attribute

        Parameters:
        name (String): name of the cell. Default value is ""\n
        """
        self.name = name

    def getName(self):
        """
          Getter for name

           Returns:
           name(String): name of the cell.
          """
        return self.name

    def getMachines(self):
        """
           Getter for Machines

           Returns:
           machines(list): machines in the cell.
        """
        return self.machines

    def getNumberOfMachines(self):
        """
        Getter for NumberOfMachines
        Returns:
        Number(int): number of machines in the cell.
        """
        return self.number_of_Machines

    def getPowerUsage(self):
        """
        Getter for getPowerUsage 
        needs to be tested may work?
        Returns:
        power(pd.DataFrame): l.
        """
        return pd.concat(map((lambda x: x.getPowerUsage), self.machines))

    def plotPower(self, plt, x, y):
        """
        plots power
        Parameters:
            plt(Figure):matplotlib lib figure \n
            x  (String):x axis of the Power dataframe\n
            y  (string):x axis of the Power dataframe
        """
        power = self.getPowerUsage()
        plt.plot(power[x], power[y])

    def addMachine(self, machine):
        """
        adds a new Machine to the cell
        Parameters:
            machine(Machine): machine object to add to the cell
        """
        self.machines.append(machine)
        self.number_of_Machines = self.number_of_Machines + 1


class Machine:
    """
    This is a class to deal with the Machine level of the manufacturing prepossess should be full implemented not fully tested as of now
    Attributes:
            name (String): name of Machine \n
            numberOfsubMachines (int): number of Submachine in the Machine \n
            subMachiens(List): list of machines in the Machine \n
    """
    def __init__(self, number=0, name="", list=[]):
        self.name = name
        self.numberOfsubMachines = number
        self.subMachiens = list

    def getNumberOfSubMachines(self):
        """
           Getter for SubMachines

           Returns:
           machines(list): subMachines in the Machines.
        """
        return self.number_of_Parts

    def getName(self):
        """
          Getter for name

           Returns:
           name(String): name of the cell.\n
          """
        return self.name

    def getPowerUsage(self):
        """
        Getter for getPowerUsage 
        needs to be tested may work?
        Returns:
        power(pd.DataFrame): l.
        """
        return pd.concat(map((lambda x: x.getPowerUsage), self.subMachines))

    def setName(self, NewName):
        """
        setter for the name Attribute

        Parameters:
        name (String): name of the cell. Default value is ""\n
        """
        name = NewName

    def addSubMachine(self, SubMachine):
        """
        adds a new SubMachine to the Machine
        Parameters:
            SubMachine(subMachine): SubMachine object to add to the Machine
        """
        self.subMachines.append(subMachine)
        self.numberOfsubMachines = self.numberOfsubMachines + 1


class subMachine:
    """
    This is a class to deal with the subMachine level of the manufacturing prepossess and is not full implemented not fully tested as of now. Need ideas ...
    Attributes:
            name (String): name of Machine \n
            power (dataframe) : this need to be worked on 
            """
    def __init__(self, number=0, name="", power=pd.DataFrame()):
        self.name = name
        self.power = power

    def getName(self):
        """
          Getter for name

           Returns:
           name(String): name of the cell.\n
          """
        return self.name

    def getPowerUsage(self):
        """
          Getter for power this need to be worked on. Possibly leave this as default and make other types of subMachiens for different things(inheritance??)

           Returns:
           power(Integer): power used by subMachine.\n
          """
        return self.power

    def setName(self, name):
        """
        setter for the name Attribute

        Parameters:
        name (String): name of the cell. Default value is ""\n
        """
        self.name = name
      
class motor3Phase(subMachine):
     def __init__(self, number=0, name="", power=pd.DataFrame(), HP=0, FullAmps=0, MotorClass='',Code=''):
         super().__init__(self, number, name, power)
         self.HP=HP
         self.FullAmps=FullAmps
         self.MotorClass=MotorClass
         self.code=Code
         
     def getPowerUsage(self):
        return 
        
class motor3PhaseSoftStart(subMachine):
     def __init__(self, number=0, name="", power=pd.DataFrame(), HP=0, FullAmps=0, MotorClass='',Code=''):
         super().__init__(self, number, name, power)
         self.HP=HP
         self.FullAmps=FullAmps
         self.MotorClass=MotorClass
         self.code=Code
         
     def getPowerUsage(self):
        return 
    
    
        
        
        
    