import webbrowser
from kivy.uix.modalview import ModalView
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.list import TwoLineIconListItem, IconLeftWidget
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
import feedparser
import joblib

Window.size = (720, 1280)
sgd_ppl_clf = joblib.load('learned_model.pkl')
parseList = ["https://news.mail.ru/rss/economics/91/", "https://news.mail.ru/rss/politics/91/"]
parsedList = []
parsedLinkList = []

ecoList = []
ecoLinkList = []
culList = []
culLinkList = []
sportList = []
sportLinkList = []
sciList = []
sciLinkList = []

KV = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"
<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    selected_color: "#4a4939"
    focus_behavior: False
    _no_ripple_effect: True
<Content>  
    adaptive_height: True
    TwoLineIconListItem:
        text: "Перейти по ссылке"
        IconLeftWidget:
            icon: 'star-plus-outline'
<Favorite>
    on_release: root.set_icon(self)
    MDScrollView:
        MDGridLayout:
            id: boxFavorites
            cols: 1
            adaptive_height: True

MDScreen:  
    MDBottomNavigation:
        #panel_color: "#eeeaea"
        selected_color_background: "orange"
        text_color_active: "lightgrey"
        MDBottomNavigationItem:
            name: 'economy'
            text: 'Экономика'
            icon: 'cash-multiple'
            MDScrollView:
                MDGridLayout:
                    id: boxEconomy
                    cols: 1
                    adaptive_height: True
                    MDTopAppBar:
                        title: "News aggregator"
                        elevation: 0
                        pos_hint: {"top": 1}
                        md_bg_color: "#e7e4c0"
                        specific_text_color: "#4a4939"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
        MDBottomNavigationItem:
            name: 'culture'
            text: 'Культура'
            icon: 'palette'
            MDScrollView:
                MDGridLayout:
                    id: boxCulture
                    cols: 1
                    adaptive_height: True
                    MDTopAppBar:
                        title: "News aggregator"
                        elevation: 0
                        pos_hint: {"top": 1}
                        md_bg_color: "#e7e4c0"
                        specific_text_color: "#4a4939"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]] 
        MDBottomNavigationItem:
            name: 'scince'
            text: 'Наука и техника'
            icon: 'laptop'
            MDScrollView:
                MDGridLayout:
                    id: boxScince
                    cols: 1
                    adaptive_height: True
                    MDTopAppBar:
                        title: "News aggregator"
                        elevation: 0
                        pos_hint: {"top": 1}
                        md_bg_color: "#e7e4c0"
                        specific_text_color: "#4a4939"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
        MDBottomNavigationItem:
            name: 'sport'
            text: 'Спорт'
            icon: 'handball'
            MDScrollView:
                MDGridLayout:
                    id: boxSport
                    cols: 1
                    adaptive_height: True
                    MDTopAppBar:
                        title: "News aggregator"
                        elevation: 0
                        pos_hint: {"top": 1}
                        md_bg_color: "#e7e4c0"
                        specific_text_color: "#4a4939"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
    MDNavigationDrawer:
        id: nav_drawer
        radius: (0, 30, 30, 0)
        MDNavigationDrawerMenu:
            MDNavigationDrawerHeader:
                title: "Опции"
                spacing: "4dp"
                padding: "12dp", 0, 0, "56dp"
            MDNavigationDrawerLabel:
                text: "Настройки:"
            DrawerLabelItem:
                icon: "shield-moon-outline"
                text: "Ночная тема:"
                MDSwitch:
                    widget_style: "android"  
                    icon_inactive: "close"
                    icon_inactive_color: 'gray'
                    icon_active: "check"
                    icon_active_color: "white"
                    track_color_active: 'yellow'
                    thumb_color_active: 'orange'
                    pos_hint: {"center_x": .65, "center_y": .35} 
                    on_active:
                        app.switch_theme_style(*args)
            MDNavigationDrawerDivider:
            MDNavigationDrawerLabel:
                text: "Страницы:"
            DrawerClickableItem:
                id: norm
                icon: 'star-check-outline'
                text: 'Избранное'
                on_release:
                    app.change_text()
            DrawerClickableItem:
                icon: 'comment-question-outline'
                text: 'FAQ'
            DrawerClickableItem:
                icon: 'file-document-alert-outline'
                text: 'Guide'
'''
per = []

def parse_news(parseList):
    per = 0
    for feed in parseList:
        feed = feedparser.parse(feed)
        for entry in feed.entries:
            if 'link' in entry:
                parsedLinkList.append(entry.link)
            if 'summary' in entry:
                parsedList.append(entry.summary)
    for i in parsedList:
        # Классификация нового текста
        new_text = parsedList[per]
        new_link = parsedLinkList[per]
        predicted_label = sgd_ppl_clf.predict([new_text])[0]
        if predicted_label == 'Экономика':
            ecoList.append(new_text)
            ecoLinkList.append(new_link)
        if predicted_label == 'Культура':
            culList.append(new_text)
            culLinkList.append(new_link)
        if predicted_label == 'Спорт':
            sportList.append(new_text)
            sportLinkList.append(new_link)
        if predicted_label == 'Наука и техника':
            sciList.append(new_text)
            sciLinkList.append(new_link)
        per += 1

class Content(MDBoxLayout):
    '''Custom content.'''

class Favorite(MDBoxLayout):
    ''''''

perem = []
perem2 = []

def write():
    with open('favourites.txt', 'a') as file:
        file.write(perem[0]+'\n')
        file.write(perem2[0]+'\n')
clearingPerem = []
clearingPeremLink = []
def clearData():
    with open('favourites.txt', 'r') as file:
        lines = file.readlines()
    try:
        index1 = lines.index(clearingPerem[0])
        index2 = lines.index(clearingPeremLink[0])
    except ValueError:
        print('ошибка')
        print(clearingPeremLink[0])
    del lines[index1]
    del lines[index2]
    with open('favourites.txt', 'w') as file:
        file.writelines(lines)

class Test(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def on_start(self):
        parse_news(parseList)
        for i in range(len(ecoList)):
            self.root.ids.boxEconomy.add_widget(
                MDExpansionPanel(
                    icon='newspaper-variant-outline',
                    content=TwoLineIconListItem(IconLeftWidget(icon='star-plus-outline', on_press=lambda x: (perem.append(x.parent.parent.secondary_text), perem2.append(x.parent.parent.parent.panel_cls.text), write(), perem.clear(), perem2.clear())), text='Перейти по ссылке:', secondary_text=ecoLinkList[i], on_release=lambda x: webbrowser.open(x.secondary_text)),
                    panel_cls=MDExpansionPanelOneLine(
                        id='chel',
                        text=ecoList[i], text_color='orange'

                    )
                )
            )
        for i in range(len(culList)):
            self.root.ids.boxCulture.add_widget(
                MDExpansionPanel(
                    icon='newspaper-variant-outline',
                    content=TwoLineIconListItem(IconLeftWidget(icon='star-plus-outline', on_press=lambda x: perem.append(x.parent.parent.secondary_text)), text='Перейти по ссылке:', secondary_text=culLinkList[i], on_release=lambda x: webbrowser.open(x.secondary_text)),
                    panel_cls=MDExpansionPanelOneLine(
                        text=culList[i]
                    )
                )
            )
        for i in range(len(sciList)):
            self.root.ids.boxScince.add_widget(
                MDExpansionPanel(
                    icon='newspaper-variant-outline',
                    content=TwoLineIconListItem(IconLeftWidget(icon='star-plus-outline', on_press=lambda x: perem.append(x.parent.parent.secondary_text)), text='Перейти по ссылке:', secondary_text=sciLinkList[i], on_release=lambda x: webbrowser.open(x.secondary_text)),
                    panel_cls=MDExpansionPanelOneLine(
                        text=sciList[i]
                    )
                )
            )

        for i in range(len(sportList)):
            self.root.ids.boxSport.add_widget(
                MDExpansionPanel(
                    icon='newspaper-variant-outline',
                    content=TwoLineIconListItem(IconLeftWidget(icon='star-plus-outline',  on_press=lambda x: perem.append(x.parent.parent.secondary_text)), text='Перейти по ссылке:', secondary_text=sportLinkList[i], on_release=lambda x: webbrowser.open(x.secondary_text)),
                    panel_cls=MDExpansionPanelOneLine(
                        text=sportList[i]

                    )
                )
            )


    def switch_theme_style(self, switch, x):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.8
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )

    def change_text(self):
        view = ModalView(background='', size_hint=(.9,.9))
        screen = MDScreen()
        scroll_view = MDScrollView()
        grid = MDGridLayout(cols=1, adaptive_height=True)
        per =[]
        perLink = []
        with open('favourites.txt', 'r') as file:
            for i in file:
                per.append(i)
        for i in range(int(len(per))):
            if i%2==0:
                grid.add_widget(
                    MDExpansionPanel(
                        icon='newspaper-variant-outline',
                        content=TwoLineIconListItem(IconLeftWidget(icon='star-minus-outline',  on_press=lambda x: (clearingPeremLink.append(x.parent.parent.secondary_text), clearingPerem.append(x.parent.parent.parent.panel_cls.text), clearData(), clearingPerem.clear(), clearingPeremLink.clear())), text='Перейти по ссылке:', secondary_text=per[i], on_release=lambda x: webbrowser.open(x.secondary_text)),
                        panel_cls=MDExpansionPanelOneLine(
                            text=per[i+1]
                        )
                    )
                )
        scroll_view.add_widget(grid)
        screen.add_widget(scroll_view)
        view.add_widget(screen)
        view.open()

Test().run()

