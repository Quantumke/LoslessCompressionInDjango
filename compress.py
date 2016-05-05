from PIL import Image
class Compress():
	def run(data):
		form_data=data.get('form_data')
		#get images in dictionary passed in get_form class
		images= data.get('images')
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
