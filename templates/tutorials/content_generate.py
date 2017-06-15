from content_management import Content
import os

TOPIC_DICT = Content()

HTML_TEMPLATE = '''
{% extends "header.html" %}
{% block body %}
<!--    <pre class="prettyprint">   width="750" height="423" -->
<body class="body">

    <div class="container" align="left" style="max-width:800px">
        <div class="progress">
            <div class="progress-bar" role="progressbar" >Basic Progress: %s Progress: {{ completed_percentages['%s']}}%
            </div>
        </div>
    <h2>{{ curTitle }}</h2>
    <br>
    
    <p></p>
    <p></p>
    <p></p>
    <p></p>
    
    <div class="col l6"><p>"print()" is a built-in Python function that will output some text to the <kbd data-toggle="collapse" data-target="#consoleinfo" aria-expanded="false" aria-controls="consoleinfo">console</kbd>.</p>
		<div class="collapse" id="consoleinfo">
		  <div class="well">
			<p>When someone says to "print to the console," they are referring to where information from your program is ouput. This might be a command prompt (CMD.exe), the terminal for Mac/Linux users, or the interactive prompt in IDLE. You will see an example of "output to console" below.</p>
		  </div>
		</div></div></div>
        
        <div class="row">
        <div class="col-md-6">
        <pre class="prettyprint">
CODE HERE
        </pre></div>
        <div class="col-md-6">
        <p>EXPLANATION</p></div></div>
        
        <p>The next tutorial:<a title="{{ nextTitle }}" href="{{ nextLink }}?completed={{ curLink }}"><button class="btn">{{ nextTitle }}</button></a></p>
        </div>
    </body>
{% endblock %}
'''

for each_topic in TOPIC_DICT:
    print(each_topic)
    each_topic = each_topic
    os.makedirs(each_topic)
    
    for eachele in TOPIC_DICT[each_topic]:
        try:
            filename = (eachele[1]+'.html').replace("/","")
            print(filename)
            savePath = each_topic+'/'+filename
            saveData = (HTML_TEMPLATE.replace("%s",each_topic))
            
            template_save = open(savePath,"w")
            template_save.write(saveData)
            template_save.close()
        except Exception as e:
            print(str(e))
