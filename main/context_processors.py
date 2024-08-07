from django.utils.translation import gettext as _

def app_title(request) -> dict:
    """
    Add the app_title to the context for 'footer.html'
    """
    return {
        'address': _('8th floor, 379 Hudson St, New York, NY 10018'),
        'phone': '(+1) 96 716 6879',
        'email': 'contact@site.com',
        'opening_hours': _('09:30 AM – 11:00 PM'),
        'opening_days': _('Every Day'),
        'twitter_nick': '@colorlib',
        'twitter_comment_1': _('''
                             Activello is a good option. It has a slider built into 
                             that displays the featured image in the slider.
                             '''),
        'twitter_comment_2': _('Activello is a good option. It has a slider built into that displays'),
        'twitter_link_1': "https://buff.ly/2zaSfAQ",
        'twitter_date_1': _('21 Dec 2017'),
        'twitter_link_2': "https://buff.ly/2zaSfAQ",
        'twitter_date_2': _('21 Dec 2017'),
    }