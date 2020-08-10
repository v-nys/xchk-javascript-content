from xchk_core import contentviews as basecv
from xchk_core.courses import Course
from .contentviews import *

course = Course('javascript',
                'Javascript',
                [(DemoJavascriptView,[])],
                "git@github.com:v-nys/xchk-javascript-model-solutions.git")
