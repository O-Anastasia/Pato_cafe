from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import DishCategory, Dish, Gallery, Chefs, Introduction, Description, Review
from .forms import ReservationForm
from django.contrib import messages
from django.utils.translation import gettext as _

# Create your views here.
class IndexView(TemplateView):
    """
    Class for rendering template index.html
    """
    template_name = 'index.html'
    def get_context_data(self, **kwargs) -> dict:
        """
        Method for rendering context data
        """
        context = super().get_context_data()
        categories = DishCategory.objects.filter(is_visible=True)
        gallery = Gallery.objects.all()
        introduction = Introduction.objects.all()
        description = Description.objects.all()
        review = Review.objects.all()

        context['categories'] = categories
        context['gallery'] = gallery
        context['introduction'] = introduction
        context['description'] = description
        context['review'] = review
        context['restaurant_name'] = _('Pato Place')
        context['story'] = _('''
                            Donec quis lorem nulla. Nunc eu odio mi. Morbi nec lobortis est. 
                            Sed fringilla, nunc sed imperdiet lacinia, nisl ante egestas mi, 
                            ac facilisis ligula sem id neque.
                            ''')
        context['welcome_to'] = _('Welcome to')
        context['menu'] = _('Look Menu')
        context['italian_restaurant'] = _('Italian Restaurant')
        context['welcome'] = _('Welcome')
        context['our_story'] = _('Our Story')
        context['discover'] = _('Discover')
        context['customer_say'] = _('Customers Say')
        context['review_title'] = _('Review')
        context['our_video'] = _('Our Video')
        
        return context


def menu(request) -> HttpResponse:
    """
    Method for rendering page 'menu.html'
    """
    categories = DishCategory.objects.filter(is_visible=True)

    context = {'categories': categories,
               'pato_menu': _('Pato Menu Book'),

               }

    return render(request, 'menu.html', context=context)

def about(request) -> HttpResponse:
    """
    Method for rendering page 'about.html'
    """

    chefs = Chefs.objects.filter(is_visible=True)

    context = {'chefs': chefs,
               'story': _('''
                            Fusce at risus eget mi auctor pulvinar. Suspendisse maximus 
                            venenatis pretium. Orci varius natoque penatibus et magnis dis parturient 
                            montes, nascetur ridiculus mus. Aliquam purus purus, lacinia a scelerisque in,
                            luctus vel felis. Donec odio diam, dignissim a efficitur at, efficitur et est.
                            Pellentesque semper est ut pulvinar ullamcorper. Class aptent taciti sociosqu 
                            ad litora torquent per conubia nostra, per inceptos himenaeos. 
                            Nulla et leo accumsan, egestas velit ac, fringilla tortor. 
                            Sed varius justo sed luctus mattis.
                            '''),
               'about_us': _('About Us'),
               'italian_restaurant': _('Italian Restaurant'),
               'our_story': _('Our Story'),
               'discover': _('Discover'),
               'our_video': _('Our Video'),
               'meet_our': _('Meet Our'),
               'chef': _('Chef'),
               }

    return render(request, 'about.html', context=context)


class ReservationView(TemplateView):
    """
    Class for rendering template 'reservation.html'
    """
    template_name = 'reservation.html'

    def get_context_data(self, **kwargs) -> dict:
        """
        Method for rendering context data
        """
        context = super().get_context_data()
        gallery = Gallery.objects.all()
        form = ReservationForm()

        context['gallery'] = gallery
        context['form'] = form
        context['comment_1'] = _('''
                                Donec quis euismod purus. Donec feugiat ligula rhoncus, 
                                varius nisl sed, tincidunt lectus. 
                                Nulla vulputate , lectus vel volutpat efficitur, 
                                orci lacus sodales sem, sit amet quam:
                                ''')
        context['phone'] = '(001) 345 6889'
        context['comment_2_line_1'] = _('Donec feugiat ligula rhoncus:')
        context['comment_2_line_2'] = _(', varius nisl sed, tinci-dunt lectus sodales sem.')
        context['reservations'] = _('Reservations')
        context['book_table'] = _('Book a table')
        context['person'] = _('person')
        context['persons'] = _('persons')
        context['people'] = _('people')
        context['reserve_by_phone'] = _('Reserve by Phone')
        context['for_event_booking'] = _('For Event Booking')


        return context

    def post(self, request):
        """
        Method for writing data to Reservation form from user
        """
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your reservation was successfully created.')
            return redirect('index')
        else:
            print('error')
            print(form.errors, len(form.errors))
            return redirect('reservation')

