 convert +append -background white -gravity center Surface1.png Surface1_spectra.png -resize x800 Surface1_image.png
 convert +append -background white -gravity center Surface2.png Surface2_spectra.png -resize x800 Surface2_image.png
 convert +append -background white -gravity center Surface3.png Surface3_spectra.png -resize x800 Surface3_image.png
 convert +append -background white -gravity center Surface4.png Surface4_spectra.png -resize x800 Surface4_image.png
 convert -append Surface1_image.png Surface2_image.png Surface3_image.png Surface4_image.png Surfaces.png
