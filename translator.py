#!/usr/bin/python3

def isplit(word):
    return [char for char in word]

fs = ['\u1680', 'ᚐ', 'ᚁ', 'ᚉ', 'ᚇ', 'ᚓ', 'ᚃ', 'ᚌ', 'ᚆ', 'ᚔ', 'ᚌ', 'ᚊ', 'ᚂ', 'ᚋ', 'ᚅ', 'ᚑ', 'ᚚ', 'ᚊ', 'ᚏ', 'ᚄ', 'ᚈ', 'ᚒ', 'ᚃ', 'ᚒ', 'ᚒ', 'ᚎ', 'ᚔ', 'ᚎ', 'ᚐ', 'ᚁ', 'ᚉ', 'ᚇ', 'ᚓ', 'ᚃ', 'ᚌ', 'ᚆ', 'ᚔ', 'ᚌ', 'ᚊ', 'ᚂ', 'ᚋ', 'ᚅ', 'ᚑ', 'ᚚ', 'ᚊ', 'ᚏ', 'ᚄ', 'ᚈ', 'ᚒ', 'ᚃ', 'ᚒ', 'ᚒ', 'ᚎ', 'ᚔ', 'ᚎ']
ns = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
itext = list(input(">"))
outtext = ""
if itext == ["[","r","e","v","e","r","s","e","]"]:
    itext = isplit(input(">"))
    ns = ['\u1680', 'ᚐ', 'ᚁ', 'ᚉ', 'ᚇ', 'ᚓ', 'ᚃ', 'ᚌ', 'ᚆ', 'ᚔ', 'ᚌ', 'ᚊ', 'ᚂ', 'ᚋ', 'ᚅ', 'ᚑ', 'ᚚ', 'ᚊ', 'ᚏ', 'ᚄ', 'ᚈ', 'ᚒ', 'ᚃ', 'ᚒ', 'ᚒ', 'ᚎ', 'ᚔ', 'ᚎ', 'ᚐ', 'ᚁ', 'ᚉ', 'ᚇ', 'ᚓ', 'ᚃ', 'ᚌ', 'ᚆ', 'ᚔ', 'ᚌ', 'ᚊ', 'ᚂ', 'ᚋ', 'ᚅ', 'ᚑ', 'ᚚ', 'ᚊ', 'ᚏ', 'ᚄ', 'ᚈ', 'ᚒ', 'ᚃ', 'ᚒ', 'ᚒ', 'ᚎ', 'ᚔ', 'ᚎ']
    fs = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for x in range(len(itext)):
        try:
            outtext = outtext + fs[ns.index(itext[x])]
        except:
            outtext = outtext + itext[x]
    print(outtext)
else:
    for x in range(len(itext)):
        try:
            outtext = outtext + fs[ns.index(itext[x])]
        except:
            outtext = outtext + itext[x]
    print(outtext)
