import sys
import time
import traceback
import dis

from browser import document as doc, window,alert
from javascript import JSObject

# set height of container to 66% of screen
_height = doc.documentElement.clientHeight
_s = doc['container']
_s.style.height = '%spx' % int(_height*0.66)

#editor_value = "#Press the Run Button!\n\nprint('Welcome to Python Programming.net!')\nprint('See how easy it is to learn programming.')\n\n# This is a 'for loop':\n\nfor each_number in range(10):\n    print(each_number)\n\nprint('You've just run a Python program!')"
editor_value = "#Press the Run Button!\n\nprint('Welcome to Python Programming.net!')\nprint('See how easy it is to program.')\n\n# This is a 'for loop':\nfor each_number in range(4):\n    print(each_number)\n\nprint('You just ran a Python program!')\nprint('Try playing with the editor values, like changing the range or print functions, or get started by clicking on the Start Learning button.')"




has_ace = True
try:
    editor = window.ace.edit("editor")
    session = editor.getSession()
    session.setMode("ace/mode/python")

    editor.setOptions({
     'enableLiveAutocompletion': True,
     'enableSnippets': True,
     'highlightActiveLine': False,
     'highlightSelectedWord': True
    })
except:
    from browser import html
    editor = html.TEXTAREA(rows=20,cols=70)
    doc["editor"] <= editor
    def get_value(): return editor.value
    def set_value(x):editor.value=x
    editor.getValue = get_value
    editor.setValue = set_value
    has_ace = False

if sys.has_local_storage:
    from browser.local_storage import storage
else:
    storage = None

if 'set_debug' in doc:
    __BRYTHON__.debug = int(doc['set_debug'].checked)

def reset_src():
    if storage is not None and "py_src" in storage:
       editor.setValue(storage["py_src"])
    else:
       editor.setValue(editor_value)

    editor.scrollToRow(0)
    editor.gotoLine(0)

def reset_src_area():
    if storage and "py_src" in storage:
       editor.value = storage["py_src"]
    else:
       editor.value = editor_value

class cOutput:
    
    def write(self, data):
        doc["console"].value += str(data)

    def flush(self):
        pass

sys.stdout = cOutput()
sys.stderr = cOutput()

def to_str(xx):
    return str(xx)

info = sys.implementation.version
#doc['version'].text = '%s.%s.%s' %(info.major,info.minor,info.micro)

output = ''

def show_console(ev):
    doc["console"].value = output
    doc["console"].cols = 60

def run(in_globals=False):
    global output
    doc["console"].value=''
    src = editor.getValue()
    if storage is not None:
       storage["py_src"]=src

    t0 = time.perf_counter()
    try:
        if(in_globals):
            exec(src)
        else:
            ns = {}
            exec(src,ns)
        state = 1
    except Exception as exc:
        traceback.print_exc(file=sys.stderr)
        state = 0
    output = doc["console"].value

    print('<PythonProgramming.net>')
    return state

# load a Python script
def load_script(evt):
    _name=evt.target.value+'?foo=%s' %time.time()
    editor.setValue(open(_name).read())

def show_js(ev):
    src = editor.getValue()
    doc["console"].value = dis.dis(src)

if has_ace:
    reset_src()
else:
    reset_src_area()
