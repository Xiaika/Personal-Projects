# Simple RestAPI using Bottle - From course BigIdeasLittle Code
from bottle import *
from pprint import pprint
import time
import algebra


@route('/')
def welcome():
    response.set_header('Vary', 'Accept')
    pprint(dict(request.headers))
    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'
        return '<h1> Howdy! </h1>'
    response.content_type = 'text/plain'
    return 'Hello'


@route('/now')
def time_service():
    response.content_type = 'text/plain'
    response.set_header('Cache-Control', 'max-age=1')
    return time.ctime()


@route('/upper/<word>')
def upper_case(word: str):
    response.content_type = 'text/plain'
    return word.upper()


secret = 'the average life expectancy of a stark or targaryen is short'


@route('/area/circle')
def circle_area_service():

    last_visit = request.get_cookie('last-visit', 'unknown', secret=secret)
    print(f'Last visit {last_visit}')
    response.set_cookie('last-visit', time.ctime(), secret=secret)
    response.set_header('Vary', 'Accept')
    try:
        radius = float(request.query.get('radius', '0.0'))
    except ValueError as e:
        return e.args[0]
    area = algebra.area_circle(radius)
    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'
        return f'<p> The area is <em> {area:.2f} </em> </p>'
    area = round(area, 3)
    return dict(radius=radius, area=area, service=request.path)


# File server ================================================================

file_template = """\
<h1> List of files in <em> Congress Data </em> directory: </h1> 
<hr>
<ol>
    % for file in files:
        <li> <a href="files/{{file}}"> {{file}} </a> </li>
    % end
</ol>
"""

@route('/files')
def show_files():
    response.set_header('Vary', 'Accept')
    files = os.listdir('congress_data')
    if 'text/html' not in request.headers.get('Accept', '*/*'):
        return dict(files=files)
    return template(file_template, files=files)


@route('/files/<filename>')
def serve_one_file(filename):
    return static_file(filename, './congress_data')


if __name__ == '__main__':
    # Develop on local host, an empty string will make the website public
    # Also can use local host forever and port forward later
    run(host='', port=8080)


