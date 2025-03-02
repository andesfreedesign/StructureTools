import os
import FreeCADGui as Gui
import FreeCAD as App

translate=App.Qt.translate
QT_TRANSLATE_NOOP=App.Qt.QT_TRANSLATE_NOOP

ICONPATH = os.path.join(os.path.dirname(__file__), "resources")
TRANSLATIONSPATH = os.path.join(os.path.dirname(__file__), "resources", "translations")

# Add translations path
Gui.addLanguagePath(TRANSLATIONSPATH)
Gui.updateLocale()

class StructureTools(Gui.Workbench):
    """
    class which gets initiated at startup of the gui
    """
    MenuText = translate("Workbench", "StructureTools")
    ToolTip = translate("Workbench", "a simple StructureTools")
    Icon = os.path.join(ICONPATH, "icone.svg")
    toolbox = []

    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self):
        """
        This function is called at the first activation of the workbench.
        here is the place to import all the commands
        """
        from freecad.StructureTools import load_distributed
        from freecad.StructureTools import load_nodal
        from freecad.StructureTools import suport
        from freecad.StructureTools import profile
        from freecad.StructureTools import material
        from freecad.StructureTools import member
        from freecad.StructureTools import calc

        

        # NOTE: Context for this commands must be "Workbench"
        self.appendToolbar('Structure_Load', ["load_distributed","load_nodal"])
        self.appendToolbar('StructureTools', ["member", "suport", "profile", "material"])
        self.appendToolbar('StructureResults', ["calc"])
        self.appendMenu('StructureTools',["load_distributed", "load_nodal","member" ,"suport", "profile", "material", "calc"])

    def Activated(self):
        '''
        code which should be computed when a user switch to this workbench
        '''
        

        App.Console.PrintMessage(translate(
            "Log",
            "Workbench StructureTools activated.") + "\n")

    def Deactivated(self):
        '''
        code which should be computed when this workbench is deactivated
        '''
        App.Console.PrintMessage(translate(
            "Log",
            "Workbench StructureTools de-activated.") + "\n")


Gui.addWorkbench(StructureTools())
