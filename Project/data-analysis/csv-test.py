#-*- coding:utf-8 -*-

import unicodecsv
import json
from datetime import datetime

# enrollments_filename = './enrollments.json'
# enrollments = []
# f = open(enrollments_filename,'rb')
# reader = unicodecsv.DictReader(f)
# for row in reader:
# 	enrollments.append(row)
# f.close()

def read_csv(path,callback):
	with open(path,'rb') as f:
		reader = json.loads(f.read())
		return callback(reader["list"])
		# reader = unicodecsv.DictReader(f)
		# return list(reader)

def parse_date(date):
	if date == '':
		return None
	else:
		return datetime.strptime(date,"%Y-%m-%d")

def parse_int(num):
	if num == '':
		return None
	else:
		return int(float(num))

def parse_float(num):
	if num == '':
		return None
	else:
		return float(num)

def parse_enrollments(data_list):
	for one in data_list:
		one['is_udacity'] = one['is_udacity'] == 'True'
		one['is_canceled'] = one['is_canceled'] == 'True'
		one['join_date'] = parse_date(one['join_date'])
		one['account_key'] = parse_int(one['account_key'])
		one['days_to_cancel'] = parse_int(one['days_to_cancel'])
		one['cancel_date'] = parse_date(one['cancel_date'])
	return data_list

def parse_daily(data_list):
	for one in data_list:
		one['lessons_completed'] = parse_int(one['lessons_completed'])
		one['num_courses_visited'] = parse_int(one['num_courses_visited'])
		one['total_minutes_visited'] = parse_float(one['total_minutes_visited'])
		one['projects_completed'] = parse_int(one['projects_completed'])
		one['account_key'] = parse_int(one['acct'])
		one['utc_date'] = parse_date(one['utc_date'])
		del one['acct']
	return data_list

def parse_project(data_list):
	for one in data_list:
		one['lesson_key'] = parse_int(one['lesson_key'])
		one['account_key'] = parse_int(one['account_key'])
		one['creation_date'] = parse_date(one['creation_date'])
		one['completion_date'] = parse_date(one['completion_date'])
	return data_list

enrollments_filename = './enrollments.json'
daily_filename = './daily_engagement.json'
project_filename = './project_submissions.json'

enrollments = read_csv(enrollments_filename,parse_enrollments)
daily_engagement = read_csv(daily_filename,parse_daily) 
project_submissions = read_csv(project_filename,parse_project)

print enrollments[0]
print daily_engagement[0]
print project_submissions[0]

unique_enrollments = set()
for i in enrollments:
	unique_enrollments.add(i['account_key'])

unique_engagement = set()
for i in daily_engagement:
	unique_engagement.add(i['account_key'])

unique_project_submissions = set()
for i in project_submissions:
	unique_project_submissions.add(i['account_key'])

print len(enrollments) , len(unique_enrollments)
print len(daily_engagement) , len(unique_engagement)
print len(project_submissions) , len(unique_project_submissions)

count = 0
for i in enrollments:
	if i['account_key'] not in unique_engagement and i['join_date'] != i['cancel_date']:
		count += 1
		print i

print 'Exception Data: {}'.format(count)

udacity_data = set()
for i in enrollments:
	if i['is_udacity']:
		udacity_data.add(i['account_key'])

def remove_udacity_data(data_list):
	not_udacity_data = []
	for i in data_list:
		if i['account_key'] not in udacity_data:
			not_udacity_data.append(i)

	return not_udacity_data

non_udacity_enrollments = remove_udacity_data(enrollments)
non_udacity_engagement = remove_udacity_data(daily_engagement)
non_udacity_project_submissions = remove_udacity_data(project_submissions)

print len(non_udacity_enrollments)
print len(non_udacity_engagement)
print len(non_udacity_project_submissions)


paid_students = set()
for i in non_udacity_enrollments:
	if not i['is_canceled'] or i['days_to_cancel'] > 7:
		paid_students.add(i['account_key'])

print 'Paid Students: {}'.format(len(paid_students))

def remove_free_trail_cancels(data_list):
	new_data = []
	for i in data_list:
		if i['account_key'] in paid_students:
			new_data.append(i)

	return new_data

paid_enrollments = remove_free_trail_cancels(non_udacity_enrollments)
paid_engagement = remove_free_trail_cancels(non_udacity_engagement)
paid_submissions = remove_free_trail_cancels(non_udacity_project_submissions)


paid_engagment_in_first_week = set()
non_udacity_submissions = remove_udacity_data(project_submissions)

print len(non_udacity_enrollments)
print len(non_udacity_engagement)
print len(non_udacity_submissions)

paid_students = set()
paid_enrollments = []
for i in non_udacity_enrollments:
	if not i['is_canceled'] or i['days_to_cancel'] > 7:
		paid_students.add(i['account_key'])
		paid_enrollments.append(i)

print 'Paid students: {}'.format(len(paid_students))

def within_one_week(data):
	if data['join_date']:
		pass









