from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import DishCategory, Dish, Gallery, Chefs, Introduction, Description, Review

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        categories = DishCategory.objects.filter(is_visible=True)
        gallery = Gallery.objects.all()
        introduction = Introduction.objects.all()
        description = Description.objects.all()
        review = Review.objects.all()
        #form = ReservationForm()

        context['categories'] = categories
        context['gallery'] = gallery
        context['introduction'] = introduction
        context['description'] = description
        context['review'] = review
        #context['form'] = form
        context['title_menu'] = 'Check Our <span>Yummy Menu</span>'
        context['title_gallery'] = 'Check <span>Our Gallery</span>'
        context['title_events'] = 'Share <span>Your Moments</span> In Our Restaurant'
        context['title_chefs'] = 'Our <span>Proffesional</span> Chefs'
        context['title_contacts'] = 'Need Help? <span>Contact Us</span>'
        context['title_contacts_address'] = 'Our Address'
        context['title_contact_email'] = 'Email Us'
        context['title_contact_phone'] = 'Call Us'
        context['title_contact_time'] = 'Opening Hours'

        return context

    def post(self, request):
        ...
        # form = ReservationForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     messages.success(request, 'Ваше бронирование принято')
        #     return redirect('main:index')

def menu(request):

    categories = DishCategory.objects.filter(is_visible=True)

    context = {'categories': categories,
               }

    return render(request, 'menu.html', context=context)

def about(request):

    chefs = Chefs.objects.filter(is_visible=True)

    context = {'chefs': chefs,
               'our_story': '''
                            Fusce at risus eget mi auctor pulvinar. Suspendisse maximus 
                            venenatis pretium. Orci varius natoque penatibus et magnis dis parturient 
                            montes, nascetur ridiculus mus. Aliquam purus purus, lacinia a scelerisque in,
                            luctus vel felis. Donec odio diam, dignissim a efficitur at, efficitur et est.
                            Pellentesque semper est ut pulvinar ullamcorper. Class aptent taciti sociosqu 
                            ad litora torquent per conubia nostra, per inceptos himenaeos. 
                            Nulla et leo accumsan, egestas velit ac, fringilla tortor. 
                            Sed varius justo sed luctus mattis.
                            ''',
               }

    return render(request, 'about.html', context=context)


