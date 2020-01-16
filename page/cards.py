from poium import Page, PageElement, PageElements


class Cardspage(Page):
    cards_list_loc = PageElements(class_name = 'item')

    def get_cards_num(self):
        return len(self.cards_list_loc)