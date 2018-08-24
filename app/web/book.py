from . import web


@web.route('/book')
def get_book():
    return "there are many books"
