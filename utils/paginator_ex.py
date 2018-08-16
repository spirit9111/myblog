from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class JuncheePaginator(Paginator):
	"""分页拓展,默认左右当前页左右个5条"""

	def __init__(self, object_list, per_page, range_num=3, orphans=0, allow_empty_first_page=True):
		Paginator.__init__(self, object_list, per_page, orphans, allow_empty_first_page)
		self.range_num = range_num

	def page(self, number):
		self.page_num = number
		return super(JuncheePaginator, self).page(number)

	def _page_range_ext(self):
		num_count = 2 * self.range_num + 1
		if self.num_pages <= num_count:
			return range(1, self.num_pages + 1)
		num_list = []
		num_list.append(int(self.page_num))
		for i in range(1, self.range_num + 1):
			if int(self.page_num) - i <= 0:
				num_list.append(num_count + int(self.page_num) - i)
			else:
				num_list.append(int(self.page_num) - i)

			if int(self.page_num) + i <= self.num_pages:
				num_list.append(int(self.page_num) + i)
			else:
				num_list.append(int(self.page_num) + i - num_count)
		num_list.sort()
		return num_list

	page_range_ext = property(_page_range_ext)

	@staticmethod
	def paging(request, query_set):
		paginate_by = 5  # 每页显示n条
		if query_set:
			page = request.GET.get('page')
			paginator = JuncheePaginator(query_set, paginate_by)  # 显示3条数据
			try:
				page_obj = paginator.page(page)
			except PageNotAnInteger:  # None或者其他
				# 如果用户请求的页码号不是整数，显示第一页
				page_obj = paginator.page(1)
			except EmptyPage:
				# 如果用户请求的页码号超过了最大页码号，显示最后一页
				page_obj = paginator.page(paginator.num_pages)
			return page_obj
		return
