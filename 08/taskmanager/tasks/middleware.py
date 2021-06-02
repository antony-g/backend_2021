class LoginMiddleware(object):
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		return self.get_response(request)

	def process_view(self, request, view_func, view_args, view_kwargs):
		if is_authenticated(request, view_func):
			return None
		return redirect_to_login()
