# -*- coding: utf-8 -*-
{
    'name': "OpenEducate Sync Log",

    'summary': """
    """,

    'description': """
    """,

    'author': "Mohamed Sharaf",

    'website': "",

    'category': 'Education',
    'depends': [
        'openeducat_core',
        'openeducat_fees'
    ],
    'version': '0.1',

    # always loaded
    'data': [
        # Security files:
        'security/ir.model.access.csv',
        # Data files:

        # View files:
        'views/sync_logs_views.xml'

    ],
    'qweb': [
        "static/src/xml/base.xml",

    ]
}
