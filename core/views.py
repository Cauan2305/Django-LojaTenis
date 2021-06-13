from django.views.generic import TemplateView
from .models import ProdutosIndexPrimeiraColuna,NovaColecaoIndex,BotasIndex
class  IndexView (TemplateView):
    template_name='index.html'


    def get_context_data(self, *args,**kwargs) :
        context=super(IndexView,self).get_context_data(**kwargs)
        context={
            'Produto':ProdutosIndexPrimeiraColuna.objects.all(),
            'Colecao':NovaColecaoIndex.objects.all() ,
        }
        return context

# class IndexView2(IndexView):
#     template_name='index.html'
#     def get_context_data(self, **kwargs):
#         context=super(IndexView2,self).get_context_data(**kwargs)
#         context['Colecao']=NovaColecaoIndex.objects.all()
#         return context

        
        
class  CollectionView (TemplateView):
    template_name='collection.html'

class  RacingView (TemplateView):
    template_name='racing_boots.html'

class  ShoesView (TemplateView):
    template_name='shoes.html'

class  ContatoView (TemplateView):
    template_name='contact.html'