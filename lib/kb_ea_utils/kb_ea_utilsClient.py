# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport
import time


class kb_ea_utils(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login',
            service_ver='release',
            async_job_check_time_ms=100, async_job_check_time_scale_percent=150, 
            async_job_check_max_time_ms=300000):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = service_ver
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc,
            async_job_check_time_ms=async_job_check_time_ms,
            async_job_check_time_scale_percent=async_job_check_time_scale_percent,
            async_job_check_max_time_ms=async_job_check_max_time_ms)

    def _check_job(self, job_id):
        return self._client._check_job('kb_ea_utils', job_id)

    def _get_fastq_ea_utils_stats_submit(self, input_params, context=None):
        return self._client._submit_job(
             'kb_ea_utils.get_fastq_ea_utils_stats', [input_params],
             self._service_ver, context)

    def get_fastq_ea_utils_stats(self, input_params, context=None):
        """
        This function should be used for getting statistics on read library object types 
        The results are returned as a string.
        :param input_params: instance of type
           "get_fastq_ea_utils_stats_params" (This module has methods to  get
           fastq statistics workspace_name    - the name of the workspace for
           input/output read_library_name - the name of 
           KBaseFile.SingleEndLibrary or KBaseFile.PairedEndLibrary) ->
           structure: parameter "workspace_name" of String, parameter
           "read_library_name" of String
        :returns: instance of String
        """
        job_id = self._get_fastq_ea_utils_stats_submit(input_params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _run_app_fastq_ea_utils_stats_submit(self, input_params, context=None):
        return self._client._submit_job(
             'kb_ea_utils.run_app_fastq_ea_utils_stats', [input_params],
             self._service_ver, context)

    def run_app_fastq_ea_utils_stats(self, input_params, context=None):
        """
        This function should be used for getting statistics on read library object type.
        The results are returned as a report type object.
        :param input_params: instance of type
           "run_app_fastq_ea_utils_stats_params" -> structure: parameter
           "workspace_name" of String, parameter "read_library_name" of String
        :returns: instance of type "Report" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        job_id = self._run_app_fastq_ea_utils_stats_submit(input_params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _get_ea_utils_stats_submit(self, input_params, context=None):
        return self._client._submit_job(
             'kb_ea_utils.get_ea_utils_stats', [input_params],
             self._service_ver, context)

    def get_ea_utils_stats(self, input_params, context=None):
        """
        This function should be used for getting statistics on fastq files. Input is string of file path.
        Output is a report string.
        :param input_params: instance of type "ea_utils_params"
           (read_library_path : absolute path of fastq files) -> structure:
           parameter "read_library_path" of String
        :returns: instance of String
        """
        job_id = self._get_ea_utils_stats_submit(input_params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _calculate_fastq_stats_submit(self, input_params, context=None):
        return self._client._submit_job(
             'kb_ea_utils.calculate_fastq_stats', [input_params],
             self._service_ver, context)

    def calculate_fastq_stats(self, input_params, context=None):
        """
        This function should be used for getting statistics on fastq files. Input is string of file path.
        Output is a data structure with different fields.
        :param input_params: instance of type "ea_utils_params"
           (read_library_path : absolute path of fastq files) -> structure:
           parameter "read_library_path" of String
        :returns: instance of type "ea_report" (read_count - the number of
           reads in the this dataset total_bases - the total number of bases
           for all the the reads in this library. gc_content - the GC content
           of the reads. read_length_mean - The average read length size
           read_length_stdev - The standard deviation read lengths phred_type
           - The scale of phred scores number_of_duplicates - The number of
           reads that are duplicates qual_min - min quality scores qual_max -
           max quality scores qual_mean - mean quality scores qual_stdev -
           stdev of quality scores base_percentages - The per base percentage
           breakdown) -> structure: parameter "read_count" of Long, parameter
           "total_bases" of Long, parameter "gc_content" of Double, parameter
           "read_length_mean" of Double, parameter "read_length_stdev" of
           Double, parameter "phred_type" of String, parameter
           "number_of_duplicates" of Long, parameter "qual_min" of Double,
           parameter "qual_max" of Double, parameter "qual_mean" of Double,
           parameter "qual_stdev" of Double, parameter "base_percentages" of
           mapping from String to Double
        """
        job_id = self._calculate_fastq_stats_submit(input_params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def status(self, context=None):
        job_id = self._client._submit_job('kb_ea_utils.status', 
            [], self._service_ver, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]
