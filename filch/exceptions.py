# The MIT License (MIT)
#
# Copyright (c) 2017 Ryan Brady <ryan@ryanbrady.org>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from filch import constants


class MissingConfigurationSectionException(Exception):
    """Missing section from filch configuration file."""

    def __init__(self, section):
        self.section = section
        message = ('Missing section from filch configuration '
                   'file: %s' % self.section)
        super(MissingConfigurationSectionException, self).__init__(message)


class MissingConfigurationSettingException(Exception):
    """Missing setting from filch configuration file."""

    def __init__(self, setting):
        self.setting = setting
        message = ('Missing setting from filch configuration '
                   'file: %s' % self.setting)
        super(MissingConfigurationSettingException, self).__init__(message)


class UnsupportedLabelColorException(Exception):
    """Invalid label color."""

    def __init__(self, color):
        self.color = color
        self.colors = constants.SUPPORTED_LABEL_COLORS
        message = ('%s is an invalid color selection.  Please use one of the'
                   ' supported colors: %s' % (self.color, self.colors))
        super(UnsupportedLabelColorException, self).__init__(message)

class APIException(Exception):
    """An execption occurs in Trello's API or an unhandled status code is returned."""

    def __init__(self, code, reason, text):
        self.code = code
        self.reason = reason
        self.text = text

        message = ('A call to the Trello API has returned a %s code, for "%s", with "%s"' % (self.code, self.reason,
                                                                                             self.text))
        super(APIException, self).__init__(message)
