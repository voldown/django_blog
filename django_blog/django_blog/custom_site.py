from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Django Blog'
    site_title = 'Django Blog Admin'
    index_title = 'Home Page'


custom_site = CustomSite(name='cus_admin')
