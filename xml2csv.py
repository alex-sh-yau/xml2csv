# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 11:11:31 2019

@author: Alex
"""

from lxml import etree
import csv

def get_value(target_tree, xpath):
    try:
        return target_tree.xpath(xpath)[0].text
    except IndexError:
        return ""

def get_attrib(target_tree, xpath):
    try:
        return target_tree.xpath(xpath)[0].attrib
    except IndexError:
        return ""

tree = etree.parse("C:\\Users\\Alex\\Desktop\\Repository\\honeybee-python\\xml2csv\\SearchResults.xml")

header = ["Study", "nct_id", "Title", "Acronym", "Status", "Study_results",
          "Conditions", "Interventions", "Outcome_measures", "Lead_sponsor", 
          "Collaborators", "Gender", "Min_age", "Max_age", "Age_groups", "Phases", 
          "Enrollment", "Funded_by", "Study_types", "exp_acc_types", "Study_designs",
          "Other_ids", "Start_date", "Primary_completion_date", "Completion_date", 
          "Study_first_posted", "Last_update_posted", "Locations", "Documents", "URL"]

with open("xml_output.csv", "w", encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",", lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(header)

    for study in tree.xpath("//study"):
        get_outcome_measure = ""
        for outcome_measures in study.findall("outcome_measures/outcome_measure"):
            get_outcome_measure += outcome_measures.text + "; "
            
        get_collaborator = ""
        for sponsor in study.findall("sponsors"):
            for collaborator in sponsor.findall("collaborator"):
                get_collaborator += collaborator.text + "; "
                
        get_study_design = ""
        for study_designs in study.findall("study_designs/study_design"):
            get_study_design += study_designs.text + "; "
            
        get_location = ""
        for locations in study.findall("locations/location"):
            get_location += locations.text + "; "

        csvwriter.writerow([study.attrib, 
                            get_value(study, "nct_id"),
                            get_value(study, "title"),
                            get_value(study, "acronym"),
                            get_value(study, "status"),
                            get_value(study, "study_results"),
                            get_value(study, "conditions/condition"),
                            get_value(study, "interventions/intervention"),
#                            get_value(study, "outcome_measures"),
                            get_outcome_measure,
                            get_value(study, "sponsors/lead_sponsor"),
#                            get_value(study, "sponsors/collaborator"),
                            get_collaborator,
                            get_value(study, "gender"),
                            get_value(study, "min_age"),
                            get_value(study, "max_age"),
                            get_value(study, "age_groups/age_group"),
                            get_value(study, "phases/phase"),
                            get_value(study, "enrollment"),
                            get_value(study, "funded_bys/funded_by"),
                            get_value(study, "study_types"),
                            get_value(study, "exp_acc_types"),
#                            get_value(study, "study_designs/study_design"),
                            get_study_design,
                            get_value(study, "other_ids/other_id"),
                            get_value(study, "start_date"),
                            get_value(study, "primary_completion_date"),
                            get_value(study, "completion_date"),
                            get_value(study, "study_first_posted"),
                            get_value(study, "last_update_posted"),
#                            get_value(study, "locations/location"),
                            get_location,
                            get_value(study, "documents"),
                            get_value(study, "url")
                            ])
