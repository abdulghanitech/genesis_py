from flask import Flask
from flask import Response,render_template
from flask_cors import CORS, cross_origin
import time
import json
import datetime
from flask_restful import Resource, Api
# from adwords import download_criteria_report_with_awql as report
# from adwords import adwords_xml_report_into_db as adwords
# from adwords import adwords_analytics_data_merging as merge
# from analytics import analytics_data_into_db as analytics 
# from sessions import users_data as users

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}}) 
api = Api(app)

# class DateRange():
#     def __init__(self,start_date,end_date):
#         self.start_date=start_date
#         self.end_date=end_date
#         # print(start_date,end_date)

#     def date_range_for_analytics(self):
#         date_range_dict={'startDate':str(self.start_date),'endDate':str(self.end_date)}
#         # print(date_range_dict)
#         return date_range_dict

#     def date_range_for_adwords(self):
#         start_date=self.start_date.replace("-","")
#         end_date=self.end_date.replace("-","")
#         date_range_string=str(start_date)+","+str(end_date)        
#         # print(date_range_string)
#         return date_range_string
    
#     def date_for_download_xml(self,date):
#         _month=date.month
#         if date.month<10:
#             _month="0"+str(date.month)        

#         _day=date.day
#         if date.day<10:
#             _day="0"+str(date.day)        

#         # print(str(date.year)+str(_month)+str(_day))
#         return str(date.year)+str(_month)+str(_day) 

# class Adwords(Resource):    
#     def get(self):
#         start=time.time()                
#         adwords_data=merge.adwords_analytics_data_merging()
#         print(time.time()-start) 
#         return {'hello':adwords_data}
# api.add_resource(Adwords,"/adwords") 

# class DataWithinDateRange(Resource):
#     def get(self, startDate, endDate):
#         start=time.time()
#         obj=DateRange(startDate,endDate)        
#         ''' date range for downloading xml report '''
#         report.DATE_RANGE_FOR_XML=obj.date_range_for_adwords() 
#         analytics.DATE_RANGE_FOR_ANALYTICS=obj.date_range_for_analytics()
#         users.DATE_RANGE_FOR_USERS=obj.date_range_for_analytics()

#         adwords_data=merge.adwords_analytics_data_merging()

#         report.DATE_RANGE_FOR_XML='TODAY'
#         report.DATE_RANGE_FOR_ANALYTICS=1
#         users.DATE_RANGE_FOR_USERS=1

#         print(time.time()-start)
#         return{'hello':adwords_data}
# api.add_resource(DataWithinDateRange,'/data/date-range/<string:startDate>/<string:endDate>')  

# class DataWithinDays(Resource):
#     def get(self, days):
#         start=time.time()        
#         endDate=datetime.datetime.now().date()
#         startDate=endDate-datetime.timedelta(days=days)        
#         # print(startDate,endDate)
#         obj=DateRange(startDate,endDate)    
#         ''' date range for downloading xml report '''
#         xml_endDate=obj.date_for_download_xml(endDate)
#         xml_startDate=obj.date_for_download_xml(startDate)
#         # print("'"+xml_startDate+","+xml_endDate+"'") 
#         report.DATE_RANGE_FOR_XML=xml_startDate+","+xml_endDate

#         analytics.DATE_RANGE_FOR_ANALYTICS=obj.date_range_for_analytics()
#         users.DATE_RANGE_FOR_USERS=obj.date_range_for_analytics()
#         adwords_data=merge.adwords_analytics_data_merging()

#         report.DATE_RANGE_FOR_XML='TODAY'
#         report.DATE_RANGE_FOR_ANALYTICS=1
#         users.DATE_RANGE_FOR_USERS=1

#         print(time.time()-start)
#         return{'hello':adwords_data}
# api.add_resource(DataWithinDays,'/data/days/<int:days>')  

class HelloWorld(Resource):
    def get(self):
        # return {'hello': 'world'}
        return Response(render_template('index.html'),mimetype='text/html')
api.add_resource(HelloWorld, '/')
        # return Response(render_template('index.html'),mimetype='text/html')

# class AdwordsReport(Resource):    
#     def get(self):
#         report.download_criteria_report()        
#         return{'hello':'adwords_report'}          
# api.add_resource(AdwordsReport,"/adwords-report") 

if __name__ == '__main__':
    app.run(debug=True) 