# How to compress images with django
 ## Steps:
 1. Get form data
 Assume you have a django view:


def add_post(request):
	context = RequestContext(request)
	post_data=newadd(request.POST,request.FILES)
	if request.method=='POST':
    data={}
    ###then pass your classes here


#Class to get form data
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
	  #Here i get files passed on the data
		files={}
		files['image1']=request_files.POST.get('image1')
		files['image2']=request_files.POST.get('image2')
		files['image3']= request_files.POST.get('image3')
		#the return the files
		return files


2. Compress the images to occupy less memory space

from PIL import Image
from class.models import model
class Compress():
	def run(data):
		form_data=data.get('form_data')
		#get images in dictionary passed in get_form class
		images= data.get('images')
		#pass im the model class
		images=model(**images)
		#get instance of image
		image1= images.image1
		#open the image
		image1= Image.open(image1)
		#save the image
		#you can delete the file using os.remove
		image1.save(image1, format="JPEG", quality=80)
		#Lets try with a secong image
		image2= images.image2
		image2= Image.open('image2')
		image2.save(image2, format="JPEG", quality=80)
		#save to database
		images.save()
