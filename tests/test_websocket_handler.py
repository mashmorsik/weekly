from icstatprofiler.unreal_plugin.StatsCollector.Content.Python.websocket_handler import WebsocketHandler
import websocket


class TestWebsocketHandler:

    def test_websocket_send_progress(self):
        ws = WebsocketHandler.initiate_connection(WebsocketHandler(), url='http://localhost:5050/')
        WebsocketHandler.send_progress(WebsocketHandler(), 'All the way up')
        message_sent = ws.recv()
        assert message_sent == 'All the way up'

    def test_websocket_close_connection(self):
        ws = WebsocketHandler.initiate_connection(WebsocketHandler(), url='http://localhost:5050/')
        WebsocketHandler.close_connection(WebsocketHandler())
        assert ws.connected == False
