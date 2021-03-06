from django.http import JsonResponse
from django.views import View
from comment.models import Comment
from utils.error_code import ErrorCode


class CommentView(View):
	"""评论"""

	def post(self, request):
		is_login = request.session.get('is_login', None)
		if not is_login:  # 如果没有登录
			return JsonResponse({'error': ErrorCode.USERNOLOGIN})
		user_id = request.session.get('user_id', None)
		content = request.POST.get('content', None)
		article_id = request.POST.get('article_id', None)
		comment_id = request.POST.get('comment_id', None)  # 可以为空,为空时返回''
		response = Comment.check_create(user_id, content, article_id, comment_id)
		return response
