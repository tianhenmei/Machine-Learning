#-*- coding:utf-8 -*-

import unicodecsv

enrollments_filename = 'https://classroom.udacity.com/datasets/ud170/udacity-students/enrollments.csv'
# enrollments = []
# f = open(enrollments_filename,'rb')
# reader = unicodecsv.DictReader(f)
# for row in reader:
# 	enrollments.append(row)
# f.close()

def read_csv(pathh):
	with open(enrollments_filename,'rb') as f:
		reader = unicodecsv.DictReader(f)
		return list(reader)

engagement_filename = 'https://classroom.udacity.com/datasets/ud170/udacity-students/daily_engagement.csv'
submissions_filename = 'https://classroom.udacity.com/datasets/ud170/udacity-students/project_submissions.csv'

enrollments = read_csv(enrollments_filename)
daily_engagement = read_csv(engagement_filename) 
project_submissions = read_csv(submissions_filename)  