from enum import Enum

#
# Created by gamerpuppy on 6/24/2021.
#



class sts: #this class replaces the original namespace 'sts'

    class CharacterClass(Enum):
        IRONCLAD = 0
        SILENT = 1
        DEFECT = 2
        WATCHER = 3
        INVALID = 4

    CHARACTERCLASSNAMES = ["Ironclad", "Silent", "Defect", "Watcher"]
    CHARACTERCLASSENUMNAMES = ["IRONCLAD", "SILENT", "DEFECT", "WATCHER"]

    @staticmethod
    def getCharacterClassName(cc):
        return sts.CHARACTERCLASSNAMES[int(cc)]


