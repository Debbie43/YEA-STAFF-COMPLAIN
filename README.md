# YEA-Staff-Complain

## Set Up Instructions
1. Clone the repository
<pre>
git clone repository_url
</pre>

2. Create and activate virtual environment
<pre>
python -m venv env
.\env\Scripts\activate.bat
</pre>

2. Install project dependencies
<pre>
pip install -r requirements.txt
</pre>

3. Make and apply migrations
<pre>
python manage.py makemigrations
python manage.py migrate
</pre>

4. Create a superuser by running the command and completing the prompts
<pre>
python manage.py createsuperuser
</pre>

5. Finally run the project
<pre>
python manage.py runserver
</pre>

## Page URLs
`/admin` - Admininistrator panel

`/create` - Staff complaint page

`/create/success` - Complain creation success page