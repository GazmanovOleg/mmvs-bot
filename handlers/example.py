class Meeting:
    def __init__(self, meeting_id, date = None, time = None, service = None, connection = None, other = None):
        self.meeting_id = meeting_id
        self.date = date 
        self.time = time
        self.service = service
        self.connection = connection
        self.other = other 
    
    def get_meeting(self):
        return {self.meeting_id: [self.date, self.time, self.service, self.connection, self.other]}

class Meeting_list:
    def __init__(self):
        self.lst = []
    def add_to_list(self, item):
        id_lst = [i.meeting_id for i in self.lst]
        if item.meeting_id in id_lst:
            for i in range(len(self.lst)):
                if self.lst[i].meeting_id == item.meeting_id:
                    if item.date != None:
                        self.lst[i].date = item.date
                    if item.time != None:
                        self.lst[i].time = item.time
                    if item.service != None:
                        self.lst[i].service = item.service
                    if item.connection != None:
                        self.lst[i].connection = item.connection
                    if item.other != None:
                        self.lst[i].other = item.other
        else:
            self.lst.append(item)
        
        print(self.lst[0].get_meeting())
                
    def get_list(self):
        return [i.get_meeting() for i in self.lst]


if __name__ == '__main__':
    meeting_lst = Meeting_list()
    meet1 = Meeting(1234567, "th 23", "18-00"," ", "че бля")
    meet2 = Meeting(1234567, "th 24", "18-00", "узбечка")

    meeting_lst.add_to_list(meet2)
  

   
