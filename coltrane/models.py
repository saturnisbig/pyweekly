import datetime

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
#from django.conf import settings

from taggit.managers import TaggableManager
from markdown import markdown


class Category(models.Model):
    title = models.CharField(max_length=250, help_text="Maximum 250 characters.")
    slug = models.SlugField(unique=True, help_text="\
                            Suggested value automatically generated from\
                            title. Must be unique.\
                            ")
    description = models.TextField()

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('coltrane_category_detail', kwargs={'slug': self.slug})
        #return '/categories/%s/' % self.slug

    def live_entry_set(self):
        from coltrane.models import Entry
        return self.entry_set.filter(status=Entry.LIVE_STATUS)


class LiveEntryManager(models.Manager):
    def get_query_set(self):
        return super(LiveEntryManager, self).get_query_set().filter(
            status=self.model.LIVE_STATUS
        )



class Entry(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )
    # Core fields.
    title = models.CharField(max_length=250,
                             help_text="Maximum 250 characters.")
    excerpt = models.TextField(blank=True,
                               help_text="A short summary of the entry.\
                               Optional.")
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    # Fields to stored generated HTML.
    excerpt_html = models.TextField(editable=False, blank=True)
    body_html = models.TextField(editable=False, blank=True)

    # Metadata.
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(True)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(unique_for_date='pub_date',
                            help_text="Suggested value automatically generated\
                            from title. Must be unique.")
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS,
                                 help_text="Only entries with live status will\
                                 be publicly displayed.")

    # Categorization.
    categories = models.ManyToManyField(Category)
    tags = TaggableManager()

    # Manager
    objects = models.Manager()
    live = LiveEntryManager()

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = "Entries"

    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, forse_update=False):
        self.body_html = markdown(self.body)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
        super(Entry, self).save(force_insert, forse_update)

    def get_absolute_url(self):
        return reverse('coltrane_entry_detail', kwargs={
            'year': self.pub_date.strftime("%Y"),
            'month': self.pub_date.strftime("%b").lower(),
            'day': self.pub_date.strftime("%d"),
            'slug': self.slug})
    #    return ('coltrane_entry_detail', (),
    #            {'year': self.pub_date.strftime("%Y"),
    #             'month': self.pub_date.strftime("%b").lower(),
    #             'day': self.pub_date.strftime("%d"),
    #             'slug': self.slug})
    #get_absolute_url = models.permalink(get_absolute_url)
        #return "/weblog/%s/%s/" % (self.pub_date.strftime('%Y/%b/%d').lower(),
        #                           self.slug)


class Link(models.Model):
    # Metadata.
    enable_comments = models.BooleanField(default=True)
    post_elsewhere = models.BooleanField('Post to del.icio.us',
                                         default=True,
                                         help_text="If checked this post will \
                                         be posted both to your weblog and \
                                         your delicious account.")
    posted_by = models.ForeignKey(User)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    slug = models.SlugField(unique_for_date='pub_date',
                            help_text="Must be unique for publication date.")

    title = models.CharField(max_length=250)

    # The actual link bits.
    description = models.TextField(blank=True)
    description_html = models.TextField(editable=False, blank=True)
    via_name = models.CharField('Via', max_length=250, blank=True,
                                help_text="The name of the person whose site \
                                you spotted the link on. Optional.")
    via_url = models.URLField('Via_URL', blank=True,
                              help_text="The URL of the site where you \
                              spotted the link. Optional.")
    url = models.URLField()
    tags = TaggableManager()
    url = models.URLField("URL", unique=True)

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.title

    def save(self):
        #if not self.id and self.post_elsewhere:
        #    import pydelicious
        #    from django.utils.encoding import smart_str
        #    pydelicious.add(settings.DELICIOUS_USER,
        #                    settings.DELICIOUS_PASSWORD,
        #                    smart_str(self.url),
        #                    smart_str(self.title),
        #                    smart_str(self.tags))
        if self.description:
            self.description_html = markdown(self.description)
        super(Link, self).save()

    def get_absolute_url(self):
        return reverse('coltrane_link_detail', kwargs={
            'year': self.pub_date.strftime('%Y'),
            'month': self.pub_date.strftime('%b').lower(),
            'day': self.pub_date.strftime('%d'),
            'slug': self.slug
        })
