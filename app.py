from flask import*
from flask_restful import Api
app = Flask(__name__)

api = Api(app)
from datetime import timedelta
from flask_jwt_extended import JWTManager


# SET UP JWT
app.secret_key="shfduifgdiusisdfguefiedid7874u948348ujjdkcdjbive##222!!!1!!5e5ufdhubhwuibcvijhbdlldkvndflkvndfvkdfgkitro"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
jwt = JWTManager(app)


# endpoints/ routes

from views.views import MemberSignup,MemberSignin,MemberProfile,AddDependant, ViewDependants,Laboratories,LabTests,MakeBooking,MyBookings,Payments
from views.views_dashboard import LabSignup,LabSignin,LabProfile,Addlabtests,ViewLabtests,ViewLabBookings,AddNurse,ViewNurse,TaskAllocation
from views.view_nurse import Nurse_Signin,NurseProfile, ChangePassword
api.add_resource(MemberSignup, '/api/member_signup')
api.add_resource(MemberSignin, '/api/member_signin')
api.add_resource(MemberProfile, '/api/member_profile')
api.add_resource(AddDependant, '/api/add_dependant')
api.add_resource(ViewDependants, '/api/view_dependant')
api.add_resource(Laboratories, '/api/labaratories')
api.add_resource(LabTests, '/api/lab_tests')
api.add_resource(MakeBooking, '/api/make_booking')
api.add_resource(MyBookings, '/api/my_bookings')
api.add_resource(Payments, '/api/payments')

api.add_resource(LabSignup, '/api/lab_signup')
api.add_resource(LabSignin, '/api/lab_signin')
api.add_resource(LabProfile, '/api/lab_profile')
api.add_resource(Addlabtests, '/api/add_labtests')
api.add_resource(ViewLabtests, '/api/view_labtests')
api.add_resource(ViewLabBookings, '/api/viewlab_bookings')
api.add_resource(AddNurse, '/api/add_nurse')
api.add_resource(ViewNurse, '/api/view_nurse')
api.add_resource(TaskAllocation, '/api/task_allocation')

api.add_resource(Nurse_Signin, '/api/nursesignin')
api.add_resource(NurseProfile, '/api/nurseprofile')
api.add_resource(ChangePassword, '/api/changepassword')
if __name__ =='__main__':
    app.run(debug=True)