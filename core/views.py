from django.views.generic import TemplateView

class  IndexView (TemplateView):
    template_name='index.html'

class  CollectionView (TemplateView):
    template_name='collection.html'

class  RacingView (TemplateView):
    template_name='racing_boots.html'

class  ShoesView (TemplateView):
    template_name='shoes.html'

class  ContatoView (TemplateView):
    template_name='contact.html'