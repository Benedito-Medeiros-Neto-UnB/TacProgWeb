

from owlready2 import *
onto_path.append(".")
onto = get_ontology("http://127.0.0.1/onto_model_article.owl")
onto10 = get_ontology("http://127.0.0.1/onto_model_source.owl")
# Havaria de se criar listas de assinatura de transmissoes RSS, 
# a fim de que as expor em um canal 

print(list(onto.classes()))   

# MODELAGEM DE ONTOLOGIA

# CRIACAO DE CLASSES
        
with onto:
    class Article(Thing):
        pass
    with onto10:
        class Source(Article):
            pass
        class RSS(Source):
            pass
        class DSpace(Source):
            pass
        class Twitter(Source):
            pass
    class Url(Article, RSS):
        pass
    class Author(Article):
        pass
    class Theme(Article):
        pass
    class Date(Article):
        pass
    class Image(Article):
        pass
    class has_date(ObjectProperty):
        domain = [Article]
        range = [Date]
    class has_source(ObjectProperty):
        domain = [Article]
        range = [Source]
    class has_instance(ObjectProperty):
        domain = [Article]
        range = [Article]
    class has_url(ObjectProperty):
        domain = [Article]
        range = [Url]
    class has_url(ObjectProperty):
        domain = [RSS]
        range = [Url]
    class has_author(ObjectProperty):
        domain = [Article]
        range = [Author]
    class has_theme(ObjectProperty):
        domain = [Article]
        range = [Theme]
    class has_image(ObjectProperty):
        domain = [Article]
        range = [Theme]

    # Possibilidade de se ter enquanto propriedade imagens, videos


# INSTANCIACAO
article = Article("Como encontrar a felicidade em tempos sombrios: três passos para olhar o futuro")
article_url = Url("https://theintercept.com/2019/10/25/felicidade-tempos-sombrios/")
article.has_url = [article_url]
#article_theme = Theme("Depressao")
#article.has_theme = [article_theme]

article_date = Date("Sat, 26 Oct 2019 03:03:57 +0000")
article.has_date = [article_date]

article_author = Author("Christian Ingo Lenz Dunker")
article.has_author = [article_author]
#article_main.has_instance.append(article)


rss = RSS("https://theintercept.com/feed/?lang=pt")
#rss_url = Url("https://theintercept.com/feed/?lang=pt")
rss.has_url = [rss]

rss.has_url = [article_url]

rss = RSS("https://diplomatique.org.br/feed/")
#rss_url = Url("https://diplomatique.org.br/feed/")
rss.has_url = [rss]

rss = RSS("https://outraspalavras.net/feed/")
#rss_url = Url("https://outraspalavras.net/feed/")
rss.has_url = [rss]

#article_main.has_instance.append(article2)
#print(URL.ancestors())

#print(article.name)
#print(article.has_url)
#print(article_url.name)
#print(onto.search(has_url = "*"))
# print(onto.search_one(label = "felicidade"))

for i in Article.instances(): 
    if (i.has_url):
        print(i.name)
        print(i.has_url)
    #print(i.URL)

# DELETA ENTIDADES/CLASSES
#destroy_entity(articles1)

onto.save()
onto.save(file = "onto_model_article.owl", format = "rdfxml")
onto10.save()
onto10.save(file = "onto_model_source.owl", format = "rdfxml")










