djangocms-column
================

A Multi Column Plugin for django CMS.


This Fork
---------

This fork of djangocms-column utilizes djangocms-attributes-field to be able to apply attributes like classes to the columns.


Installation
------------

This plugin requires `django CMS` 3.4.5 or higher to be properly installed as well as the `django CMS Attributes Field` plugin.

Install the django CMS Attributes Field plugin according to the instructions: https://github.com/divio/djangocms-attributes-field

Then:

* In your projects virtualenv, run ``pip install git+https://github.com/Kinsa/djangocms-column.git``.
* Add ``'djangocms_column'`` to your ``INSTALLED_APPS`` setting.
* Run ``manage.py migrate djangocms_column``.


Usage
-----

There are 2 plugins: MultiColumn and Column
The first is MultiColumn that should be added to your placeholder conf.
MultiColumn only allows one plugin as a child: the Column plugin.
The Column plugin has a parameter width. With this parameter you can control the width
of the column via classes.

You can add a new setting to your settings.py called `COLUMN_WIDTH_CHOICES`

the default is::

	COLUMN_WIDTH_CHOICES = (
        ('10%', _("col-10pct")),
        ('25%', _("col-25pct")),
        ('33.33%', _('col-33pct')),
        ('50%', _("col-50pct")),
        ('66.66%', _('col-66pct')),
        ('75%', _("col-75pct")),
        ('100%', _('col-100pct')),
	)

but you can change that to fit your CSS grid framework or other purposes.

Add to your CSS::

    .col-10pct,
    .col-25pct,
    .col-33pct,
    .col-50pct,
    .col-66pct,
    .col-75pct,
    .col-100pct {
      float: left;
    }

    .col-10pct {
      width: 10%;
    }

    .col-25pct {
      width: 25%;
    }

    .col-33pct {
      width: 33%;
    }

    .col-50pct {
      width: 50%;
    }

    .col-66pct {
      width: 66%;
    }

    .col-75pct {
      width: 75%;
    }

    .col-100pct {
      width: 100%;
    }


Translations
------------

If you want to help translate the plugin please do it on transifex:

https://www.transifex.com/projects/p/django-cms/resource/djangocms-column/
