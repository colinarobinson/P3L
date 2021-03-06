﻿from dcavarCorpus import *

oFile = open("dante.stats", 'w')

iStopWords = ["a","adesso","ai","al","alla","allo","allora","altre","altri","altro","anche","ancora","avere","aveva","avevano","ben","buono","che","chi","cinque","comprare","con","consecutivi","consecutivo","cosa","cui","da","del","della","dello","dentro","deve","devo","di","doppio","due","e","ecco","fare","fine","fino","fra","gente","giu","ha","hai","hanno","ho","il","indietroinvece","io","la","lavoro","le","lei","lo","loro","lui","lungo","ma","me","meglio","molta","molti","molto","nei","nella","no","noi","nome","nostro","nove","nuovi","nuovo","o","oltre","ora","otto","peggio","pero","persone","piu","poco","primo","promesso","qua","quarto","quasi","quattro","quello","questo","qui","quindi","quinto","rispetto","sara","secondo","sei","sembrasembrava","senza","sette","sia","siamo","siete","solo","sono","sopra","soprattutto","sotto","stati","stato","stesso","su","subito","sul","sulla","tanto","te","tempo","terzo","tra","tre","triplo","ultimo","un","una","uno","va","vai","voi","volte","vostro"]

iStopWords = iStopWords + [ x.capitalize() for x in iStopWords ]

mytext = getTextFromFile("Dante.txt").lower()

mytokens = tokenize( mytext )

junksymbols = " ,;:-+=()[]'\"?!$%.<>`"

removeJunk(mytokens, junksymbols)

mytokens = [ x  for x in mytokens if x ]

mytokens = [ x  for x in mytokens if x not in iStopWords ]

unigrams = getNGramModel(mytokens, 1)
bigrams  = getNGramModel(mytokens, 2)
trigrams = getNGramModel(mytokens, 3)

print( [a for a in unigrams] , file = oFile)
prettyPrintFRP(bigrams, myreverse=False , file = oFile)
prettyPrintFRP(trigrams, myreverse=False , file = oFile)

whitespaceChars = [' ','\n','\t']
characters = makeFrequencyProfile( [a for a in mytext if a not in whitespaceChars] )

prettyPrintFRP(characters, myreverse=False, file = oFile)


oFile.close()