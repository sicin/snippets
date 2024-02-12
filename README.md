# My Programming Journey

- [Introduction](#introduction)
- [The Beginnings](#the-beginnings)
  - [edX Course](#edx-course)
  - [Bachelor's Thesis](#bachelor-s-thesis)
- [Leiden University](#leiden-university)
  - [Attending the _Constructing Digital Language Toolkits_ Class](#attending-the--constructing-digital-language-toolkits--class)
  - [Researching China’s Role in Cyber Security](#researching-china-s-role-in-cyber-security)
  - [Web Content Creator for OpenPhilology](#web-content-creator-for-openphilology)
  - [TAing for _Constructing Digital Language Toolkits_ Class](#taing-for--constructing-digital-language-toolkits--class)
- [Sinoreporter](#sinoreporter)
- [Freelancing](#freelancing)
- [Simplicity](#simplicity)
- [Personal Projects](#projects)

<br>

# Introduction

This repository outlines my IT experience, presenting the progress and projects I made throughout my programming journey. Apart from learning about my background, I will be providing excerpts from code I have written (anonymized where necessary).

<br>

# The Beginnings

## edX Course

### < 1 yr. Python experience

**Stack: Python (Jupyter Notebook)**

It all started in 2017 with [Microsoft's Python course on edX](https://learning.edx.org/course/course-v1:Microsoft+DEV236x+1T2017/home). It was my first experience with for loops, while statements, functions, if/else, etc. I found the topic extremely interesting and completed the whole course, learning about the basics of programming in the process. Below is the final assignment diagram:

<img src="Images/final-assignment.png" alt="The forever (while True) loop diagram" width="500">

#### [Link to my solution](Certificates/adding_report.py)

Soon after I completed another course from DataCamp:
<img src="Certificates/datacamp.png" alt="DataCamp certificate" width="500">

<br>

## Bachelor's Thesis

Back then I only wanted to learn Python for my research in general and my Bachelor's thesis in particular. I was able to apply this newly obtained skill into my thesis, graphing out text reuse between several ancient Chinese texts. The inclusion of digital humanities section was met with much interest and recognition from the reviewers.

![N-gram text reuse](Images/thesis.png)

<br>

# Leiden University

## Attending the _Constructing Digital Language Toolkits_ Class

### < 1 yr. Python experience

**Stack: Python, Django, HTML, CSS**

One of my motivations for applying for a Master's Degree in Chinese Studies in Leiden was my growing interest in digital humanities. They had a class called _Constructing Digital Language Toolkits_, which was exactly what I wanted at the time. Combining programming with my major and interests, that sounded great. And it was great!

The course was taught by [Dr. Christopher Handy](https://github.com/handyc), an amazing person to whom I owe a lot, since he enabled me to delve deeper into the world of programming. During this one-semester course we were learning the basics of unix systems and command line, SQL databases, HTML, CSS, JavaScript, Python, and Django.

Fueled by a deep passion for the subject I went far and beyond with my final project. I created a full-fledged, responsive (albeit a bit ugly) website converting Chinese units and measurements into their Western counterparts.

![](DjangoConverter/Converter.gif)

Definitely the biggest achievement at this point was the creation of a pretty complex algorithm converting Chinese numerals into Arabic numbers. Since there were no real examples (and one algorithm written in Perl actually had erroneous output in many cases) I had to create it from ground-up. Here's the code if you're interested (types were added later) and some examples:

一千二百三十四亿五千六百七十八万九千 --> 123456789000

四千万零一十 --> 40000010

二亿五千四百三十一万五千 --> 254315000

#### [Algorithm converting Chinese numerals into Arabic numbers](PythonConverterAlgorithm/converter_trillion.py)

#### [Test cases](PythonConverterAlgorithm/converter_test.py)

<br>

## Researching China’s Role in Cyber Security

While in Leiden, I was lucky enough to get hired for a research assistant position at [Leiden Asia Centre](https://leidenasiacentre.nl/), a leading European thin-tank specializing in Asia. Although the bulk of my responsibilities were research- or translation- related, with some Airtable added to the mix, it was a great learning experience for me, solidifying my overall understanding of cyberspace and tech in general.

You can even find me as the co-author of a paper released by LAC: _[How Asia Confronts COVID-19 through Technology](https://leidenasiacentre.nl/how-asia-confronts-covid-19-through-technology-2/)_.

<br>

## Web Content Creator for OpenPhilology

**Stack: Grav CMS, HTML, CSS**

Creating web content for OpenPhilology was my other part-time job back then. Apart from learning more about Buddhism and helping out the team with internal tasks, I was working with Grav CMS (sometimes sprinkled with some basic HTML and CSS). This in turn introduced me to YAML files and their syntax. Slowly but surely, I was adding new tools to my toolbox.

<br>

## TAing for _Constructing Digital Language Toolkits_ Class

### ~1 yr. Python experience

**Stack: Python (Pandas, Matplotlib), Django, Bash**

As the new academic year started, I was asked by Chris Handy whether I'd be open to become the Teaching Assistant for his class. I loved the idea and immediately agreed.

I was tasked with tutoring students and helping them with their homeworks and final projects. However, since the class was taking place online, with students having to log into the server, I created a tool tracking students' presence on the server.

![Assignment 10](Images/assignment-10.png)
![Deadline madness](Images/deadline.png)
![Total time spent on the server](Images/time-spent.png)

As you can see, the last few days before the final deadline were hectic! I was also spending most of my time helping students with their projects. Most were done in Django, making it a good practice for me as well. Some created basic websites, others opted for specialized dictionaries, one person even made an Anki-like flashcards app.

The class was a huge success and many more students handed out their final assignments than years prior!

#### [Bash script run by a cronjob](PythonServerPresenceTool/stalker.sh)

#### [Processing and analyzing data with Python](PythonServerPresenceTool/stalker_prog.ipynb)

<br>

# Sinoreporter

### > 1 yr. Python experience

**Stack: Python, Django, MongoDB (Atlas + Charts), CSS (Bootstrap), Raspberry PI, Heroku**

As thanks for TAing, Chris gifted me Raspberry Pi 4, which was a great, nerdy present. I was deliberating how to use it best and soon came up with an idea I'd had for quite some time - to create a news site with articles about China from all over the world! But why would anyone need a Raspberry Pi for that? Well, I decided to fully automate the process and provide China news to the world in a concise form (infopills as you may).

The first step was finding proper APIs for gathering news, creating summaries, and translating them. My choice for the news was the industry standard, NewsAPI. As for the other two, I decided on SMMRY and Google Translate. In a few short weeks my news-generating machine was ready. You can find some snippets of the script here: link.

Due to my prior experience with Django, it was a no-brainer, unfortunately I made a mistake of choosing a NoSQL database (MongoDB), which is totally not compatible with the Django ORM and the connector library *djongo* made it impossible for me to update the dependencies...Basically, a huge nuisance, especially since my data is now structured and consistent. The unavoidable migration process to PostgreSQL is still not finished at the day of writing this text.

When everything was set and ready, I deployed the app to Heroku (when I started with the code it still used to be free), bought a domain on Gandi.net and spun up a new database on MongoDB Atlas and embellished it with some basic graphs using MongoDB Charts. Thus, Sinoreporter.com had come to existance, and every 2 hours new articles - fully summarized and translated into Polish - were being added to the website. Shortly after I also decided to add translated Chinese headlines to the mix.

As of writing this text, there are over 70k articles, 200k headlines, and 200 registered users. Not a huge success commercially but it was never supposed to be. It was still a success for me, since I was able to single-handadly create a complete web application from the very first commit to a sucessful deployment.

# Freelancing

**Stack: Python, Django, React, CSS (SASS), PostgreSQL**

# Simplicity

### > 3 yrs Python experience </br> > 2 yrs React experience

**Stack: TypeScript, Python, React, Node.js, MongoDB, CSS (SASS, Tailwind CSS), Material UI, RabbitMQ, Elasticsearch, Docker, Kubernetes**

# Personal Projects

## WWN Character Sheet Creator

## Playing around with C

## JSON Complexity App
