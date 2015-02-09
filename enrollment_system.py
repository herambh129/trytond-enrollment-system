# -*- coding: utf-8 -*-
"""
    enrollment_system.py

    :copyright: (c) 2015 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.model import ModelView, ModelSQL, fields
from trytond.pyson import Eval
from trytond.pool import PoolMeta


__all__ = ['EducationalBackground', 'PriorExperience', 'SkillSet', 'Party']
__metaclass__ = PoolMeta


STATES = {
    'readonly': ~Eval('active'),
}
DEPENDS = ['active']


class Party:
    '''
    Party class
    '''
    __name__ = 'party.party'
    educational_qualifications = fields.One2Many(
        'party.educational_background',
        'party', 'EducationalBackground', states=STATES, depends=DEPENDS
    )
    prior_experience = fields.One2Many(
        'party.prior_experience', 'party', 'PriorExperience',
        states=STATES, depends=DEPENDS
    )
    skill_set = fields.One2Many(
        'party.skill_set', 'party', 'SkillSet',
        states=STATES, depends=DEPENDS
    )


class EducationalBackground(ModelSQL, ModelView):
    '''
     Educational Background class
    '''
    __name__ = 'party.educational_background'
    party = fields.Many2One(
        'party.party', 'Party', required=True,
        ondelete='CASCADE', select=True
    )
    graduations = fields.Char('Graduation', required=True)
    specialization = fields.Char('Specialization', required=True)
    grade = fields.Char('Grade', required=True)
    university = fields.Char('University_Name', required=True)
    year_of_completion = fields.Char('Year_of_completion', required=True)
    references = fields.Char('References')
    post_held = fields.Char('Post_of_refrence')
    institution = fields.Char('Institution')
    reference_city = fields.Char('City_refrence')


class PriorExperience(ModelSQL, ModelView):
    '''
     Prior Experience class
    '''
    __name__ = 'party.prior_experience'
    party = fields.Many2One(
        'party.party', 'Party', required=True,
        ondelete='CASCADE', select=True
    )
    post_held = fields.Char('Post')
    department = fields.Char('Department')
    experience_company = fields.Char('Name_company')
    experience_city = fields.Char('City_experience')
    tenure = fields.Char('Tenure')
    references = fields.Char('References_in_company')
    designation = fields.Char('Designation')
    experience_area = fields.Char('Area_experience')
    organization = fields.Char('Organization')
    email = fields.Char('Email')


class SkillSet(ModelSQL, ModelView):
    '''
     Skill set class
    '''
    __name__ = 'party.skill_set'
    party = fields.Many2One(
        'party.party', 'Party', required=True,
        ondelete='CASCADE', select=True
    )
    skill_area = fields.Char('Area_skill')
    skill = fields.Char('Skill')
    certificate_grade = fields.Char('Certificate')
    project_summary = fields.Text('Project')
