"""kytos/sample_ui."""
import logging

from kytos.core.apm import execution_context
from flask import jsonify
from kytos.core import KytosNApp, log, rest

log2 = logging.getLogger("kytos.napps.kytos/sample_ui")


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

    @rest("v1/core_log")
    def core_log(self):
        transaction = execution_context.get_transaction()
        if transaction:
            transaction.begin_span("log.debug", "custom")
        log.debug("core_log")
        if transaction:
            transaction.end_span()
        return jsonify()

    @rest("v1/log")
    def log(self):
        transaction = execution_context.get_transaction()
        if transaction:
            transaction.begin_span("log.debug", "custom")
        log2.debug("core_log")
        if transaction:
            transaction.end_span()
        return jsonify()
