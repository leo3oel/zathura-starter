from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent, PreferencesEvent, PreferencesUpdateEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.item.ExtensionSmallResultItem import ExtensionSmallResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

import subprocess as sub
from folder import *

path = "~"

def getList(path):
    """
    Make Liste to Display
    """
    folders = getFolders(path)
    items = []
    for folder in folders:
        pathtofolder = f"00;{path}/{folder}" # next folder path
        items.append(ExtensionSmallResultItem(icon='images/folder.png',
                                            name='Folder: %s' % folder,
                                            on_enter=ExtensionCustomAction(pathtofolder, keep_app_open=True)))
    pdfs = getFiles(path)
    for pdf in pdfs:
        pathtofile = f"01;{path}/{pdf}"
        items.append(ExtensionSmallResultItem(icon='images/pdf.png',
                                            name='PDF: %s' % pdf,
                                            on_enter=ExtensionCustomAction(pathtofile, keep_app_open=False)))
    return(items)

class ZathuraExtension(Extension):

    def __init__(self):
        super().__init__() # Parent Constructor
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener()) # if Keywords get entered -> KeywordQueryEventListener
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())  # <-- add this line
        self.subscribe(PreferencesEvent, PreferencesEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        # return List
        return RenderResultListAction(getList(path))

class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        # event is instance of ItemEnterEvent
        data = event.get_data()
        if data[0:2] == "00":
            temppath = data[3:] # set new path

            #return new list
            return RenderResultListAction(getList(temppath))
        else:
            pdf = data[3:] # extract filename

            # Open File in Zathura
            sub.run(["zathura", pdf])

            return RenderResultListAction([])

class PreferencesEventListener(EventListener):
    """
    Listener for prefrences event.
    It is triggered on the extension start with the configured preferences
    """

    def on_event(self, event, extension):
        global path
        path = "~"
        if event.preferences["start_path"] != "":
            path = event.preferences["start_path"]



if __name__ == '__main__':
    ZathuraExtension().run()