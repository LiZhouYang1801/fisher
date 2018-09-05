from . import web


@web.route('/book')
def get_book():
    return "welcome my books"
