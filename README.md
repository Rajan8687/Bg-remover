├── README.md
└── bgremover.py


/README.md:
--------------------------------------------------------------------------------
1 | # Bg-remover
2 | A simple yet powerful Python tool to automatically remove image backgrounds using deep learning. Ideal for product images, profile pictures, and content creation.
3 | 


--------------------------------------------------------------------------------
/bgremover.py:
--------------------------------------------------------------------------------
1 | from rembg import remove
2 | 
3 | from PIL import Image
4 | 
5 | input = Image.open("rajan.jpg")
6 | output = remove(input)
7 | output.save("rajancopy.png")


--------------------------------------------------------------------------------
