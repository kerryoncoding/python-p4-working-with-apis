
import requests
import json

class GetPrograms:

  def get_programs(self):
    # URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
    URL = "https://data.cityofchicago.org/resource/ydr8-5enu.json"
    # URL = "https://dev.socrata.com/foundry/data.cityofnewyork.us/szgz-awuh"


    response = requests.get(URL)
    return response.content
  
  def program_agencies(self):
    # we use the JSON library to parse the API response into nicely formatted JSON
      programs_list = []
      programs = json.loads(self.get_programs())
      for program in programs:
        programs_list.append(program["agency"])

      return programs_list

# programs = GetPrograms().get_programs()
# print(programs)
  
programs = GetPrograms()
agencies = programs.program_agencies()

for agency in set(agencies):
  print(agency) 

 