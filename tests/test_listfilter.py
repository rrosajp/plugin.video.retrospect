import unittest

from tests.channel_tests.channeltest import ChannelTest


class TestListFilter(ChannelTest):
    # noinspection PyPep8Naming
    def __init__(self, methodName):  # NOSONAR
        super(TestListFilter, self).__init__(methodName, "channel.nos.nos2010", "uzgjson")

    def test_channel_exists(self):
        self.assertIsNotNone(self.channel)

    def test_no_filter(self):
        from resources.lib.addonsettings import AddonSettings
        from resources.lib.addonsettings import KODI
        AddonSettings.store(KODI).set_setting("geo_region", 0)
        AddonSettings.store(KODI).set_setting("hide_types", 0)

        items = self.__get_items()
        self.assertGreaterEqual(len(items), 2)

    def test_paid_filter_toggle(self):
        from resources.lib.addonsettings import AddonSettings
        from resources.lib.addonsettings import KODI

        AddonSettings.store(KODI).set_setting("hide_premium", "false")
        self.assertFalse(AddonSettings.store(KODI).get_boolean_setting("hide_premium"))
        AddonSettings.store(KODI).set_setting("hide_premium", "true")
        self.assertTrue(AddonSettings.store(KODI).get_boolean_setting("hide_premium"))

    def test_filter_list_paid(self):
        from resources.lib.addonsettings import AddonSettings
        from resources.lib.addonsettings import KODI
        AddonSettings.store(KODI).set_setting("geo_region", 1)
        AddonSettings.store(KODI).set_setting("hide_types", 0)

        items = self.__get_items()
        self.assertGreaterEqual(len(items), 1)

    def tearDown(self):
        "Hook method for deconstructing the test fixture after testing it."
        from resources.lib.addonsettings import AddonSettings
        from resources.lib.addonsettings import KODI

        AddonSettings.store(KODI).set_setting("geo_region", 0)
        AddonSettings.store(KODI).set_setting("hide_types", 1)
        AddonSettings.store(KODI).set_setting("hide_premium", "false")

    def __get_items(self):
        return self._test_folder_url(
            "https://start-api.npo.nl/media/series/KN_1689408/episodes?pageSize=500",
            expected_results=1,
            headers={"apikey": "07896f1ee72645f68bc75581d7f00d54"},
            retry=0,
        )
