from django import forms


class SearchForm(forms.Form):
    app_title = forms.CharField(max_length=200, label='App title', help_text='part or whole of the app name')

    PRICE_CHOICES = (('all', 'All'), ('free', 'Free'), ('paid', 'Paid'))
    price = forms.ChoiceField(choices=PRICE_CHOICES, label='Price')

    CONTENT_RATING_CHOICES = (
        ('All', 'All'), ('Everyone', 'Everyone'), ('Low Maturity', 'Low Maturity'),
        ('Medium Maturity', 'Medium Maturity'),
        ('High Maturity', 'High Maturity'),)
    content_rating = forms.ChoiceField(choices=CONTENT_RATING_CHOICES, label='Content Rating')

    DOWNLOADS_CHOICES = (('All', 'All'), ('0', '0'), ('1 - 5', '1 - 5'), ('5 - 10', '5 - 10'), ('10 - 50', '10 - 50'),
                         ('50 - 100', '50 - 100'), ('100 - 500', '100 - 500'), ('500 - 1,000', '500 - 1K'),
                         ('1,000 - 5,000', '1K - 5K'), ('5,000 - 10,000', '5K - 10K'), ('10,000 - 50,000', '10K - 50K'),
                         ('50,000 - 100,000', '50K - 100K'), ('100,000 - 500,000', '100K - 500K'),
                         ('500,000 - 1,000,000', '500K - 1M'), ('1,000,000 - 5,000,000', '1M - 5M'),
                         ('5,000,000 - 10,000,000', '5M - 10M'), ('10,000,000 - 50,000,000', '10M - 50M'),
                         ('50,000,000 - 100,000,000', '50M - 100M'), ('100,000,000 - 500,000,000', '100M - 500M'),
                         ('500,000,000 - 1,000,000,000', '500M - 1B'), ('1,000,000,000 - 5,000,000,000', '1B - 5B'))
    downloads = forms.ChoiceField(choices=DOWNLOADS_CHOICES, label='Downloads')

    RATING_CHOICES = (('Any', 'Any'), ('>1', '>1'), ('>2', '>2'), ('>3', '>3'), ('>4', '>4'), ('5', '5'))
    rating = forms.ChoiceField(choices=RATING_CHOICES, label='User rating')

    CATEGORY_CHOICES = (
        ('All', 'All' ), ('Educational', 'Educational' ), ('Puzzle', 'Puzzle' ), ('Entertainment', 'Entertainment'),
        ('Racing', 'Racing'), ('uncategorized', 'uncategorized'), ('Family', 'Family'),
        ('Role Playing', 'Role Playing'),
        ('Action', 'Action'), ('Finance', 'Finance'), ('Shopping', 'Shopping'), ('Adventure', 'Adventure'),
        ('Health & Fitness', 'Health & Fitness'), ('Simulation', 'Simulation'), ('Arcade', 'Arcade'),
        ('Libraries & Demo', 'Libraries & Demo'), ('Social', 'Social'), ('Board', 'Board'), ('Lifestyle', 'Lifestyle'),
        ('Sports', 'Sports'), ('Books & Reference', 'Books & Reference'), ('Media & Video', 'Media & Video'),
        ('Strategy', 'Strategy'), ('Business', 'Business'), ('Medical', 'Medical'), ('Tools', 'Tools'),
        ('Card', 'Card'),
        ('Music', 'Music'), ('Transportation', 'Transportation'), ('Casino', 'Casino'),
        ('Music & Audio', 'Music & Audio'),
        ('Travel & Local', 'Travel & Local'), ('Casual', 'Casual'), ('News & Magazines', 'News & Magazines'),
        ('Trivia', 'Trivia'), ('Comics', 'Comics'), ('Personalization', 'Personalization'), ('Weather', 'Weather'),
        ('Communication', 'Communication'), ('Photography', 'Photography'), ('Word', 'Word'),
        ('Education', 'Education'),
        ('Productivity', 'Productivity'))
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label='Category')
    CLUSTER_CHOICES = (
    ('Any', 'Any'), ('6', '6: perfect apps'), ('1', '1: successful apps'), ('4', '4: high rated apps with average downloads'),
    ('0', '0: high rated apps with low downloads'), ('2', '2: average to low apps'), ('3', '3: no good apps'))
    cluster = forms.ChoiceField(choices=CLUSTER_CHOICES, label='Cluster')

    LANGUAGE_CHOICE = (('All', 'All'), ('en', 'En'), ('ar', 'Ar'), ('other', 'Other'))
    language = forms.ChoiceField(choices=LANGUAGE_CHOICE, label='Language')

