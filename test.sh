set -e
echo "Testing"
pip install --find-links=dist/ $PACKAGE_NAME
echo "import angularui; print 'Hello World';" | python
