echo "Testing"
pip install --use-wheel --find-links=dist/ django-angularui
echo "import angularui; print 'Hello World';" | python
