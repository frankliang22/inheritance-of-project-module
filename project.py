from openerp.osv import osv,fields
from datetime import datetime, date
import time

class Project(osv.Model):
	_inherit = "project.project"
	#_name = "my_project"

	def _responsible_id (self, cr, uid, ids, field_names, arg, context=None):
		result = {}
		str3=''
		responsible=''
		for i in self.browse(cr, uid, ids, context=context):
			str1 = str(i.po_id.name)
			str2 = str(i.user_id.name)
			str4 = str(i.project_status)
			responsible=''
			if str4 == "Pre-award":
				responsible = str1 
			else:
				responsible = str2
			str3 = str(responsible)
		result [i.id] = str3
		return result

	def _set_equal_field (self, cr, uid, ids, field_names, arg, context=None):
		result = {}
		for i in self.browse(cr, uid, ids, context=context):
			i.x_stage = i.stage
			string = str(i.x_stage.name)
		result [i.id] = str(string)
		return result

	def _customer_duration (self, cr, uid, ids, field_names, arg, context=None):
		result = {}
		for i in self.browse(cr, uid, ids, context=context):
			if i.x_target_mp and i.x_expected_award_date:
				end = datetime.strptime(i.x_target_mp,'%Y-%m-%d')
				start = datetime.strptime(i.x_expected_award_date,'%Y-%m-%d')
				end_year = int(end.strftime("%Y"))
				start_year = int(start.strftime("%Y"))
				if end.strftime("%B") == "January":
					end_month = 1
				elif end.strftime("%B") == "February":
					end_month = 2
				elif end.strftime("%B") == "March":
					end_month = 3
				elif end.strftime("%B") == "April":
					end_month = 4
				elif end.strftime("%B") == "May":
					end_month = 5
				elif end.strftime("%B") == "June":
					end_month = 6
				elif end.strftime("%B") == "July":
					end_month = 7
				elif end.strftime("%B") == "August":
					end_month = 8
				elif end.strftime("%B") == "September":
					end_month = 9
				elif end.strftime("%B") == "October":
					end_month = 10
				elif end.strftime("%B") == "November":
					end_month = 11
				elif end.strftime("%B") == "December":
					end_month = 12
				if start.strftime("%B") == "January":
					start_month = 1
				elif start.strftime("%B") == "February":
					start_month = 2
				elif start.strftime("%B") == "March":
					start_month = 3
				elif start.strftime("%B") == "April":
					start_month = 4
				elif start.strftime("%B") == "May":
					start_month = 5
				elif start.strftime("%B") == "June":
					start_month = 6
				elif start.strftime("%B") == "July":
					start_month = 7
				elif start.strftime("%B") == "August":
					start_month = 8
				elif start.strftime("%B") == "September":
					start_month = 9
				elif start.strftime("%B") == "October":
					start_month = 10
				elif start.strftime("%B") == "November":
					start_month = 11
				elif start.strftime("%B") == "December":
					start_month = 12
				duration = (end_year - start_year)*12 + (end_month - start_month)
				final_duration = str(duration) + " months"
			else:
				duration = ''
				final_duration = str(duration)
		result [i.id] = str(final_duration)
		return result

	def _actual_duration (self, cr, uid, ids, field_names, arg, context=None):
		result = {}
		for i in self.browse(cr, uid, ids, context=context):
			if i.x_mp_current and i.x_actual_award_date:
				end = datetime.strptime(i.x_mp_current,'%Y-%m-%d')
				start = datetime.strptime(i.x_actual_award_date,'%Y-%m-%d')
				end_year = int(end.strftime("%Y"))
				start_year = int(start.strftime("%Y"))
				if end.strftime("%B") == "January":
					end_month = 1
				elif end.strftime("%B") == "February":
					end_month = 2
				elif end.strftime("%B") == "March":
					end_month = 3
				elif end.strftime("%B") == "April":
					end_month = 4
				elif end.strftime("%B") == "May":
					end_month = 5
				elif end.strftime("%B") == "June":
					end_month = 6
				elif end.strftime("%B") == "July":
					end_month = 7
				elif end.strftime("%B") == "August":
					end_month = 8
				elif end.strftime("%B") == "September":
					end_month = 9
				elif end.strftime("%B") == "October":
					end_month = 10
				elif end.strftime("%B") == "November":
					end_month = 11
				elif end.strftime("%B") == "December":
					end_month = 12
				if start.strftime("%B") == "January":
					start_month = 1
				elif start.strftime("%B") == "February":
					start_month = 2
				elif start.strftime("%B") == "March":
					start_month = 3
				elif start.strftime("%B") == "April":
					start_month = 4
				elif start.strftime("%B") == "May":
					start_month = 5
				elif start.strftime("%B") == "June":
					start_month = 6
				elif start.strftime("%B") == "July":
					start_month = 7
				elif start.strftime("%B") == "August":
					start_month = 8
				elif start.strftime("%B") == "September":
					start_month = 9
				elif start.strftime("%B") == "October":
					start_month = 10
				elif start.strftime("%B") == "November":
					start_month = 11
				elif start.strftime("%B") == "December":
					start_month = 12
				duration = (end_year - start_year)*12 + (end_month - start_month)
				final_duration = str(duration) + " months"
			else:
				duration = ''
				final_duration = str(duration)
		result [i.id] = str(final_duration)
		return result

	def _set_equal_field (self, cr, uid, ids, field_names, arg, context=None):
		result = {}
		for i in self.browse(cr, uid, ids, context=context):
			i.x_stage = i.stage
			string = str(i.x_stage.name)
		result [i.id] = str(string)
		return result

	def _calc_revenue(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		for i in self.browse(cr,uid,ids,context=context):
			res[i.id] = i.x_target_price*i.x_quantity
		return res


	_columns = {
		'x_project_number': fields.char(string="Project Number", required=True, size=250),
		'po_id' : fields.many2one('res.users','PPO'),
		'responsible_id' : fields.function(_responsible_id,string='Person Responsible for Project', type = 'char'),
		'x_type': fields.selection([('System','System'),('Driver','Driver')], 'Type', required=True,),
		'x_business_type' : fields.selection([('TA','Traditional Audio'),('CA','Consumer Audio'),('PA','Pro Audio'),('RM','Roadmap')],'Business Type', required=False,),
		'x_process_type': fields.selection([('A','A'),('B','B'),('C','C'),],'Process Type'),
		'x_SAP': fields.char(string="SAP Number", size=250),
		'x_redmine': fields.char(string="Redmine Link", size=1000),
		'x_hold': fields.boolean(string="On Hold"),
		'x_projoect_description': fields.char(string="Project Description", size=250),
		'x_notes': fields.char(string="Notes", size=10000),
		'x_customer_duration' : fields.function(_customer_duration, string='Customer Duration',type='char'),
		'x_actual_duration' : fields.function(_actual_duration, string='Actual Duration',type='char'),
		'x_engineering_estimate' : fields.float(string="Engineering Estimate",digits=(16,2),required=False),
		'x_project_lifecycle': fields.float(string="Project Lifecycle"), 
		'x_target_mp': fields.date(string="Target MP Date", required=True,),
		'x_expected_award_date': fields.date(string="Expected Award Date", required=True,),

		#stage gates
		'x_stage' : fields.function(_set_equal_field, string="x_stage",type='char'),
		'stage': fields.many2one('res.states', ondelete='set null', string="Stage", required=True, select=True),
		'milestone': fields.related('stage','milestone', readonly=True, type='char',relation='res.states', string='Milestone'),
		'phase': fields.related('stage','phase', readonly=True, type='char',relation='res.states', string='Phase'),
		'project_status': fields.related('stage','project_status', readonly=True, type='char', string='Project Status'),

		#dates field
		'x_enquiry_date': fields.date(string="Enquiry Date", required=True,),
		'x_prd_initial_date': fields.date(string="PRD Initiation Date"),
		'x_prd_complete': fields.date(string="PRD Complete Date"),
		'x_expected_award_date': fields.date(string="Expected Award Date", required=True,),
		'x_actual_award_date': fields.date(string="Actual Award Date"),
		'x_checklist_complete': fields.date(string="Checklist Complete Date"),
		'x_target_mp': fields.date(string="Target MP Date", required=True,),
		'x_ship_date': fields.date(string="Ship Date"),
		'x_design_phase_schedule': fields.date(string="Design Phase Schedule"),
		'x_design_phase_current': fields.date(string="Design Phase Current"),
		'x_dvr_schedule': fields.date(string="DV Schedule"),
		'x_dvr_current': fields.date(string="DV Current"),
		'x_pp_schedule': fields.date(string="PP Schedule"),
		'x_pp_current': fields.date(string="PP Current"),
		'x_mp_schedule': fields.date(string="MP Schedule"),
		'x_mp_current': fields.date(string="MP Current"),

		#float field
		'x_duration': fields.float(string="Duration (Months)"),

		#function field
		'x_stage' : fields.function(_set_equal_field ,string="x_stage",type='char'),

		#load fields
		'x_pjm_load': fields.float(string="PJM Load", required=True,),
		'x_lead_se_load': fields.float(string="LSE Load", required=True,),
		'x_se_load': fields.float(string="SE Load", required=True,),
		'x_lead_system_me_load': fields.float(string="Lead System ME Load", required=True,),
		'x_system_me_load': fields.float(string="System ME Load", required=True,),
		'x_lead_ee_load': fields.float(string="Lead EE Load", required=True,),
		'x_ee_load': fields.float(string="EE Load", required=True,),
		'x_ee_tech_load': fields.float(string="EE Technician Load", required=True,),
		'x_lead_swe_load': fields.float(string="Lead Software Engineer Load", required=True,),
		'x_swe_load': fields.float(string="Software Engineer Load", required=True,),
		'x_lead_swe_test_load': fields.float(string="Lead Software Test Load", required=True,),
		'x_swe_test_load': fields.float(string="Software Test Load", required=True,),
		'x_lead_technical_engineer_load': fields.float(string="Lead TE Load", required=True,),
		'x_technical_engineer_load': fields.float(string="TE Load", required=True,),
		'x_te_me_load': fields.float(string="TE ME Load", required=True,),
		'x_ppo_load': fields.float(string="PPO Load", required=True,),
		'x_ppe_load': fields.float(string="PPE Load", required=True,),
		'x_lead_pt_load': fields.float(string="Lead PT Load", required=True,),
		'x_pt_load': fields.float(string="PT Load", required=True,),
		'x_qe_load': fields.float(string="QE Load", required=True,),

		#pricing fields
		'x_quote_status': fields.selection([
			('open','Open'),
			('hold','On-hold'),
			('closed','Closed')
			], 
			'Quote Status', required=True),
		'x_sales_feedback': fields.selection([('open','Open'),('closed','Closed')], 'Sales Feedback'),
		'x_quantity': fields.integer(string="Annual Quantity", required=True,),
		'x_target_price': fields.float(string="Target Price", required=True,),
		'x_revenue': fields.function(_calc_revenue, string="Revenue", type="float", store=True,),
		'x_project_winning_percentage': fields.integer(string="Winning Percentage", required=True,),
		'x_cancel_reason': fields.selection([
			('tym','Tymphany Rejected'), 
			('refer','Project Refered to Primax'),
			('cust','Customer does not want it for marketing'),
			('other','Other')
			], 
			'Cancel Reason'),
		'x_lost_reason': fields.selection([
			('cost','Cost too high'),
			('sched','Schedule too long'),
			('trans','Customer turn into transducer project only'),
			('perf','Performance can not reach customer requirement'),
			('other','Other')
			], 
			'Lost Reason'),
		'x_remark': fields.char(string="Remarks", size=10000),
		'x_rfq_receive_date': fields.date(string="RFQ Receive Date", ),
		'x_cr_approved_date': fields.date(string="CR Approval Date"),
		'x_lost_date': fields.date(string="Lost Date"),
		'x_on_hold_date': fields.date(string="On Hold Date"),
	}

class Task(osv.Model):
	
	_inherit = "project.task"
	#_name = "new_project.task"
	def _calc_difference_me (self, cr, uid, ids, field_names, arg, context=None):
		result = {}
		now= date.today().strftime('%Y-%m-%d')
		difference='0'
		for i in self.browse(cr, uid, ids, context=context):
			
			if i.x_expected_me_bom_release and i.x_actual_me_bom_release:
				start = datetime.strptime(i.x_actual_me_bom_release, '%Y-%m-%d')
				end = datetime.strptime(i.x_expected_me_bom_release, '%Y-%m-%d')
				duration = end-start
				if end==start:
					difference='0'
				else:
					difference = str(duration)
					difference = difference.replace(":","")
					difference = difference.replace(",","")
					difference = difference.replace("day","")
					difference = difference.replace("s","")
					difference = difference.rstrip("0")
				result [i.id] = int(difference)
			elif i.x_expected_me_bom_release:
				start = datetime.strptime(now, '%Y-%m-%d')
				end = datetime.strptime(i.x_expected_me_bom_release, '%Y-%m-%d')
				duration = end-start
				if end==start:
					difference='0'
				else:
					difference = str(duration)
					difference = difference.replace(":","")
					difference = difference.replace(",","")
					difference = difference.replace("day","")
					difference = difference.replace("s","")
					difference = difference.rstrip("0")
				result [i.id] = int(difference)		
			else:
				result [i.id] = ''
		return result

	def _calc_difference_te (self, cr, uid, ids, field_names, arg, context=None):
		result = {}
		now= date.today().strftime('%Y-%m-%d')
		difference='0'
		for i in self.browse(cr, uid, ids, context=context):
			
			if i.x_expected_te_bom_release and i.x_actual_te_bom_release:
				start = datetime.strptime(i.x_actual_te_bom_release, '%Y-%m-%d')
				end = datetime.strptime(i.x_expected_te_bom_release, '%Y-%m-%d')
				duration = end-start
				if end==start:
					difference='0'
				else:
					difference = str(duration)
					difference = difference.replace(":","")
					difference = difference.replace(",","")
					difference = difference.replace("day","")
					difference = difference.replace("s","")
					difference = difference.rstrip("0")
				result [i.id] = int(difference)
			elif i.x_expected_te_bom_release:
				start = datetime.strptime(now, '%Y-%m-%d')
				end = datetime.strptime(i.x_expected_te_bom_release, '%Y-%m-%d')
				duration = end-start
				if end==start:
					difference='0'
				else:
					difference = str(duration)
					difference = difference.replace(":","")
					difference = difference.replace(",","")
					difference = difference.replace("day","")
					difference = difference.replace("s","")
					difference = difference.rstrip("0")
				result [i.id] = int(difference)

			else:
				result [i.id] = ''
		return result


	def _calc_difference_se (self, cr, uid, ids, field_names, arg, context=None):
		result = {}
		now= date.today().strftime('%Y-%m-%d')
		difference='0'
		for i in self.browse(cr, uid, ids, context=context):
			
			if i.x_expected_se_bom_release and i.x_actual_se_bom_release:
				start = datetime.strptime(i.x_actual_se_bom_release, '%Y-%m-%d')
				end = datetime.strptime(i.x_expected_se_bom_release, '%Y-%m-%d')
				duration = end-start
				if end==start:
					difference='0'
				else:
					difference = str(duration)
					difference = difference.replace(":","")
					difference = difference.replace(",","")
					difference = difference.replace("day","")
					difference = difference.replace("s","")
					difference = difference.rstrip("0")
				result [i.id] = int(difference)
			elif i.x_expected_se_bom_release:
					start = datetime.strptime(now, '%Y-%m-%d')
					end = datetime.strptime(i.x_expected_se_bom_release, '%Y-%m-%d')
					duration = end-start
					if end==start:
						difference='0'
					else:
						difference = str(duration)
						difference = difference.replace(":","")
						difference = difference.replace(",","")
						difference = difference.replace("day","")
						difference = difference.replace("s","")
						difference = difference.rstrip("0")
					result [i.id] = int(difference)
			else:
				result [i.id] = ''
		return result


	def _calc_difference_ee (self, cr, uid, ids, field_names, arg, context=None):
		result = {}
		now= date.today().strftime('%Y-%m-%d')
		difference='0'
		for i in self.browse(cr, uid, ids, context=context):
			
			if i.x_expected_ee_bom_release and i.x_actual_ee_bom_release:
				start = datetime.strptime(i.x_actual_ee_bom_release, '%Y-%m-%d')
				end = datetime.strptime(i.x_expected_ee_bom_release, '%Y-%m-%d')
				duration = end-start
				if end==start:
					difference='0'
				else:
					difference = str(duration)
					difference = difference.replace(":","")
					difference = difference.replace(",","")
					difference = difference.replace("day","")
					difference = difference.replace("s","")
					difference = difference.rstrip("0")
				result [i.id] = int(difference)
			elif i.x_expected_ee_bom_release:
					start = datetime.strptime(now, '%Y-%m-%d')
					end = datetime.strptime(i.x_expected_ee_bom_release, '%Y-%m-%d')
					duration = end-start
					if end==start:
						difference='0'
					else:
						difference = str(duration)
						difference = difference.replace(":","")
						difference = difference.replace(",","")
						difference = difference.replace("day","")
						difference = difference.replace("s","")
						difference = difference.rstrip("0")
					result [i.id] = int(difference)
			else:
				result [i.id] = ''
		return result

	def _calc_difference_b (self, cr, uid, ids, field_names, arg, context=None):
		result = {}
		now= date.today().strftime('%Y-%m-%d')
		difference='0'
		for i in self.browse(cr, uid, ids, context=context):
			
			if i.x_expected_bbom_review and i.x_actual_bbom_review:
				start = datetime.strptime(i.x_actual_bbom_review, '%Y-%m-%d')
				end = datetime.strptime(i.x_expected_bbom_review, '%Y-%m-%d')
				duration = end-start
				if end==start:
					difference='0'
				else:
					difference = str(duration)
					difference = difference.replace(":","")
					difference = difference.replace(",","")
					difference = difference.replace("day","")
					difference = difference.replace("s","")
					difference = difference.rstrip("0")
				result [i.id] = int(difference)
			elif i.x_expected_bbom_review:
					start = datetime.strptime(now, '%Y-%m-%d')
					end = datetime.strptime(i.x_expected_bbom_review, '%Y-%m-%d')
					duration = end-start
					if end==start:
						difference='0'
					else:
						difference = str(duration)
						difference = difference.replace(":","")
						difference = difference.replace(",","")
						difference = difference.replace("day","")
						difference = difference.replace("s","")
						difference = difference.rstrip("0")
					result [i.id] = int(difference)
			else:
				result [i.id] = ''
		return result
	
	def _calc_difference_c (self, cr, uid, ids, field_names, arg, context=None):
		result = {}
		now= date.today().strftime('%Y-%m-%d')
		difference='0'
		for i in self.browse(cr, uid, ids, context=context):
			
			if i.x_expected_cbom_release and i.x_actual_cbom_release:
				start = datetime.strptime(i.x_actual_cbom_release, '%Y-%m-%d')
				end = datetime.strptime(i.x_expected_cbom_release, '%Y-%m-%d')
				duration = end-start
				if end==start:
					difference='0'
				else:
					difference = str(duration)
					difference = difference.replace(":","")
					difference = difference.replace(",","")
					difference = difference.replace("day","")
					difference = difference.replace("s","")
					difference = difference.rstrip("0")
				result [i.id] = int(difference)
			elif i.x_expected_cbom_release:
					start = datetime.strptime(now, '%Y-%m-%d')
					end = datetime.strptime(i.x_expected_cbom_release, '%Y-%m-%d')
					duration = end-start
					if end==start:
						difference='0'
					else:
						difference = str(duration)
						difference = difference.replace(":","")
						difference = difference.replace(",","")
						difference = difference.replace("day","")
						difference = difference.replace("s","")
						difference = difference.rstrip("0")
					result [i.id] = int(difference)
			else:
				result [i.id] = ''
		return result

	def _calc_difference_e (self, cr, uid, ids, field_names, arg, context=None):
		result = {}
		now= date.today().strftime('%Y-%m-%d')
		difference='0'
		for i in self.browse(cr, uid, ids, context=context):
			
			if i.x_expected_ebom_review and i.x_actual_ebom_review:
				start = datetime.strptime(i.x_actual_ebom_review, '%Y-%m-%d')
				end = datetime.strptime(i.x_expected_ebom_review, '%Y-%m-%d')
				duration = end-start
				if end==start:
					difference='0'
				else:
					difference = str(duration)
					difference = difference.replace(":","")
					difference = difference.replace(",","")
					difference = difference.replace("day","")
					difference = difference.replace("s","")
					difference = difference.rstrip("0")
				result [i.id] = int(difference)

			elif i.x_expected_ebom_review:
					start = datetime.strptime(now, '%Y-%m-%d')
					end = datetime.strptime(i.x_expected_ebom_review, '%Y-%m-%d')
					duration = end-start
					if end==start:
						difference='0'
					else:
						difference = str(duration)
						difference = difference.replace(":","")
						difference = difference.replace(",","")
						difference = difference.replace("day","")
						difference = difference.replace("s","")
						difference = difference.rstrip("0")
					result [i.id] = int(difference)
			else:
				result [i.id] = ''
		return result

	def _calc_difference_v (self, cr, uid, ids, field_names, arg, context=None):
		result = {}
		now= date.today().strftime('%Y-%m-%d')
		difference='0'
		for i in self.browse(cr, uid, ids, context=context):
			
			if i.x_expected_vbom_release and i.x_actual_vbom_release:
				start = datetime.strptime(i.x_actual_vbom_release, '%Y-%m-%d')
				end = datetime.strptime(i.x_expected_vbom_release, '%Y-%m-%d')
				duration = end-start
				if end==start:
					difference='0'
				else:
					difference = str(duration)
					difference = difference.replace(":","")
					difference = difference.replace(",","")
					difference = difference.replace("day","")
					difference = difference.replace("s","")
					difference = difference.rstrip("0")
				result [i.id] = int(difference)

			elif i.x_expected_vbom_release:
					start = datetime.strptime(now, '%Y-%m-%d')
					end = datetime.strptime(i.x_expected_vbom_release, '%Y-%m-%d')
					duration = end-start
					if end==start:
						difference='0'
					else:
						difference = str(duration)
						difference = difference.replace(":","")
						difference = difference.replace(",","")
						difference = difference.replace("day","")
						difference = difference.replace("s","")
						difference = difference.rstrip("0")
					result [i.id] = int(difference)
			else:
				result [i.id] = ''
		return result

	def _calc_difference_sales (self, cr, uid, ids, field_names, arg, context=None):
		result = {}
		now= date.today().strftime('%Y-%m-%d')
		difference='0'
		for i in self.browse(cr, uid, ids, context=context):
			
			if i.x_expected_sales_feedback and i.x_actual_sales_feedback:
				start = datetime.strptime(i.x_actual_sales_feedback, '%Y-%m-%d')
				end = datetime.strptime(i.x_expected_sales_feedback, '%Y-%m-%d')
				duration = end-start
				if end==start:
					difference='0'
				else:
					difference = str(duration)
					difference = difference.replace(":","")
					difference = difference.replace(",","")
					difference = difference.replace("day","")
					difference = difference.replace("s","")
					difference = difference.rstrip("0")
				result [i.id] = int(difference)

			elif i.x_expected_sales_feedback:
					start = datetime.strptime(now, '%Y-%m-%d')
					end = datetime.strptime(i.x_expected_sales_feedback, '%Y-%m-%d')
					duration = end-start
					if end==start:
						difference='0'
					else:
						difference = str(duration)
						difference = difference.replace(":","")
						difference = difference.replace(",","")
						difference = difference.replace("day","")
						difference = difference.replace("s","")
						difference = difference.rstrip("0")
					result [i.id] = int(difference)
			else:
				result [i.id] = ''
		return result

	_columns = {
		'partner_id': fields.many2one('res.partner', 'Customer'),
		'user_id': fields.many2one('res.users', 'PPO', select=True, track_visibility='onchange'),
		'x_rfq_receive_date': fields.date(string="RFQ Receive Date"),
		'x_introduction_meeting_date': fields.date(string="Introduction Meeting Date"),
		'x_quote_sent_to_customer': fields.date(string="Quote Sent to Customer"),
		'x_quotation_stage' : fields.selection([('1st','1st'),
			('2nd','2nd'),
			('3rd','3rd'),
			('4th','4th'),
			('5th','5th'),
			('6th','6th'),
			('7th','7th'),
			('8th','8th'),
			('9th','9th'),
			('10th','10th')],'Quotation Stage'),
		'x_sales_person' : fields.many2one('res.users','Sales'),
		'x_begin_wait_for_sales' : fields.date('Begin to wait for sales date'),
		'project_id': fields.many2one('project.project', 'Project', ondelete='set null', select=True, track_visibility='onchange'),
		'x_ppe_person' : fields.many2one('res.users','PPE'),
		'x_study_meeting': fields.date(string="Study meeting"),
		'x_information_preparation_date': fields.date(string="Information Preparation Date"),
		'x_issue' : fields.selection([('open','Open'),
			('closed','Closed'),
			('open-W','Open-W'),
			('closed-W','Closed-W'),
			('onhold','On Hold')],'Issue(Open/Closed)'),
		'x_department' : fields.selection([('TYM Sourcing','TYM Sourcing'),
			('PMX Sourcing','PMX Sourcing'),
			('TE','TE'),
			('TE-BU','TE-BU'),
			('ME','ME'),
			('Sales','Sales'),
			('SE','SE'),
			('LSE','TPL'),
			('EE','EE'),
			('Team','Team'),
			('product pricing','Product Pricing'),
			('System PJM','System PJM'),
			('Transducer PJM','Transducer PJM'),
			('PE','PE'),
			('Customer_sales','Customer_sales'),
			('Customer_PJM','Customer_PJM')],'Department'),
		'x_estimate_response_date' : fields.date('Estimated Response Date'),

		#Pricing Dates
		'x_expected_me_bom_release': fields.date(string="Expected ME A-BOM Release"),
		'x_actual_me_bom_release': fields.date(string="Actual ME A-BOM Release"),
		'x_me_difference': fields.function(_calc_difference_me, string="ME-BOM Difference", type="integer"),
		
		'x_actual_te_bom_release': fields.date(string="Actual TE A-BOM Release"),
		'x_expected_te_bom_release': fields.date(string="Expected TE A-BOM Release"),
		'x_te_difference': fields.function(_calc_difference_te, string="TE-BOM Difference", type="integer"),
		
		'x_expected_se_bom_release': fields.date(string="Expected SE A-BOM Release"),
		'x_actual_se_bom_release': fields.date(string="Actual SE A-BOM Release"),
		'x_se_difference': fields.function(_calc_difference_se, string="SE-BOM Difference", type="integer"),
		
		'x_expected_ee_bom_release': fields.date(string="Expected EE A-BOM Release"),
		'x_actual_ee_bom_release': fields.date(string="Actual EE A-BOM Release"),
		'x_ee_difference': fields.function(_calc_difference_ee, string="EE-BOM Difference", type="integer"),
		
		'x_expected_bbom_review': fields.date(string="Expected B-BOM Review"),
		'x_actual_bbom_review': fields.date(string="Actual B-BOM Review"),
		'x_b_difference': fields.function(_calc_difference_b, string="B-BOM Difference", type="integer"),

		'x_expected_cbom_release': fields.date(string="Expected C-BOM Release"),
		'x_actual_cbom_release': fields.date(string="Actual C-BOM Release"),
		'x_c_difference': fields.function(_calc_difference_c, string="C-BOM Difference", type="integer"),

		'x_expected_ebom_review': fields.date(string="Expected E-BOM Review"),
		'x_actual_ebom_review': fields.date(string="Actual E-BOM Review"),
		'x_e_difference': fields.function(_calc_difference_e, string="E-BOM Difference", type="integer"),

		'x_expected_vbom_release': fields.date(string="Expected V-BOM Release"),
		'x_actual_vbom_release': fields.date(string="Actual V-BOM Release"),
		'x_v_difference': fields.function(_calc_difference_v, string="V-BOM Difference", type="integer"),
		
		'x_expected_sales_feedback': fields.date(string="Expected Sales Feedback"),
		'x_actual_sales_feedback': fields.date(string="Actual Sales Feedback"),
		'x_sales_difference': fields.function(_calc_difference_sales, string="Sales Difference", type="integer"),

		#Pricing Info
		'x_vbom_version': fields.float(string="V-BOM Version"),
		'x_final_price': fields.float(string="Final Price"),
		'x_eng_cost_act': fields.float(string='Engineering DevelopmentCost (Actual)'),
		'x_eng_cost_cust': fields.float(string='Engineering DevelopmentCost (Assume collect from Customer)'),
		'x_ROE': fields.float(string='ROE'),

		'x_quote_status': fields.text(string="Quote Status"),
		'x_sales_status': fields.text(string="Sales Status"),
		}

