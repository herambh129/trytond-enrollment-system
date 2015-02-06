# -*- coding: utf-8 -*-
"""
    medical_family_details.py
    :copyright: (c) 2015 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""

from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['Party']
__metaclass__ = PoolMeta


STATES = {
    'readonly': ~Eval('active')
}

DEPENDS = ['active']


class Party:
    __name__ = "party.party"

    '''
    Adding Family Deatils to Party Module
    '''
    father_name = fields.Char(
        "Father's Name", states=STATES, depends=DEPENDS
    )
    father_occupation = fields.Char(
        "Father's Occuaption", size=30, states=STATES, depends=DEPENDS
    )
    mother_name = fields.Char(
        "Mother's Name", states=STATES, depends=DEPENDS
    )
    mother_occupation = fields.Char(
        "Mother's Occuaption", size=30, states=STATES, depends=DEPENDS
    )
    parent_contact = fields.Many2One(
        "party.contact_mechanism", "Parent's Contact",
        states=STATES, depends=DEPENDS
    )
    '''
    Adding Medical Issues to Party Module
    '''
    blood_group = fields.Char(
        "Blood Group", size=3, states=STATES, depends=DEPENDS
    )
    doctor_name = fields.Char(
        "Doctor's Name", states=STATES, depends=DEPENDS
    )
    doctor_contact = fields.Many2One(
        "party.contact_mechanism", "Doctor's Contact",
        states=STATES, depends=DEPENDS
    )
    allergies = fields.Char(
        "Allergies", states=STATES, depends=DEPENDS
    )
    past_diseases = fields.Char(
        "Past Diseases", states=STATES, depends=DEPENDS
    )
    current_diseases = fields.Char(
        "Current Diseases", states=STATES, depends=DEPENDS
    )
    medications = fields.Char(
        "Mediactions", states=STATES, depends=DEPENDS
    )
