# -*- coding: utf-8 -*-
from openerp import http

# para ejercicio 1
#class Academy(http.Controller):
#    @http.route('/academy/academy/', auth='public')
#    def index(self, **kw):
#        return "Hello, world"

class Academy(http.Controller):
    @http.route('/academy/academy/', auth='public')
    def index(self, **kw):
        Teachers = http.request.env['academy.teachers']
        return http.request.render('academy.index', {
            'teachers': Teachers.search([])
        })


# class Academy(http.Controller):
#     @http.route('/academy/academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/academy/academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('academy.listing', {
#             'root': '/academy/academy',
#             'objects': http.request.env['academy.academy'].search([]),
#         })

#     @http.route('/academy/academy/objects/<model("academy.academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy.object', {
#             'object': obj
#         })