from xchk_core.contentviews import ContentView
from xchk_core.strats import *

class DemoJavascriptView(ContentView):
     
    uid = 'xchk_javascript_content_demo'
    template = 'xchk_javascript_content/xchk_javascript_content_demo.html'
    strat = Strategy(refusing_check=TrueCheck(),
                     accepting_check=Negation(TrueCheck()))
