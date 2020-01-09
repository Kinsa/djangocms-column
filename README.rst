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

The Column plugin has parameters for width. With these parameter you can control the width
of the column via classes.

The columns are built using flexbox and will display as a row. This is important to note -- a column set to 100% width adjacent to another column will not fill out the whole space but will follow the rules of flexbox, taking up 100% of the remaining space after the other column, so that two columns set to 100% width will actually take up 50% of the parent.

There are 4 breakpoints, XS and SM are required, MD and LG are optional. The breakpoints are:

* xs: < 768px
* sm: >= 768px
* md: >= 992px
* lg: >= 1200px


Add to your CSS::

    /* responsive multi-column layout */

    /*

     * -xs- : < 768px
     * -sm- : >= 768px
     * -md- : >= 992px
     * -lg- : >= 1200px

    */

    .col-sm-10pct,
    .col-sm-25pct,
    .col-sm-33pct,
    .col-sm-50pct,
    .col-sm-66pct,
    .col-sm-75pct,
    .col-md-10pct,
    .col-md-25pct,
    .col-md-33pct,
    .col-md-50pct,
    .col-md-66pct,
    .col-md-75pct,
    .col-lg-10pct,
    .col-lg-25pct,
    .col-lg-33pct,
    .col-lg-50pct,
    .col-lg-66pct,
    .col-lg-75pct {
      float: left;
    }

    @media screen and (max-width: 767px) {
      .col-xs-10pct,
      .col-xs-25pct,
      .col-xs-33pct,
      .col-xs-50pct,
      .col-xs-66pct,
      .col-xs-75pct {
        float: left;
      }

      .col-xs-10pct {
        width: 10%;
      }
      
      .col-xs-25pct {
        width: 25%;
      }
      
      .col-xs-33pct {
        width: 33%;
      }
      
      .col-xs-50pct {
        width: 50%;
      }
      
      .col-xs-66pct {
        width: 66%;
      }
      
      .col-xs-75pct {
        width: 75%;
      }
      
      .col-xs-100pct {
        width: 100%;
      }
    }

    @media screen and (min-width: 768px) {
      .col-sm-10pct,
      .col-sm-25pct,
      .col-sm-33pct,
      .col-sm-50pct,
      .col-sm-66pct,
      .col-sm-75pct {
        float: left;
      }

      .col-sm-10pct {
        width: 10%;
      }
      
      .col-sm-25pct {
        width: 25%;
      }
      
      .col-sm-33pct {
        width: 33%;
      }
      
      .col-sm-50pct {
        width: 50%;
      }
      
      .col-sm-66pct {
        width: 66%;
      }
      
      .col-sm-75pct {
        width: 75%;
      }
      
      .col-sm-100pct {
        width: 100%;
      }
    }

    @media screen and (min-width: 992px) {
      .col-md-10pct,
      .col-md-25pct,
      .col-md-33pct,
      .col-md-50pct,
      .col-md-66pct,
      .col-md-75pct {
        float: left;
      }

      .col-md-10pct {
        width: 10%;
      }
      
      .col-md-25pct {
        width: 25%;
      }
      
      .col-md-33pct {
        width: 33%;
      }
      
      .col-md-50pct {
        width: 50%;
      }
      
      .col-md-66pct {
        width: 66%;
      }
      
      .col-md-75pct {
        width: 75%;
      }
      
      .col-md-100pct {
        width: 100%;
      }
    }

    @media screen and (min-width: 1200px) {
      .col-lg-10pct,
      .col-lg-25pct,
      .col-lg-33pct,
      .col-lg-50pct,
      .col-lg-66pct,
      .col-lg-75pct {
        float: left;
      }

      .col-lg-10pct {
        width: 10%;
      }
      
      .col-lg-25pct {
        width: 25%;
      }
      
      .col-lg-33pct {
        width: 33%;
      }
      
      .col-lg-50pct {
        width: 50%;
      }
      
      .col-lg-66pct {
        width: 66%;
      }
      
      .col-lg-75pct {
        width: 75%;
      }
      
      .col-lg-100pct {
        width: 100%;
      }
    }


Translations
------------

If you want to help translate the plugin please do it on transifex:

https://www.transifex.com/projects/p/django-cms/resource/djangocms-column/
