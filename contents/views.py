from .models import Author, Content, Category, Tag, Type, Publication, Geotag
from django.shortcuts import render, redirect
import json
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    pieces = Content.objects.filter(type=Type.objects.get(id=1)).order_by('-pub_date_full')[:7]
    books = Content.objects.filter(type=Type.objects.get(id=3)).order_by('-pub_date_full')[:7]
    articles = Content.objects.filter(type=Type.objects.get(id=2)).order_by('-pub_date_full')[:5]
    thesis = Content.objects.filter(type=Type.objects.get(id=4)).order_by(('-pub_date_full'))[:5]
    return render(request, 'index.html', {'pieces': pieces, 'books': books, 'articles': articles, 'thesis':thesis})


def show_content(request, id):
    content = Content.objects.get(id=id)
    author_ids = content.authors.values('id')
    author_relateds = Content.objects.filter(authors__in=author_ids).exclude(id=id).order_by('-pub_date_full')[:5]
    tag_ids = content.tags.values('id')
    tag_relateds = Content.objects.filter(tags__in=tag_ids).exclude(id=id).order_by('-pub_date_full')[:5]
    cat_ids = content.category.values('id')
    cat_relateds = Content.objects.filter(category__in=cat_ids).exclude(id=id).order_by('-pub_date_full')[:5]
    geotag_ids = content.tags.values('id')
    geotag_relateds = Content.objects.filter(geotags__in=geotag_ids).exclude(id=id).order_by('-pub_date_full')[:5]
    pub_id = content.publication_id
    pub_relateds = Content.objects.filter(publication_id=pub_id).exclude(id=id).order_by('-pub_date_full')[:5]
    return render(request, 'post.html', {
        'content': content,
        'author_relateds': author_relateds,
        'tag_relateds': tag_relateds,
        'cat_relateds': cat_relateds,
        'geotag_relateds': geotag_relateds,
        'pub_relateds': pub_relateds,
    })

def show_type(request, slug):
    type_slugs = list(Type.objects.all().values_list('slug', flat=True))
    if slug in type_slugs:
        contents = Content.objects.filter(type__slug=slug)
        return render(request, 'archive-type.html', {'contents': contents})


def show_cat(request, slug, id):
    type_slugs = list(Type.objects.all().values_list('slug', flat=True))
    if slug in type_slugs:
        content = Content.objects.get(id=id)
        author_ids = content.authors.values('id')
        author_relateds = Content.objects.filter(authors__in=author_ids).exclude(id=id).order_by('-pub_date_full')[:5]
        tag_ids = content.tags.values('id')
        tag_relateds = Content.objects.filter(tags__in=tag_ids).exclude(id=id).order_by('-pub_date_full')[:5]
        cat_ids = content.category.values('id')
        cat_relateds = Content.objects.filter(category__in=cat_ids).exclude(id=id).order_by('-pub_date_full')[:5]
        geotag_ids = content.tags.values('id')
        geotag_relateds = Content.objects.filter(geotags__in=geotag_ids).exclude(id=id).order_by('-pub_date_full')[:5]
        pub_id = content.publication_id
        pub_relateds = Content.objects.filter(publication_id=pub_id).exclude(id=id).order_by('-pub_date_full')[:5]
        return render(request, 'post.html', {
            'content': content,
            'author_relateds': author_relateds,
            'tag_relateds': tag_relateds,
            'cat_relateds': cat_relateds,
            'geotag_relateds': geotag_relateds,
            'pub_relateds': pub_relateds,
        })
    elif slug == 'tags':
        select = Tag.objects.get(id=id)
        page_title = 'برچسب: '+select.title
        contents = Content.objects.filter(tags=select)
        return render(request, 'archive.html', {'contents': contents, 'pagetitle': page_title})
    elif slug == 'publications':
        select = Publication.objects.get(id=id)
        page_title = 'مرجع: '+select.title
        contents = Content.objects.filter(publication=select)
        return render(request, 'archive.html', {'contents': contents, 'pagetitle': page_title})
    elif slug == 'geotags':
        select = Geotag.objects.get(id=id)
        page_title = 'موقعیت: '+select.title
        contents = Content.objects.filter(geotags=select)
        return render(request, 'archive.html', {'contents': contents, 'pagetitle': page_title})
    elif slug == 'authors':
        select = Author.objects.get(id=id)
        page_title = 'نویسنده/مترجم: '+select.first_name+' '+select.last_name
        contents = Content.objects.filter(authors=select)
        return render(request, 'archive.html', {'contents': contents, 'pagetitle': page_title})
    elif slug == 'categories':
        select = Category.objects.get(id=id)
        page_title = 'موضوع: '+select.title
        contents = Content.objects.filter(category=select)
        return render(request, 'archive.html', {'contents': contents, 'pagetitle': page_title})


@login_required(login_url='login')
def save_content(request, content):
    title = request.POST.get('title')
    authors_id = request.POST.getlist('authors')
    traslator_ids = request.POST.getlist('translators')
    tag_ids = request.POST.getlist('tags')
    geotag_ids = request.POST.getlist('geotags')
    cat_ids = request.POST.getlist('categories')
    type_id = request.POST.get('type')
    pub_id = request.POST.get('publication') if request.POST.get('publication') else None
    content.title = title
    content.type = Type.objects.get(id=type_id)
    content.featured = request.POST.get('featured')
    content.modified_by = request.POST.get('modified_by')
    content.created_by = request.POST.get('created_by')
    content.published = request.POST.get('action')

    if pub_id is not None:
        content.publication = Publication.objects.get(id=pub_id)
    content.content = request.POST.get('content')
    content.excerpt = request.POST.get('excerpt')
    content.url = request.POST.get('url')
    content.pub_date_y = request.POST.get('pub_date_y') if request.POST.get('pub_date_y') else None
    content.pub_date_m = request.POST.get('pub_date_m') if request.POST.get('pub_date_m') else None
    content.pub_date_d = request.POST.get('pub_date_d') if request.POST.get('pub_date_d') else None
    content.pub_date_full = int(request.POST.get('pub_date_y') or 0) * 10000 + int(
        request.POST.get('pub_date_m') or 0) * 100 + int(request.POST.get('pub_date_d') or 0)
    content.authors.set('')
    content.translators.set('')
    content.tags.set('')
    content.geotags.set('')
    content.category.set('')

    for x in authors_id:
        content.authors.add(Author.objects.get(id=x))
    for t in traslator_ids:
        content.translators.add(Author.objects.get(id=t))
    for y in tag_ids:
        content.tags.add(Tag.objects.get(id=y))
    for g in geotag_ids:
        content.geotags.add(Geotag.objects.get(id=g))
    for z in cat_ids:
        content.category.add(Category.objects.get(id=z))
    if 'pdf' in request.FILES:
        content.pdf_file = request.FILES['pdf']
    if 'img' in request.FILES:
        content.img = request.FILES['img']
    content.save()


@login_required(login_url='login')
def add_content(request):
    if request.method == "POST":
        content = Content.objects.create()
        save_content(request, content)

        return render(
            request,
            'add_content.html',
            {
                'authors': Author.objects.all(),
                'categories': Category.objects.all(),
                'tags': Tag.objects.all(),
                'geotags': Geotag.objects.all(),
                'types': Type.objects.all(),
                'publications': Publication.objects.all(),
                'msg': "content added"
            }
        )
    else:
        return  render(
            request,
            'add_content.html',
            {
                'authors': Author.objects.all(),
                'categories': Category.objects.all(),
                'tags': Tag.objects.all(),
                'geotags': Geotag.objects.all(),
                'types': Type.objects.all(),
                'publications': Publication.objects.all(),
            }
        )


@login_required(login_url='login')
def update_content(request, id):
    if User.is_staff:
        content = Content.objects.get(id=id)
        if request.method == 'POST':
            save_content(request, content)
            return redirect('/contents/' + str(id))
        else:
            return render(
                request,
                'add_content.html',
                {
                    'content': content,
                    'authors': Author.objects.all(),
                    'categories': Category.objects.all(),
                    'tags': Tag.objects.all(),
                    'geotags': Geotag.objects.all(),
                    'types': Type.objects.all(),
                    'publications': Publication.objects.all(),
                }
            )
    else:
        redirect('/contents/' + str(id))




def ajax_add_author(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        slug = request.POST.get('slug')
        author = Author.objects.create(
            first_name=first_name,
            last_name=last_name,
            slug=slug
        )
        return JsonResponse({'id': author.id, 'title': author.first_name+' '+author.last_name})

@csrf_exempt
def ajax_add_tag(request):
    if request.method == 'POST':
        title = request.POST.get('input')
        tag = Tag.objects.create(
            title=title
        )
        return HttpResponse(tag.id)



def ajax_add_geotag(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        slug = request.POST.get('slug')
        json_dat = json.loads(request.POST.get('json'))
        geotag = Geotag.objects.create(
            title=title,
            slug=slug,
            json=json_dat
        )
        return JsonResponse({'id': geotag.id, 'title': geotag.title})



@csrf_exempt
def ajax_add_cat(request):
    if request.method == 'POST':
        title = request.POST.get('input')
        category = Category.objects.create(
            title=title
        )
        return HttpResponse(category.id)


@csrf_exempt
def ajax_add_publication(request):
    if request.method == 'POST':
        title = request.POST.get('input')
        publication = Publication.objects.create(
            title=title
        )
        return HttpResponse(publication.id)


def del_content(request, id):
    if User.is_staff:
        content = Content.objects.get(id=id)
        content.delete()
        return redirect('/')
    else:
        return redirect('contents/'+str(id))
