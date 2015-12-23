class AssetManager:
    def __init__(this, discoveredAssets, loader, logger = None):
        this.__images = dict()
        this.__audios = dict()

        for key, asset in discoveredAssets.iteritems():
            kind, path = asset
            if not logger is None:
                logger.info(str.format("Asset: \"{0}\" ({1}) at \"{2}\"", key, kind, path))
            if kind == "image":
                this.__images[key] = loader.loadImage(path)
            elif kind == "audio":
                this.__audios[key] = loader.loadAudio(path)

    def getImage(this, imageKey):
        return this.__images[imageKey]

    def getAudio(this, audioKey):
        return this.__audios[audioKey]
