import json
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit,QSpinBox, QDoubleSpinBox)
from PyQt6.QtGui import QPixmap, QImage
import requests
with open('PeriodicTableJSON.json', 'r') as file:
    pTable = json.load(file)["elements"]
print("PREIDODIC TABE!!!!!!!!!! USING JASON!!!!")


while 0:
    inp = input("give atomic numberer or symbol pls: ")

    for element in pTable:

        if element["symbol"] == inp or str(element["number"]) == inp:
            print(f"{element["name"]}:\n {element["symbol"]}\n num: {element["number"]} period: {element["period"]} group: {element["group"]}\n category: {element["category"]}\n state: {element["phase"]}")

class main(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(10,10,500,500)
        #self.setFixedSize(500,500)

        with open('PeriodicTableJSON.json', 'r') as file:
            self.pTable = json.load(file)["elements"]
        self.EL = self.pTable[118]

        self.Density = QLabel("")
        self.Melt = QLabel("")
        self.boil = QLabel("")
        self.molar = QLabel("")

        self.elecAf = QLabel("")
        self.ElecNeg = QLabel("")
        self.ElecNegP = QLabel("")
        self.state = QLabel("")
        self.block = QLabel("")
        self.cat = QLabel("")
        self.disc = QLabel("")
        self.desc = QLabel("")

        self.element = QLineEdit()
        self.Symbol = QLineEdit()
        self.Anum = QSpinBox()
        self.per = QSpinBox()
        self.group = QSpinBox()
        self.elCon = QLineEdit()
        self.elCon2 = QLineEdit()
        self.mass = QDoubleSpinBox()
        self.url = "https://upload.wikimedia.org/wikipedia/commons/0/00/Helium-glow.jpg" 

        self.Mappings = {
            self.element: "name",
            self.Symbol: "symbol",
            self.Anum: "number",                  
            self.per: "period",                  
            self.group: "group",                
            self.elCon: "electron_configuration",
            self.elCon2: "electron_configuration_semantic",
            self.mass: "atomic_mass",
            self.Density: "density",
            self.Melt: "melt",
            self.boil: "boil",
            self.molar: "molar_heat",
            self.elecAf: "electron_affinity",
            self.ElecNegP: "electronegativity_pauling",
            self.ElecNeg: "ionization_energies",
            self.state: "phase",
            self.cat: "category",
            self.block: "block",
            self.disc: "discovered_by",
            self.desc: "summary",
            

        }
        
        
        self.LabelTs()
        self.show()

        self.top = self.Thing.y()

        self.CreateLabels()
        self.Set()
        
    def freakingThing(self, Lay, Thing):
        Thing.addWidget(Lay)
        Lay.returnPressed.connect(lambda: self.OnChange(Lay))
    def freakingThing2(self, Lay, Thing):
        Thing.addWidget(Lay)
        Lay.valueChanged.connect(lambda: self.OnChange(Lay))

    def CreateLabels(self):
        self.Collection = []
        for Elle in self.pTable:
            self.Collection.append(ElemLabel(Elle, self, self.top))
    def GetImage(self):
        
        output = requests.get(self.url).content
        
        self.image = QPixmap()
        self.image.loadFromData(output)
        self.ShowImage.setPixmap(self.image)



    def LabelTs(self):
        self.vertLay = QVBoxLayout()
        self.vertLay.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.vertLay.addWidget(QLabel("WELCOME TO PERIODIC TABLE SEARCH!!!"))

        symline = QHBoxLayout()
        symline.addWidget(QLabel("Element: "))

        self.freakingThing(self.element, symline)

        symline.addWidget(QLabel("Symbol: "))

        self.freakingThing(self.Symbol, symline)

        self.vertLay.addLayout(symline)

        nums = QHBoxLayout()
        
        nums.addWidget(QLabel("Atomic Number: "))

        self.Anum.setMinimum(1)
        self.Anum.setMaximum(118)

        self.freakingThing2(self.Anum, nums)


        nums.addWidget(QLabel("Period: "))

        self.per.setMinimum(1)
        self.per.setMaximum(7)

        self.freakingThing2(self.per, nums)

        nums.addWidget(QLabel("group: "))

        self.group.setMinimum(1)
        self.group.setMaximum(18)

        self.freakingThing2(self.group, nums)

        self.vertLay.addLayout(nums)

        econ = QHBoxLayout()
        econ.addWidget(QLabel("Electron Config: "))

        self.freakingThing(self.elCon, econ)

        self.vertLay.addLayout(econ)

        econ = QHBoxLayout()
        econ.addWidget(QLabel("Electron Config simplified: "))

        self.freakingThing(self.elCon2, econ)

        self.vertLay.addLayout(econ)

        NumValues = QHBoxLayout()

        NumValues.addWidget(QLabel("Electron Affinity: "))
        NumValues.addWidget(self.elecAf)
        NumValues.addWidget(QLabel("Electronegativity: "))
        NumValues.addWidget(self.ElecNegP)
        self.vertLay.addWidget(QLabel("Ionization Energies: "))
        self.vertLay.addWidget(self.ElecNeg)
        
        self.vertLay.addLayout(NumValues)

        MassEtc = QHBoxLayout()
        MassEtc.addWidget(QLabel("Atomic Mass: "))

        self.mass.setDecimals(9)
        self.freakingThing2(self.mass, MassEtc)
        MassEtc.addWidget(QLabel("Density: "))
        MassEtc.addWidget(self.Density)
        self.vertLay.addLayout(MassEtc)

        self.vertLay.addLayout(MassEtc)

        NumValues = QHBoxLayout()

        NumValues.addWidget(QLabel("Melting Point: "))
        NumValues.addWidget(self.Melt)
        NumValues.addWidget(QLabel("Boiling Point: "))
        NumValues.addWidget(self.boil)
        NumValues.addWidget(QLabel("Molar Heat: "))
        NumValues.addWidget(self.molar)
        
        self.vertLay.addLayout(NumValues)

        NumValues = QHBoxLayout()

        NumValues.addWidget(QLabel("State: "))
        NumValues.addWidget(self.state)
        NumValues.addWidget(QLabel("Category: "))
        NumValues.addWidget(self.cat)
        NumValues.addWidget(QLabel("block: "))
        NumValues.addWidget(self.block)
        

        NumValues.addWidget(QLabel("Discovered by: "))
        NumValues.addWidget(self.disc)
        self.vertLay.addLayout(NumValues)

        NumValues = QHBoxLayout()

        NumValues.addWidget(QLabel("Description: "))
        NumValues.addWidget(self.desc)

        self.vertLay.addLayout(NumValues)

        #self.ShowImage = QLabel()
        #self.vertLay.addWidget(self.ShowImage)

        self.Thing = QLabel("")

        

        self.vertLay.addWidget(self.Thing)

        

        self.setLayout(self.vertLay)
 
    def OnChange(self, changed):
        
        if changed in self.Mappings:
            garfiel = self.Mappings[changed]
            try:
                self.EL = self.FindEl(changed.text(), garfiel)
            except:
                self.EL = self.FindEl(str(changed.value()), garfiel)
        self.Set()
        

        #self.element.setText(self.EL["name"])
    def Set(self):
        for Thing, Data in self.Mappings.items():
            
                try:
                    Value = self.EL[Data]
                except:
                    Value = pTable[118][Data]

                try:
                    Thing.setText(str(Value))
                except:
                    Thing.setValue(Value)
            


        for elle in self.Collection:
            if elle.El == self.EL:
                elle.Label.setStyleSheet("background-color: gray;")
            else:
                
                elle.Label.setStyleSheet(elle.sheet)
        #self.GetImage()
        

    def FindEl(self, inp, form):
        if form != "period" and form != "group":
            for element in pTable:
                if str(element[form]).lower() == inp.lower():
                    return element
        else:
            Found = False
            for element in pTable:
                if element["group"] == self.group.value() and element["period"] == self.per.value():
                    Found = True
                    return element
            if Found == False:
                return pTable[118]

class ElemLabel():
    def __init__(self, element, pa, top):
        self.parent = pa
        self.top = top
        self.El = element
        self.Size = 35
        self.Label = QPushButton(self.El["symbol"], parent=self.parent)
        self.Place()
        self.Label.clicked.connect(self.Click)
        self.Label.show()

    def Place(self):
        self.Label.setGeometry(self.Size*(self.El["xpos"]-1), self.top+self.Size*(self.El["ypos"]-1), self.Size,self.Size)
        
        match self.El["phase"]:
            case "Gas":
                self.Label.setStyleSheet("color: white;")
            case "Solid":
                self.Label.setStyleSheet("color: black;")
            case "Liquid":
                self.Label.setStyleSheet("color: blue;")
        sheet = self.Label.styleSheet()
        match self.El["category"]:
            case "metalloid":
                sheet = sheet + "background-color: yellow;"
            case "alkali metal":
                sheet = sheet + "background-color: darkMagenta;"
            case "alkaline earth metal":
                sheet = sheet + "background-color: magenta;"
            case "lanthanide":
                sheet = sheet + "background-color: blue;"
            case "actinide":
                sheet = sheet + "background-color: cyan;"
            case "transition metal":
                sheet = sheet + "background-color: lightBlue;"
            case "noble gas":
                sheet = sheet + "background-color: darkRed;"
            case "diatomic nonmetal":
                sheet = sheet + "background-color: red;"
            case "post-transition metal":
                sheet = sheet + "background-color: lightGreen;"
            case "polyatomic nonmetal":
                sheet = sheet + "background-color: orange;"

            case "unknown, probably transition metal":
                            sheet = sheet + "background-color: lightBlue;"
            case "unknown, probably metalloid":
                sheet = sheet + "background-color: yellow;"
            case "unknown, probably post-transition metal":
                    sheet = sheet + "background-color: lightGreen;" 
            
        self.sheet = sheet
        self.Label.setStyleSheet(sheet)

    
    def Click(self):
        self.parent.EL = self.El
        self.parent.Set()

app = QApplication(sys.argv)
main = main()
app.exec()