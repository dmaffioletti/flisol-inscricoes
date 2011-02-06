# -*- coding: utf-8 -*-
#########################################################################
## Customizando o titulo da aplicação, subtitulo e menus
#########################################################################

response.title = 'FLISOL Inscrições'
# response.subtitle = T('customize me!')

response.meta.author = 'Bruno Barbosa e Gilson Filho'
response.meta.description = ''
response.meta.keywords = 'web2py, flisol, software livre, acsldf'
response.meta.generator = 'Web2py Enterprise Framework'
response.meta.copyright = 'Copyright 2011'

##########################################
## Criando seus menus
##########################################

response.menu = [
    (T('Home'), False, URL(request.application,'default','index'), []),
    (T('Atividades'), False, URL(request.application,'default','index'), []),
    (T('Certificados'), False, URL(request.application,'default','index'), [])
    ]


