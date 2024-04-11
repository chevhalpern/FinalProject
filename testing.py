import re
string = "<Student 3-Sdei Chemed-//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Medini_1.jpg/91px-Medini_1.jpg-https://en.wikipedia.org/wiki/Sdei_Chemed>"
# image = re.findall("Vilna Gaon=\".+?(?=\")", string)
image = re.findall("//upload.+?(?=-https)", string)
print(image)

# <Student 3-Sdei Chemed-//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Medini_1.jpg/91px-Medini_1.jpg-https://en.wikipedia.org/wiki/Sdei_Chemed>




<py-script src="app.py">
                    print("hello")
                    <!-- function generate() {
                       // obj = Gedolim.query.all()
                        // randomNumber = random.randint(0, len(obj) - 1)
                        // randomPhotoObject = obj[randomNumber]
                        // randomImage = re.findall("//upload.+?(?=-https)", str(randomPhotoObject)) -->
                        <!-- let image = document.getElementById("image");
                        image.src = "//upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Vilna_Gaon_authentic_portrait.JPG/87px-Vilna_Gaon_authentic_portrait.JPG"
                        // document.getElementById("btnID").style.display = "none"; --> -->
                    <!-- } -->
                </py-script>