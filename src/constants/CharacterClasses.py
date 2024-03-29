﻿from enum import Enum


class CharacterClass(Enum):
    IRONCLAD = 0
    SILENT = 1
    DEFECT = 2
    WATCHER = 3
    INVALID = 4

    def __int__(self):
        return self.value


CHARACTERCLASSNAMES = ["Ironclad", "Silent", "Defect", "Watcher"]
CHARACTERCLASSENUMNAMES = ["IRONCLAD", "SILENT", "DEFECT", "WATCHER"]


def getCharacterClassName(cc):
    return CHARACTERCLASSNAMES[int(cc)]
