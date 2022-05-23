# SPDX-License-Identifier: GPL-3.0-or-later


class ProxyInfo(object):
    def __init__(self, proxy, port, scheme="http", username="", password=""):
        """ Retrieves a new ProxyInfo object

        :param str proxy:       Name or IP of the Proxy server.
        :param int port:        The port of the proxy server.
        :param str scheme:      The type of proxy (http is default).
        :param str username:    The username to use (if empty or omitted no authentication is done.
        :param str password:    The password to use.

        """

        self.Proxy = proxy
        self.Port = int(port)
        self.Scheme = scheme
        self.Username = username
        self.Password = password
        self.Filter = []            # : If specified, only URLs that contain these parts will be routed via the proxy.

    def get_proxy_address(self, hide_password=False):
        """ Returns the proxy address for this proxy

        :param bool hide_password:    Should we show or hide the password.

        :return: The proxy address for this proxy.
        :rtype: str

        """

        if self.Scheme.lower() == "dns":
            return f"{self.Scheme}://{self.Proxy}"

        elif self.__is_secure():
            if hide_password:
                return f"{self.Scheme}://{self.Username}:*******@{self.Proxy}:{self.Port}"
            else:
                return f"{self.Scheme}://{self.Username}:{self.Password}@{self.Proxy}:{self.Port}"

        else:
            return f"{self.Scheme}://{self.Proxy}:{self.Port}"

    def use_proxy_for_url(self, url):
        """ Checks whether the URL is allowed based on the proxy filter.

        :param str url:     The URL

        :return: True if the given URL should use this proxy object.
        :rtype: bool

        """

        return any(f in url for f in self.Filter) if self.Filter else True

    def __is_secure(self):
        """ An easy way of determining if this server should use proxy authentication.

        :return: Boolean indicating of proxy authentication should be used.
        :rtype: bool

        """

        return self.Username != ""

    def __str__(self):
        """ String representation

        :return: The String representation
        :rtype: str

        """

        if self.Proxy == "":
            return "Proxy Default Override."

        return f"Proxy ({self.Scheme}): {self.get_proxy_address(True)}"
