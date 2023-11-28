"""CSCA08 Assignment 3: arxiv.org

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2021-2023 Anya Tafliovich.

"""

import copy  # needed in examples of functions that modify input dict
from typing import TextIO

# remove unused constants from this import statement when you are
# finished your assignment
from constants import (ID, TITLE, CREATED, MODIFIED, AUTHORS,
                       ABSTRACT, END, SEPARATOR, NameType,
                       ArticleValueType, ArticleType, ArxivType)


EXAMPLE_ARXIV = {
    '008': {
        'identifier': '008',
        'title': 'Intro to CS is the best course ever',
        'created': '2021-09-01',
        'modified': None,
        'authors': [('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')],
        'abstract': '''We present clear evidence that Introduction to
Computer Science is the best course.'''},
    '031': {
        'identifier': '031',
        'title': 'Calculus is the best course ever',
        'created': None,
        'modified': '2021-09-02',
        'authors': [('Breuss', 'Nataliya')],
        'abstract': '''We discuss the reasons why Calculus I
is the best course.'''},
    '067': {'identifier': '067',
            'title': 'Discrete Mathematics is the best course ever',
            'created': '2021-09-02',
            'modified': '2021-10-01',
            'authors': [('Bretscher', 'Anna'), ('Pancer', 'Richard')],
            'abstract': ('We explain why Discrete Mathematics is the best ' +
                         'course of all times.')},
    '827': {
        'identifier': '827',
        'title': 'University of Toronto is the best university',
        'created': '2021-08-20',
        'modified': '2021-10-02',
        'authors': [('Bretscher', 'Anna'),
                    ('Ponce', 'Marcelo'),
                    ('Tafliovich', 'Anya Y.')],
        'abstract': '''We show a formal proof that the University of
Toronto is the best university.'''},
    '042': {
        'identifier': '042',
        'title': None,
        'created': '2021-05-04',
        'modified': '2021-05-05',
        'authors': [],
        'abstract': '''This is a very strange article with no title
and no authors.'''}
}

EXAMPLE_BY_AUTHOR = {
    ('Ponce', 'Marcelo'): ['008', '827'],
    ('Tafliovich', 'Anya Y.'): ['008', '827'],
    ('Bretscher', 'Anna'): ['067', '827'],
    ('Breuss', 'Nataliya'): ['031'],
    ('Pancer', 'Richard'): ['067']
}


# We provide the header and docstring for this function to get you
# started and to demonstrate that there are no docstring examples in
# functions that read from files.
def read_arxiv_file(afile: TextIO) -> ArxivType:
    """Return a dict containing all arxiv information in afile.

    Precondition: afile is open for reading
                  afile is in the format described in the handout
    """

    pass

def get_coauthors(id_to_article: ArxivType, author_name: NameType) -> list[NameType]:
    pass

def get_most_published_authors(id_to_article: ArxivType) -> list[NameType]:
    pass

def suggest_collaborators(id_to_article: ArxivType, author_name: NameType) -> list[NameType]:
    pass

def has_prolific_authors() -> bool:
    pass

def keep_prolific_authors(id_to_article: ArxivType, prolific_threshold: int) -> None:
    pass


# We provide the header and part of a docstring for this function to
# get you started and to demonstrate the use of example data.
def make_author_to_articles(
        id_to_article: ArxivType) -> dict[NameType, list[str]]:
    """Return a dict that maps each author name to a list (sorted in
    lexicographic order) of IDs of articles written by that author,
    based on the information in arxiv data id_to_article.

    >>> make_author_to_articles(EXAMPLE_ARXIV) == EXAMPLE_BY_AUTHOR
    True

    """

    pass


# We provide the header and part of a docstring for this function to
# get you started and to demonstrate the use of function deepcopy in
# examples that modify input data.
def keep_prolific_authors(id_to_article: ArxivType,
                          min_publications: int) -> None:
    """Update the articles data id_to_article so that it contains only
    articles published by authors with min_publications or more
    articles published. As long as at least one of the authors has
    min_publications, the article is kept.

    >>> arxiv_copy = copy.deepcopy(EXAMPLE_ARXIV)
    >>> keep_prolific_authors(arxiv_copy, 2)
    >>> len(arxiv_copy)
    3
    >>> '008' in arxiv_copy and '067' in arxiv_copy and '827' in arxiv_copy
    True
    """

    pass


if __name__ == '__main__':

    import doctest
    doctest.testmod()

    # uncomment to test with example data files
    # with open('example_data.txt', encoding='utf-8') as example_data:
    #     RESULT = read_arxiv_file(example_data)
    #     print('Did we produce a correct dict? ',
    #           RESULT == EXAMPLE_ARXIV)

    # # uncomment to work with a larger data set
    # with open('data.txt', encoding='utf-8') as data_txt:
    #     EXAMPLE = read_arxiv_file(data_txt)

    # EXAMPLE_AUTHOR_TO_ARTICLE = make_author_to_articles(EXAMPLE)
    # EXAMPLE_MOST_PUBLISHED = get_most_published_authors(EXAMPLE)
    # print(EXAMPLE_MOST_PUBLISHED)
    # print(get_coauthors(EXAMPLE, ('Varanasi', 'Mahesh K.')))  # one
    # print(get_coauthors(EXAMPLE, ('Chablat', 'Damien')))  # many
