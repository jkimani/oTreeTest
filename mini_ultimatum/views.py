# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):

    pass

class Introduction(Page):
    pass

class Offer(Page):
    form_model = models.Group
    form_fields = ['amount_offered']

    def is_displayed(self):
        return self.player.id_in_group == 1

class WaitForProposer(WaitPage):
    pass

class Accept(Page):
    form_model = models.Group
    form_fields = ['offer_accepted']

    def is_displayed(self):
        return self.player.id_in_group == 2 and not self.group.strategy


class AcceptStrategy(Page):
    form_model = models.Group
    form_fields = ['response_{}'.format(int(i)) for i in Constants.offer_choices]

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.group.strategy


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()

class Punish(Page):
    form_model = models.Group
    form_fields = ['offer_accepted']

    def is_displayed(self):
        return self.player.id_in_group == 3

class WaitForPunisher(WaitPage):
    pass

class Results(Page):
    pass


page_sequence = [Introduction,
            Offer,
            WaitForProposer,
            Accept,
            AcceptStrategy,
            ResultsWaitPage,
            Punish,
            WaitForPunisher,
            Results]

