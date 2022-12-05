from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.item.ExtensionSmallResultItem import ExtensionSmallResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

import subprocess as sub
from folder import *


class ZathuraExtension(Extension):

    def __init__(self):
        super().__init__() # Parent Constructor
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener()) # if Keywords get entered -> KeywordQueryEventListener
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())  # <-- add this line


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        path = "/home/leodesktopF/Downloads/"
        folders = getFolders(path)
        items = []
        for folder in folders:
            items.append(ExtensionSmallResultItem(icon='images/folder.png',
                                             name='Folder %s' % folder,
                                             on_enter=HideWindowAction()))
        pdfs = getFiles(path)
        for pdf in pdfs:
            pathtofile = f"{path}{pdf}"
            items.append(ExtensionSmallResultItem(icon='images/pdf.png',
                                             name='PDF %s' % pdf,
                                             on_enter=ExtensionCustomAction(pathtofile, keep_app_open=False)))
        return RenderResultListAction(items)

class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        # event is instance of ItemEnterEvent

        pdf = event.get_data()
        # do additional actions here...
        sub.run(["zathura", pdf])

        return RenderResultListAction([])

""" class PreferencesEventListener(EventListener):
    
    def on_event(self, event, extension):
        super().on_event(event, extension)

        preferences = Preferences() """

if __name__ == '__main__':
    ZathuraExtension().run()