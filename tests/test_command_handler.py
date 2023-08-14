from icstatprofiler.unreal_plugin.StatsCollector.Content.Python.command_handler import WebSocketCommandHandler


class TestCommandHandler:

    def test_connection_state_after_stopping_server(self):
        socket = WebSocketCommandHandler()
        socket.stop_server()
        socket.set_connection_state()
        assert socket.connection_closed == False


