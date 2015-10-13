# -*- coding: utf-8 -*-

"""Stackalytics API module"""

import requests
from sys import stderr



class Dotable(dict):
    """
    Make the JSON dot accessor thingy!
    Credits: http://hayd.github.io/2013/dotable-dictionaries/
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
        """Remove param if the value is None"""

        return dict((key, value) for key, value in params.iteritems() if value)

    @staticmethod
    def _request_url(url, params):
        """Get the JSON"""

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
        """Contribution by Modules"""

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
        """Contribution by Companies"""

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
        """Contribution by Engineers"""

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
        """Activity log"""

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
        """Contribution summary"""

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
