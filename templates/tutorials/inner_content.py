from content_management import Content

TOPIC_DICT = Content()

FUNC_TEMPLATE = '''
@app.route(TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][1],methods=['GET','POST'])
def CURRENTTITLE():
    update_user_tracking()
    completed_percentages = topic_completion_percent()
    return render_template("tutorials/CURRENTTOPIC/CURRENTHTML",completed_percentages=completed_percentages,curLink=TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][1],curTitle=TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][0],nextLink=TOPIC_DICT["CURRENTTOPIC"][NEXTINDEX][1],nextTitle=TOPIC_DICT["CURRENTTOPIC"][NEXTINDEX][0])
'''

filename = "generated_func.py"
temp_save = open(filename,"a")
for each_topic in TOPIC_DICT:
    
    index_counter = 0
    
    for eachele in TOPIC_DICT[each_topic]:
        try:
            CURRENTHTML = (eachele[1]+'.html').replace("/","")
            CURRENTTOPIC = each_topic
            CURRENTTITLE = eachele[0].replace("-","_").replace(" ","_").replace("/","").replace(":","").replace(",","")
            CURRENTINDEX = str(index_counter)
            NEXTINDEX = str(index_counter + 1)
            index_counter += 1
            
            temp_save.write (FUNC_TEMPLATE.replace("CURRENTTOPIC",CURRENTTOPIC).replace("CURRENTINDEX",CURRENTINDEX).replace("NEXTINDEX",NEXTINDEX).replace("CURRENTTITLE",CURRENTTITLE).replace("CURRENTHTML",CURRENTHTML))
        except Exception as e:
            print str(e)

temp_save.close()            