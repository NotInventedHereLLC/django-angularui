echo "Testing"
pip install --use-wheel --find-links=dist/ $PACKAGE_NAME
echo "import angularui; print 'Hello World';" | python
