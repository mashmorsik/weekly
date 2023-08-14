import pytest

from icstatprofiler.unreal_plugin.StatsCollector.Content.Python.init_unreal import PipelinePythonBridgeImplementation


def test_execute_command():
    command = 'stat_profiler'
    result = PipelinePythonBridgeImplementation.spawn_icstatprofiler()
    assert PipelinePythonBridgeImplementation.execute_command(command) == result

