# -*- coding: utf-8 -*-

# Copyright 2016-2017 The Wazo Authors  (see the AUTHORS file)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from test_api import scenarios as s


def invalid_destinations():
    return [
        1234,
        'string',
        {'type': 'invalid'},

        {'type': 'application'},
        {'type': 'application', 'missing_required_field': 'disa'},
        {'type': 'application', 'application': 'invalid'},

        {'type': 'application', 'application': 'callback_disa', 'context': True},
        {'type': 'application', 'application': 'callback_disa', 'context': None},
        {'type': 'application', 'application': 'callback_disa', 'context': 'invalid_char_@'},
        {'type': 'application', 'application': 'callback_disa', 'context': s.random_string(40)},
        {'type': 'application', 'application': 'callback_disa', 'context': 'default', 'pin': 'invalid'},
        {'type': 'application', 'application': 'callback_disa', 'context': 'default', 'pin': True},
        {'type': 'application', 'application': 'callback_disa', 'context': 'default', 'pin': 1234},
        {'type': 'application', 'application': 'callback_disa', 'context': 'default', 'pin': '#123'},
        {'type': 'application', 'application': 'callback_disa', 'context': 'default', 'pin': s.random_string(41)},

        {'type': 'application', 'application': 'directory', 'context': True},
        {'type': 'application', 'application': 'directory', 'context': None},
        {'type': 'application', 'application': 'directory', 'context': 'invalid_char_@'},
        {'type': 'application', 'application': 'directory', 'context': s.random_string(40)},

        {'type': 'application', 'application': 'disa', 'context': True},
        {'type': 'application', 'application': 'disa', 'context': None},
        {'type': 'application', 'application': 'disa', 'context': 'invalid_char_@'},
        {'type': 'application', 'application': 'disa', 'context': s.random_string(40)},
        {'type': 'application', 'application': 'disa', 'context': 'default', 'pin': 'invalid'},
        {'type': 'application', 'application': 'disa', 'context': 'default', 'pin': True},
        {'type': 'application', 'application': 'disa', 'context': 'default', 'pin': 1234},
        {'type': 'application', 'application': 'disa', 'context': 'default', 'pin': '#123'},
        {'type': 'application', 'application': 'disa', 'context': 'default', 'pin': s.random_string(41)},

        {'type': 'application', 'application': 'fax_to_mail', 'email': 'invalid'},
        {'type': 'application', 'application': 'fax_to_mail', 'email': 1234},
        {'type': 'application', 'application': 'fax_to_mail', 'email': True},
        {'type': 'application', 'application': 'fax_to_mail', 'email': None},
        {'type': 'application', 'application': 'fax_to_mail', 'email': s.random_string(81)},

        {'type': 'application', 'application': 'voicemail', 'context': True},
        {'type': 'application', 'application': 'voicemail', 'context': None},
        {'type': 'application', 'application': 'voicemail', 'context': 'invalid_char_@'},
        {'type': 'application', 'application': 'voicemail', 'context': s.random_string(40)},

        {'type': 'meetme'},
        {'type': 'meetme', 'missing_required_field': 123},
        {'type': 'meetme', 'conference_id': 'string'},
        {'type': 'meetme', 'conference_id': None},

        {'type': 'conference'},
        {'type': 'conference', 'missing_required_field': 123},
        {'type': 'conference', 'conference_id': 'string'},
        {'type': 'conference', 'conference_id': None},

        {'type': 'custom'},
        {'type': 'custom', 'missing_required_field': '123'},
        {'type': 'custom', 'command': 1234},
        {'type': 'custom', 'command': True},
        {'type': 'custom', 'command': None},
        {'type': 'custom', 'command': 'invalid'},
        {'type': 'custom', 'command': 'system(not_authorized)'},
        {'type': 'custom', 'command': 'trysystem(not_authorized)'},
        {'type': 'custom', 'command': s.random_string(256)},

        {'type': 'extension'},
        {'type': 'extension', 'missing_required_field': '123'},
        {'type': 'extension', 'context': True},
        {'type': 'extension', 'context': None},
        {'type': 'extension', 'context': 'invalid_char_@'},
        {'type': 'extension', 'context': s.random_string(40)},
        {'type': 'extension', 'context': 'default', 'exten': 1234},
        {'type': 'extension', 'context': 'default', 'exten': True},
        {'type': 'extension', 'context': 'default', 'exten': None},
        {'type': 'extension', 'context': 'default', 'exten': '*1234#??'},

        {'type': 'group'},
        {'type': 'group', 'missing_required_field': 123},
        {'type': 'group', 'group_id': 'string'},
        {'type': 'group', 'group_id': None},
        {'type': 'group', 'group_id': 1, 'ring_time': -10},

        {'type': 'hangup', 'cause': 'invalid'},

        {'type': 'hangup', 'cause': 'busy', 'timeout': 'invalid'},
        {'type': 'hangup', 'cause': 'busy', 'timeout': -9},

        {'type': 'hangup', 'cause': 'congestion', 'timeout': 'invalid'},
        {'type': 'hangup', 'cause': 'congestion', 'timeout': -10},

        {'type': 'ivr'},
        {'type': 'ivr', 'missing_required_field': 123},
        {'type': 'ivr', 'ivr_id': 'string'},
        {'type': 'ivr', 'ivr_id': None},

        {'type': 'outcall'},
        {'type': 'outcall', 'missing_required_field': 123},
        {'type': 'outcall', 'outcall_id': 'string'},
        {'type': 'outcall', 'outcall_id': None},

        {'type': 'queue'},
        {'type': 'queue', 'missing_required_field': 123},
        {'type': 'queue', 'queue_id': 'string'},
        {'type': 'queue', 'queue_id': None},
        {'type': 'queue', 'queue_id': 1, 'ring_time': -10},

        {'type': 'sound'},
        {'type': 'sound', 'missing_required_field': 'string'},
        {'type': 'sound', 'filename': 1234},
        {'type': 'sound', 'filename': None},
        {'type': 'sound', 'filename': s.random_string(256)},
        {'type': 'sound', 'filename': 'daddy-cool', 'skip': None},
        {'type': 'sound', 'filename': 'daddy-cool', 'skip': 123},
        {'type': 'sound', 'filename': 'daddy-cool', 'skip': 'invalid'},
        {'type': 'sound', 'filename': 'daddy-cool', 'skip': []},
        {'type': 'sound', 'filename': 'daddy-cool', 'skip': {}},
        {'type': 'sound', 'filename': 'daddy-cool', 'no_answer': None},
        {'type': 'sound', 'filename': 'daddy-cool', 'no_answer': 123},
        {'type': 'sound', 'filename': 'daddy-cool', 'no_answer': 'invalid'},
        {'type': 'sound', 'filename': 'daddy-cool', 'no_answer': []},
        {'type': 'sound', 'filename': 'daddy-cool', 'no_answer': {}},

        {'type': 'switchboard'},
        {'type': 'switchboard', 'missing_required_field': 123},
        {'type': 'switchboard', 'switchboard_id': 'string'},
        {'type': 'switchboard', 'switchboard_id': None},
        {'type': 'switchboard', 'switchboard_id': 1, 'ring_time': -10},

        {'type': 'user'},
        {'type': 'user', 'missing_required_field': 123},
        {'type': 'user', 'user_id': 'string'},
        {'type': 'user', 'user_id': None},
        {'type': 'user', 'user_id': 1, 'ring_time': -10},

        {'type': 'voicemail'},
        {'type': 'voicemail', 'missing_required_field': 123},
        {'type': 'voicemail', 'voicemail_id': 'string'},
        {'type': 'voicemail', 'voicemail_id': None},
        {'type': 'voicemail', 'voicemail_id': 1, 'skip_instructions': None},
        {'type': 'voicemail', 'voicemail_id': 1, 'skip_instructions': 'string'},
        {'type': 'voicemail', 'voicemail_id': 1, 'greeting': True},
        {'type': 'voicemail', 'voicemail_id': 1, 'greeting': 'invalid'},
    ]


def valid_destinations(meetme, ivr, group, outcall, queue, switchboard, user, voicemail, conference):
    return [
        {'type': 'application', 'application': 'callback_disa',
         'context': 'name'},
        {'type': 'application', 'application': 'callback_disa',
         'pin': '1234', 'context': 'name'},
        {'type': 'application', 'application': 'callback_disa',
         'pin': None, 'context': 'name'},
        {'type': 'application', 'application': 'directory',
         'context': 'name'},
        {'type': 'application', 'application': 'disa',
         'context': 'name'},
        {'type': 'application', 'application': 'disa',
         'pin': '1234', 'context': 'name'},
        {'type': 'application', 'application': 'disa',
         'pin': None, 'context': 'name'},
        {'type': 'application', 'application': 'fax_to_mail',
         'email': 'toto@example.com'},
        {'type': 'application', 'application': 'voicemail',
         'context': 'name'},
        {'type': 'meetme', 'conference_id': meetme['id']},
        {'type': 'conference', 'conference_id': conference['id']},
        {'type': 'custom', 'command': 'Playback(toto)'},
        {'type': 'extension', 'exten': '1001', 'context': 'name'},
        {'type': 'group', 'group_id': group['id']},
        {'type': 'group', 'group_id': group['id'], 'ring_time': 1.5},
        {'type': 'group', 'group_id': group['id'], 'ring_time': None},
        {'type': 'hangup', 'cause': 'normal'},
        {'type': 'hangup', 'cause': 'busy'},
        {'type': 'hangup', 'cause': 'busy', 'timeout': 1.6},
        {'type': 'hangup', 'cause': 'busy', 'timeout': None},
        {'type': 'hangup', 'cause': 'congestion'},
        {'type': 'hangup', 'cause': 'congestion', 'timeout': 0.6},
        {'type': 'hangup', 'cause': 'congestion', 'timeout': None},
        {'type': 'ivr', 'ivr_id': ivr['id']},
        {'type': 'none'},
        {'type': 'outcall', 'outcall_id': outcall['id'], 'exten': '1234567890'},
        {'type': 'queue', 'queue_id': queue['id']},
        {'type': 'queue', 'queue_id': queue['id'], 'ring_time': 0.9},
        {'type': 'queue', 'queue_id': queue['id'], 'ring_time': None},
        {'type': 'sound', 'filename': 'filename_without_extension'},
        {'type': 'sound', 'filename': 'filename_without_extension',
         'skip': True},
        {'type': 'sound', 'filename': 'filename_without_extension',
         'no_answer': True},
        {'type': 'sound', 'filename': 'filename_without_extension',
         'skip': True, 'no_answer': True},
        {'type': 'sound', 'filename': 'filename_without_extension',
         'skip': False, 'no_answer': False},
        {'type': 'switchboard', 'switchboard_uuid': switchboard['uuid']},
        {'type': 'switchboard', 'switchboard_uuid': switchboard['uuid'], 'ring_time': 1.5},
        {'type': 'switchboard', 'switchboard_uuid': switchboard['uuid'], 'ring_time': None},
        {'type': 'user', 'user_id': user['id']},
        {'type': 'user', 'user_id': user['id'], 'ring_time': 2},
        {'type': 'user', 'user_id': user['id'], 'ring_time': None},
        {'type': 'voicemail', 'voicemail_id': voicemail['id']},
        {'type': 'voicemail', 'voicemail_id': voicemail['id'],
         'skip_instructions': True},
        {'type': 'voicemail', 'voicemail_id': voicemail['id'],
         'greeting': None},
        {'type': 'voicemail', 'voicemail_id': voicemail['id'],
         'skip_instructions': True, 'greeting': None},
        {'type': 'voicemail', 'voicemail_id': voicemail['id'],
         'skip_instructions': True, 'greeting': 'busy'},
        {'type': 'voicemail', 'voicemail_id': voicemail['id'],
         'skip_instructions': False, 'greeting': 'unavailable'},
    ]
