# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'mini_ultimatum'
    players_per_group = 3
    num_rounds = 1

    endowment = c(10)
    offer_increment = c(5)

    offer_choices = currency_range(0, endowment, offer_increment)
    offer_choices_count = len(offer_choices)


class Subsession(BaseSubsession):
     pass

class Group(BaseGroup):

    strategy = models.BooleanField(
    doc="""Whether this group uses strategy method"""
        )

    amount_offered = models.CurrencyField(choices=Constants.offer_choices)

    offer_accepted = models.BooleanField(
        doc="if offered amount is accepted (direct response method)"
    )

    def set_payoffs(self):
        p1, p2, p3 = self.get_players()

        if self.strategy:
            self.offer_accepted = getattr(self, 'response_{}'.format(int(self.amount_offered)))

        if self.offer_accepted:
            p1.payoff = Constants.endowment - self.amount_offered
            p2.payoff = self.amount_offered


class Player(BasePlayer):
    pass
