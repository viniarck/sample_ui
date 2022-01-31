"""kytos/sample_ui."""

from kytos.core import KytosNApp, log


class Main(KytosNApp):
    """Main class to be used by Kytos controller."""

    def setup(self):
        """Replace the 'init' method for the KytosApp subclass.

        The setup method is automatically called by the run method.
        Users shouldn't call this method directly.
        """
        log.info("sample_ui napp loaded")

    def execute(self):
        """Run once on NApp 'start' or in a loop.

        The execute method is called by the run method of KytosNApp class.
        Users shouldn't call this method directly.
        """
        pass

    def shutdown(self):
        """Shutdown routine of the NApp."""
        pass
