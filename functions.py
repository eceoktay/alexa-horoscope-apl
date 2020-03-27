import json

def removeChars(chars):
    return chars.replace("$", "").replace("{", "").replace("}", "").replace("payload.", "")

def splitIntoElements(array):
    arr = array.split(".")
    newArray = []
    for i in range(len(arr)):
        if ("[" in arr[i]) and ("]" in arr[i]):
            items = arr[i].split("[")
            if len(items) != 2:
                print("it wont work well")
            newArray.append(items[0])
            item = items[1].replace("[", "").replace("]", "")
            newArray.append(item)
        else:
            newArray.append(arr[i])
    return newArray

def getAllElements(obj):
    if isinstance(obj, dict):
        for item in obj.values():
            yield from getAllElements(item)
    elif any(isinstance(obj, t) for t in (list, tuple)):
        for item in obj:
            yield from getAllElements(item)
    else:
        yield obj

def getElementsWithVariable(arr):
    newArray = []
    for item in arr:
        item = str(item)
        if ("${" in item) and ("==" not in item):
            newArray.append(item)
    return newArray

def getRealValue(dataSources, var):
    var = removeChars(var)
    elements = splitIntoElements(var)
    temp = dataSources
    for el in elements:
        if el.isdigit():
            el = int(el)
        print(el)
        temp = temp[el]
    return temp

def updateDocument(document, dataSources):
    allElements = getAllElements(document)
    variables = getElementsWithVariable(allElements)
    doc = json.dumps(document)
    for var in variables:
        newValue = getRealValue(dataSources, var)
        doc = doc.replace(var, newValue)
    return json.loads(doc, strict=False)
