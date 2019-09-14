import json
# Write JSON file
def writeToJSONFile(path, fileName, data):
    filePathNameWExt = 'C:/Users/Public/'  + 'biodata' + '.json'
    # JSON file path
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)
# Biodata

data = {}
data['nama'] = 'Toto Bachtiar Palokoto'
data['age'] = 25
data['address'] = 'Jl Pucang Anom Timur Raya 16'
data['hobbies'] = 'Membaca', 'Menonton Film', 'Olahraga'
data['is_married'] = False
data['list-school'] = {'key_name': 'Politeknik Negeri Semarang',
                       'year_in':2012,
                       'year_out':2017,
                       'major': 'Teknik Elektro'
                       }
data['skills'] = { 'skill_name': {
                            'Programming': 
                                        {   'level':'Beginner' }
                                                ,
                            'Editing Video':{'level':'Advance'}
                                 }
                  
                  }
data['interest_in_coding']=True




writeToJSONFile('C:/Users/Public/','biodata',data)
# './' represents the current directory so the directory save-file.py is in
# 'test' is my file name
