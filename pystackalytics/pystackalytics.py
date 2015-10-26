# -*- coding: utf-8 -*-

"""Stackalytics API module

This module is a wrapper to Stackalytics API maintained by Mirantis Inc.

.. _Stackalytics JSON API v1.0:
    http://stackalytics.readthedocs.org/en/latest/userdoc/api_v1.0.html

"""

import requests
from sys import stderr



class Dotable(dict):
    """Make the JSON dot accessor object

    Takes any json-like object and returns an object whose dictionary part
    can be accessed with dot notation

    .. _Credits:
        http://hayd.github.io/2013/dotable-dictionaries/

    """

    __getattr__ = dict.__getitem__

    def __init__(self, data):
        super(Dotable, self).__init__()
        self.update(**dict((key, self.parse(value))
                           for key, value in data.iteritems()))

    @classmethod
    def parse(cls, value):
        if isinstance(value, dict):
            return cls(value)
        elif isinstance(value, list):
            return [cls.parse(i) for i in value]
        else:
            return value



class Stackalytics(object):
    """Stackalytics API Class"""

    def __init__(self):
        self.base_url = 'http://stackalytics.com'

    @staticmethod
    def _build_params(params):
        """Build valid parameters

        Remove a parameter from the dict if the value is None.

        Args:
            params(dict): A dictionary of API parameters

        Returns:
            dict: A dictionary of parameters sans the keys with values None

        """

        return dict((key, value) for key, value in params.iteritems() if value)

    @staticmethod
    def _request_url(url, params):
        """Get the JSON object

        Get the JSON response for the API endpoint requested.

        Args:
            url(str): URL for the API endpoint
            params(dict): API parameters to be passed along with the request

        Returns:
            dict: Decoded JSON object from the response

        """

        r = requests.get(url=url, params=params)
        try:
            r.raise_for_status()
            response = r.json()
        except requests.exceptions.HTTPError as error:
            print >> stderr, 'HTTPError:', error.message
        except ValueError as error:
            print >> stderr, 'Unexpected content! Wrong parameters may be ' \
                             'to blame:', error.message
        return response

    def modules(self,
                release=None,
                project_type=None,
                module=None,
                company=None,
                user_id=None,
                metric=None,
                start_date=None,
                end_date=None):
        """Contribution by Modules

        Stats on contribution per modules. The data contains list of modules
        with their metric. Modules which metric is 0 are omitted.

        Args:
            release(Optional[str]): Name of OpenStack release or ‘all’,
                by default current release
            project_type(Optional[str]): Type of project, by default ‘openstack’
            module(Optional[str]): Name of module (repository name)
            company(Optional[str]): Company name
            user_id(Optional[str]): Launchpad id of user or email if no
            Launchpad id is mapped.
            metric(Optional[str]): Metric: e.g. ‘commits’, ‘loc’, ‘marks’,
                ‘emails’
            start_date(Optional[Unix time]): When the period starts
            end_date(Optional[Unix time]): When the period ends

        Returns:
            Dotable object: Dictionary accessible using dot notation

        """

        parameters = self._build_params({'release': release,
                                         'project_type': project_type,
                                         'module': module,
                                         'company': company,
                                         'user_id': user_id,
                                         'metric': metric,
                                         'start_date': start_date,
                                         'end_date': end_date})

        url = '{base_url}/api/1.0/stats/modules'.format(base_url=self.base_url)
        return Dotable.parse(self._request_url(url=url, params=parameters))

    def companies(self,
                  release=None,
                  project_type=None,
                  module=None,
                  company=None,
                  user_id=None,
                  metric=None,
                  start_date=None,
                  end_date=None):
        """Contribution by Companies

        Stats on contribution per companies. The data contains list of
        companies with their metric. Companies which metric is 0 are omitted.

        Args:
            release(Optional[str]): Name of OpenStack release or ‘all’,
                by default current release
            project_type(Optional[str]): Type of project, by default ‘openstack’
            module(Optional[str]): Name of module (repository name)
            company(Optional[str]): Company name
            user_id(Optional[str]): Launchpad id of user or email if no
            Launchpad id is mapped.
            metric(Optional[str]): Metric: e.g. ‘commits’, ‘loc’, ‘marks’,
                ‘emails’
            start_date(Optional[Unix time]): When the period starts
            end_date(Optional[Unix time]): When the period ends

        Returns:
            Dotable object: Dictionary accessible using dot notation

        """

        parameters = self._build_params({'release': release,
                                         'project_type': project_type,
                                         'module': module,
                                         'company': company,
                                         'user_id': user_id,
                                         'metric': metric,
                                         'start_date': start_date,
                                         'end_date': end_date})

        url = '{base_url}/api/1.0/stats/companies'.format(
            base_url=self.base_url)
        return Dotable.parse(self._request_url(url=url, params=parameters))

    def engineers(self,
                  release=None,
                  project_type=None,
                  module=None,
                  company=None,
                  user_id=None,
                  metric=None,
                  start_date=None,
                  end_date=None):
        """Contribution by Engineers

        Stats on contribution per engineers. The data contains list of
        engineers with their metric. Engineers who has metric 0 are omitted.
        For reviews also added column with review distribution.

        Args:
            release(Optional[str]): Name of OpenStack release or ‘all’,
                by default current release
            project_type(Optional[str]): Type of project, by default ‘openstack’
            module(Optional[str]): Name of module (repository name)
            company(Optional[str]): Company name
            user_id(Optional[str]): Launchpad id of user or email if no
            Launchpad id is mapped.
            metric(Optional[str]): Metric: e.g. ‘commits’, ‘loc’, ‘marks’,
                ‘emails’
            start_date(Optional[Unix time]): When the period starts
            end_date(Optional[Unix time]): When the period ends

        Returns:
            Dotable object: Dictionary accessible using dot notation

        """

        parameters = self._build_params({'release': release,
                                         'project_type': project_type,
                                         'module': module,
                                         'company': company,
                                         'user_id': user_id,
                                         'metric': metric,
                                         'start_date': start_date,
                                         'end_date': end_date})

        url = '{base_url}/api/1.0/stats/engineers'.format(
            base_url=self.base_url)
        return Dotable.parse(self._request_url(url=url, params=parameters))

    def activity(self,
                 release=None,
                 project_type=None,
                 module=None,
                 company=None,
                 user_id=None,
                 metric=None,
                 start_date=None,
                 end_date=None):
        """Activity log

        Depending on selected metric Activity log contains commits, reviews,
        emails or blueprints.

        When querying the activity log, the page_size and start_record
        parameters can be used to manage the paging of results
        (splitting results over multiple requests/responses).
        The default value of page_size is 10.

        Args:
            release(Optional[str]): Name of OpenStack release or ‘all’,
                by default current release
            project_type(Optional[str]): Type of project, by default ‘openstack’
            module(Optional[str]): Name of module (repository name)
            company(Optional[str]): Company name
            user_id(Optional[str]): Launchpad id of user or email if no
            Launchpad id is mapped.
            metric(Optional[str]): Metric: e.g. ‘commits’, ‘loc’, ‘marks’,
                ‘emails’
            start_date(Optional[Unix time]): When the period starts
            end_date(Optional[Unix time]): When the period ends

        Returns:
            Dotable object: Dictionary accessible using dot notation

        """

        parameters = self._build_params({'release': release,
                                         'project_type': project_type,
                                         'module': module,
                                         'company': company,
                                         'user_id': user_id,
                                         'metric': metric,
                                         'start_date': start_date,
                                         'end_date': end_date})

        url = '{base_url}/api/1.0/activity'.format(base_url=self.base_url)
        return Dotable.parse(self._request_url(url=url, params=parameters))

    def contribution(self,
                     release=None,
                     project_type=None,
                     module=None,
                     company=None,
                     user_id=None,
                     metric=None,
                     start_date=None,
                     end_date=None):
        """Contribution summary

        Get contribution summary: number of commits, locs, emails,
        drafted and completed blueprints, review marks with distribution
        per mark (-2..+2).

        Args:
            release(Optional[str]): Name of OpenStack release or ‘all’,
                by default current release
            project_type(Optional[str]): Type of project, by default ‘openstack’
            module(Optional[str]): Name of module (repository name)
            company(Optional[str]): Company name
            user_id(Optional[str]): Launchpad id of user or email if no
            Launchpad id is mapped.
            metric(Optional[str]): Metric: e.g. ‘commits’, ‘loc’, ‘marks’,
                ‘emails’
            start_date(Optional[Unix time]): When the period starts
            end_date(Optional[Unix time]): When the period ends

        Returns:
            Dotable object: Dictionary accessible using dot notation

        """

        parameters = self._build_params({'release': release,
                                         'project_type': project_type,
                                         'module': module,
                                         'company': company,
                                         'user_id': user_id,
                                         'metric': metric,
                                         'start_date': start_date,
                                         'end_date': end_date})

        url = '{base_url}/api/1.0/contribution'.format(base_url=self.base_url)
        return Dotable.parse(self._request_url(url=url, params=parameters))
