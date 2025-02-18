"""
module :- pip install jenkinsapi
use :- Used to directly interact with the jenkins from our local system using python script.
"""
import argparse
import logging
import sys
from jenkinsapi.jenkins import Jenkins

JENKINS_URL = "http://localhost:8080"
JENKINS_USER = "divya1804"
JENKINS_PASS = "Divya1804"

logger=logging.getLogger("my_logger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('mylog.log', 'w')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

console_handler=logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def get_all_jobs(jenkins_obj):
    """
    This function will give the available jobs name from the localhost:8080
    :param jenkins_obj:
    :return:
    """
    jobs = jenkins_obj.get_jobs()
    job_list = [job[0] for job in jobs]
    logger.info("List of available jobs:")
    # logger.info("-------------------------")
    for job in job_list:
        logger.info(job)
    logger.info('\n')

def change_job_name(jenkins_obj, name, job_new_name):
    """
    This function will perform rename operation for the given job_name and convert it to the new job name.
    :param jenkins_obj:
    :param name:
    :param job_new_name:
    :return:
    """
    jenkins_obj.rename_job(name, job_new_name)
    logger.info(f"Name changed from {name} to {job_new_name}")
    logger.info('\n')

def get_no_builds(jenkins_obj, name):
    """
    This function will print the number of builds that we did for the particular job.
    :param name:
    :param jenkins_obj:
    :return:
    """
    logger.info("=================================================")
    job = jenkins_obj.get_job(name)
    job_builds = list(job.get_build_ids())
    no_builds = len(job_builds)
    logger.info(f"\tNumber of available builds = {no_builds}")
    logger.info("=================================================")
    logger.info('\n')

def get_last_build_details(jenkins_obj:Jenkins, job_name):
    """
    This function will print the data about the last build of the job.
    :param jenkins_obj:
    :return:
    """
    logger.info("=============================================================================")
    job = jenkins_obj.get_job(job_name)
    job_last_build = job.get_last_build()
    logger.info(f"{job_last_build.get_timestamp().strftime('%d-%m-%Y %H:%M:%S')}, {job_last_build.get_build_url()}, 'build no:-', {job_last_build.buildno}")
    logger.info("=============================================================================")
    logger.info('\n')

if __name__ == "__main__":
    try:
        jenkins = Jenkins(JENKINS_URL, JENKINS_USER, JENKINS_PASS)

        arg_obj = argparse.ArgumentParser()
        arg_obj.add_argument("--job", type=str, required=True)
        args = arg_obj.parse_args()

        job_name = args.job

        get_all_jobs(jenkins)
        get_no_builds(jenkins, job_name)

        # To change the name of the job from old_name to new_name.
        # change_job_name(jenkins, "Run_Serial_Simulator", "Run_Serial_Simulator")

        get_all_jobs(jenkins)
        get_last_build_details(jenkins, job_name)
    except ConnectionError as e:
        logger.debug(f"Error :- {e}")
