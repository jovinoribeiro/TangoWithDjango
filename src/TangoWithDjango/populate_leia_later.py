
from leialater.models import Category, Bookmark

def populate():
    python_cat = add_cat('Python')
    
    add_bookmark(cat=python_cat,
        title="Oficial Python Tutorial",
        url = "http://docs.python.org/2/tutorial/",
        summary="Learn Python")
    
    java_cat = add_cat('Java')
    
    add_bookmark(cat=java_cat,
        title="Oficial Java Tutorial",
        url = "http://docs.python.org/2/tutorial/",
        summary="Learn Java")
    
def add_bookmark(cat, title, url, summary):
    b = Bookmark.objects.get_or_create(category=cat, title=title, url=url, summary=summary)
    return b

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

# Start execution
if __name__ == '__main__':
    import django
    django.setup()
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TangoWithDjango.settings")
    print "Starting Leialater population script..."
    populate()
    