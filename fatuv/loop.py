from _fatuv import ffi, lib

uv_default_loop = lib.fatuv_default_loop

uv_loop_new     = lib.fatuv_loop_new
uv_loop_delete  = lib.fatuv_loop_delete
uv_loop_init    = lib.fatuv_loop_init
uv_loop_close   = lib.fatuv_loop_close

uv_run          = lib.fatuv_run

__all__ = [
	'UV_RUN_DEFAULT', 'UV_RUN_ONCE', 'UV_RUN_NOWAIT',
	'Loop',
]

UV_RUN_DEFAULT  = lib.FATUV_RUN_DEFAULT
UV_RUN_ONCE     = lib.FATUV_RUN_ONCE
UV_RUN_NOWAIT   = lib.FATUV_RUN_NOWAIT

class Loop(object):
	@staticmethod
	def default_loop():
		return Loop(uv_default_loop())

	def __init__(self, handle=None):
		self.handle = handle or uv_loop_new()
		uv_loop_init(self.handle)

	def run(self, mode=UV_RUN_DEFAULT):
		assert self.handle
		uv_run(self.handle, mode)

	def close(self):
		assert self.handle
		uv_loop_close(self.handle)
		uv_loop_delete(self.handle)
		self.handle = None

