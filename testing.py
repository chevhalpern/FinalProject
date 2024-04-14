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









                <script>
                fun(){
                    print();
                }
            </script>
            <!-- <script>
                function generate()
                {
                    // function randomNum(){
                    //     let randomNum = Math.floor(Math.random * (array.length - 1));
                    //     return randomNum;
                    // }
                    function generateRandomImage(array){
                        let image = document.getElementById("image");
                        // number = randomNum();
                        image.setAttribute("src", array[0]);
                    };
                    const imageArray = [
                        "//upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Vilna_Gaon_authentic_portrait.JPG/87px-Vilna_Gaon_authentic_portrait.JPG",
                        "//upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Yitzchak_Zev_Soloveitchik.jpg/96px-Yitzchak_Zev_Soloveitchik.jpg",
                        "//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Medini_1.jpg/91px-Medini_1.jpg"
                    ];
                    // const button = document.getElementById("button");
                    // window.onload = () => generateRandomImage(imageArray);
                    // button.addEventListener("click", () => generateRandomImage(imageArray));
                    return generateRandomImage(imageArray);
                };
            </script> -->
            <!-- <script>
                function generate(){
                   const imageArray = [
                    "//upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Vilna_Gaon_authentic_portrait.JPG/87px-Vilna_Gaon_authentic_portrait.JPG",
                "//upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Yitzchak_Zev_Soloveitchik.jpg/96px-Yitzchak_Zev_Soloveitchik.jpg",
            "//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Medini_1.jpg/91px-Medini_1.jpg"];
            const image = document.getElementById("image");
            const button = document.getElementById("button");
            window.onload = () => generateRandomImage(imageArray);
            button.addEventListener("click", () => generateRandomImage(imageArray));

            function generateRandomImage(array){
                let randomNum = Math.floor(Math.random * array.length);
                image.setAttribute("src", array[randomNum])
                }
                }
            </script> -->

            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5TgD-NycF2Odr6Tc1YGzsXN_AF6-AsYM8dq0E7IqNkw&s"



            array = ["//upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Vilna_Gaon_authentic_portrait.JPG/87px-Vilna_Gaon_authentic_portrait.JPG",
                 "//upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Yitzchak_Zev_Soloveitchik.jpg/96px-Yitzchak_Zev_Soloveitchik.jpg",
                 "//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Medini_1.jpg/91px-Medini_1.jpg",
                 "//upload.wikimedia.org/wikipedia/commons/thumb/3/38/Shlomo_Ganzfried.jpg/86px-Shlomo_Ganzfried.jpg",
                 "//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Chaim_Yosef_David_Azulai.jpg/88px-Chaim_Yosef_David_Azulai.jpg",
                 "//upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Meir_Shapiro.jpg/83px-Meir_Shapiro.jpg",
                 "//upload.wikimedia.org/wikipedia/commons/thumb/6/62/Schneur_Zalman_of_Liadi.jpg/96px-Schneur_Zalman_of_Liadi.jpg",
                 "//upload.wikimedia.org/wikipedia/en/thumb/4/45/Steipler_Gaon.jpg/85px-Steipler_Gaon.jpg",
                 "//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Yitzchak_Elchanan_Spektor.jpg/85px-Yitzchak_Elchanan_Spektor.jpg",
                 "//upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Shmuel_Salant.jpg/84px-Shmuel_Salant.jpg",
                 "//upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Avraham_Mattisyahu_of_Shtefanesht.JPG/91px-Avraham_Mattisyahu_of_Shtefanesht.JPG",
                 "//upload.wikimedia.org/wikipedia/commons/thumb/1/19/Reb_Chaim_Ozer.jpg/92px-Reb_Chaim_Ozer.jpg",
                 "//upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Yisrael_Meir_Kagan.jpg/94px-Yisrael_Meir_Kagan.jpg",
                 "//upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Rabbi_Kalischer.jpg/108px-Rabbi_Kalischer.jpg",
                 "//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Gershon_Edelshtein.jpg/77px-Gershon_Edelshtein.jpg",
                 "//upload.wikimedia.org/wikipedia/commons/thumb/3/30/Reb_Moshe_Feinstein.jpg/120px-Reb_Moshe_Feinstein.jpg"
                 ]