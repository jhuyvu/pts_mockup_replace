import os
import photoshop.api as ps

app = ps.Application()
current_path = os.path.dirname(__file__)
psd_path = os.path.join(current_path, 'P1.psd')
background_path = os.path.join(current_path, '101111.jpg')
app.open(psd_path)
docRef = app.activeDocument
groups = docRef.layers

replace_contents = app.stringIDToTypeID("placedLayerReplaceContents")
desc = ps.ActionDescriptor()
idnull = app.charIDToTypeID("null")
desc.putPath(key=idnull, value=background_path)

for group in groups:
    if group.name == 'design in':
        for layerInGroup in group.artLayers:
            if layerInGroup.name == 'design':
                docRef.activeLayer = layerInGroup
                app.executeAction(replace_contents, descriptor=desc)
                options = ps.JPEGSaveOptions(quality=12)    # max 12
                docRef.saveAs(os.path.join(current_path, 'cat.jpg'), options, True)
