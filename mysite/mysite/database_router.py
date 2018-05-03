# from django.conf import settings
# DATABASE_MAPPING = settings.DATABASE_APPS_MAPPING
# class qidian_app_DatabaseRouter(object):
#     def db_for_read(self, model, **hints):
#         """"Point all read operations to the specific database."""
#         if model._meta.app_label == 'qidian':
#             return 'qidian_db'
#         return None
#     def db_for_write(self, model, **hints):
#         """Point all write operations to the specific database."""
#         if model._meta.app_label == 'qidian':
#             return 'qidian_db'
#         return None
#     def allow_relation(self, obj1, obj2, **hints):
#         """Allow any relation between apps that use the same database."""
#         if obj1._meta.app_label == 'qidian' or \
#                 obj2._meta.app_label == 'qidian':
#             return True
#         return None
#     def allow_syncdb(self, db, model):
#         """Make sure that apps only appear in the related database."""
#         if db == 'qidian_db' or model._meta.app_label == "qidian":
#             return False
#         else:
#             return True
#         return None
#     def allow_migrate(self, db, model):
#         """
#         Make sure the auth app only appears in the 'auth_db'
#         database.
#         """
#         if db == 'qidian_db':
#             return model._meta.app_label == 'qidian'
#         elif model._meta.app_label == 'qidian':
#             return False