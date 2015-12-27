import components

class App:
    def __init__(this):
        this.__logger = components.getLogger()
        this.__viewer = components.getViewer()
        this.__loader = components.getLoader()
        this.__renderer = components.getRenderer()
        this.__input = components.getInput()

    def getLogger(this):
        return this.__logger

    def getViewer(this):
        return this.__viewer

    def getLoader(this):
        return this.__loader

    def getRenderer(this):
        return this.__renderer

    def getInput(this):
        return this.__input

##    def discoverAssetPaths(this):
##        assetPaths = dict()
##        
##        ## For now, just assume 'config.ini' contains an [assets] record.
##        assetsRecordFound = False
##        with open("config.ini", "r") as configFile:
##            for line in configFile:
##                ## Strip the line ending.
##                line = line.strip("\r\n")
##                if not assetsRecordFound and line == "[assets]":
##                    assetsRecordFound = True
##                    ## GOTO the next line
##                    continue
##                if assetsRecordFound:
##                    ## Allow finishing of reading the assets record early.
##                    if len(line) == 0:
##                        break
##
##                    ## Process the assette record fields.
##                    if line.startswith("image:"):
##                        ## Load the image key and path.
##                        parts = line.split(":")[1].split("=")
##                        key = parts[0]
##                        path = parts[1]
##                        del parts
##                        assetPaths[key] = ("image", path)
##                        
##        return assetPaths
