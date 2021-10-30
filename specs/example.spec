Specification Heading
=====================

This is an executable specification file. This file follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

To execute this specification, run
	gauge specs

Ozdilekteyim
-----------
* "Özdilekteyim uygulaması açılır." yapılır
* "com.ozdilek.ozdilekteyim:id/tv_startShoppingStore" İd'li elemente tıkla
* "Alışverişe başla butonuna tıklanır." yapılır
* "2" saniye bekle
* "//android.widget.FrameLayout[@content-desc=\"Kategoriler\"]/android.widget.ImageView" xpath'li elemente tıkla
* "Kategori sayfasına tıklanır" yapılır
* "2" saniye bekle
* "//*[@resource-id=\"com.ozdilek.ozdilekteyim:id/relLayCategoriesItem\"][2]" xpath'li elemente tıkla
* "Menüden Kadın şeçilir" yapılır
* "2" saniye bekle
* "//*[@resource-id=\"com.ozdilek.ozdilekteyim:id/relLayCategoriesItem\"][4]" xpath'li elemente tıkla
* "Menüden Pantolon şeçilir" yapılır
* "3" saniye bekle
* x ="500" y="500" Scroll Yap
* x ="500" y="500" Scroll Yap
* "2 kere scroll yapılır" yapılır
* "2" saniye bekle
* "//*[@resource-id=\"com.ozdilek.ozdilekteyim:id/textView\"]" xpath'li elemente tıkla
* "Rasgele bir ürün seçilir" yapılır
* "2" saniye bekle
* "//*[@resource-id=\"com.ozdilek.ozdilekteyim:id/imgFav\"]" xpath'li elemente tıkla
* "Favoriler butonuna tıklanır" yapılır
* "3" saniye bekle
* "com.ozdilek.ozdilekteyim:id/etEposta" İd'li elemente "burakkurt72@gmail.com" değerini yaz
* "com.ozdilek.ozdilekteyim:id/etPassword" İd'li elemente "123142452" değerini yaz
* "Epost ve şifre girilir" yapılır
* "2" saniye bekle
* "com.ozdilek.ozdilekteyim:id/ivBack" İd'li elemente tıkla
* "Geri butonuna tıklanır" yapılır
* "2" saniye bekle
* "com.ozdilek.ozdilekteyim:id/ivBack" İd'li elemente tıkla
* "Geri butonuna tıklanır" yapılır
* "2" saniye bekle
* "//*[@resource-id=\"com.ozdilek.ozdilekteyim:id/textView\"]" xpath'li elemente tıkla
* "Rasgele bir ürün seçilir" yapılır
* "3" saniye bekle
* "com.ozdilek.ozdilekteyim:id/relLayAddCartBtn" İd'li elemente tıkla
* "Şeçilen ürün sepete eklenir" yapılır
* "2" saniye bekle