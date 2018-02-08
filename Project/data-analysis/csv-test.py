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

def read_csv(path):
	with open(path,'rb') as f:
		reader = json.loads(f.read())
		# return parse_list(reader["list"])
		return reader["list"]
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

def parse_list(data_list):
	for one in data_list:
		one['is_udacity'] = one['is_udacity'] == 'True'
		one['is_canceled'] = one['is_canceled'] == 'True'
		one['join_date'] = parse_date(one['join_date'])
		one['account_key'] = parse_int(one['account_key'])
		one['days_to_cancel'] = parse_int(one['days_to_cancel'])
		one['cancel_date'] = parse_date(one['cancel_date'])

	return data_list

enrollments_filename = './enrollments.json'
daily_filename = './daily_engagement.json'
project_filename = './project_submissions.json'

enrollments = read_csv(enrollments_filename)
daily_engagement = read_csv(daily_filename) 
project_submissions = read_csv(project_filename)

print enrollments[0]
print daily_engagement[0]
print project_submissions[0]




