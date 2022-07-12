{
    'name': "openacademy",
    'author': "Ahmed Abdel baky",
    'description': """
                open academy modeule to manage training:
                -manage course
                -mange attendence
                -mange skill    
    """,
    'version': '1.0',
    'demo': [
        'demo.xml',
    ],
    'depends':
    [
        'crm',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/course.xml',
        'Views/session.xml',
        'Views/partner.xml',
        'Views/wizard.xml',
    ],


}