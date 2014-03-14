from Products.CMFCore.utils import getToolByName
from zope.component.hooks import getSite
import os.path


ASSETS = os.path.join(os.path.dirname(__file__), 'assets')
OFFICE_MIME = 'application/vnd.openxmlformats-officedocument.'
MIMETYPES_BY_EXTENSION = {
    '.docx': '%swordprocessingml.document' % OFFICE_MIME,
    '.pdf': 'application/pdf'}


def convert_asset(filename):
    path = os.path.join(ASSETS, filename)
    transforms = getToolByName(getSite(), 'portal_transforms')
    _, extension = os.path.splitext(filename)
    mimetype = MIMETYPES_BY_EXTENSION[extension]
    with open(path, 'r') as asset:
        stream = transforms.convertTo('text/plain', asset, mimetype=mimetype,
                                      filename=filename)
        return stream.getData().strip()
