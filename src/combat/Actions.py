#The following statement is interrupted by a preprocessor statement.

#The original statement from the file Actions.cpp starts with:
#    return {[=] (BattleContext &bc) { int openIdxCount = 0; int newGremlinIdxs[2]; if (bc.monsters.arr[1].isDying()) { newGremlinIdxs[openIdxCount++] = 1; } if (bc.monsters.arr[2].isDying()) { newGremlinIdxs[openIdxCount++] = 2; } if (openIdxCount < 2 && bc.monsters.arr[0].isDying()) { newGremlinIdxs[openIdxCount++] = 0; }

#These cannot be handled by this converter.
#Modify this statement so that it is not interrupted by preprocessor statements and try the conversion again.