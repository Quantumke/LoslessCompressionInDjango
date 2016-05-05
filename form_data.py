class FormData():
	def run(data):
		data['form_data']=FormData.get_form.request_data
		data['images']=FormData.get_images.request_files

	def get_form(request_data):
		#getting user input from django view
		#i.e if method==request.post: the pass data as an empty dictionary
		form_data={}
		form_data['title']=request_data.POST.get('title')
		form_data['post_body']= request_data.POST.get('post_body')
		form_data['category']= request_data.POST.get('category')
		return form_data
	def get_images(request_files):
		files={}
		files['image1']=request_files.POST.get('image1')
		files['image2']=request_files.POST.get('image2')
		files['image3']= request_files.POST.get('image3')
		return files

