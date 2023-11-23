import random
import sys

class Flashcards:
    def __init__(self):
        self.cards = self.load_questions_and_answers()
        self.lessons = self.extract_lessons()
        random.shuffle(self.cards)

    def load_questions_and_answers(self):
        questions_and_answers = """
        Glikoliz|Glukoz, neden iyi bir yakıt olarak kabul edilir?|Hücrelerde enerji üretimi için
        Glikoliz|Nişasta ve glikojen gibi depo formların düşük sitozolik neyi sağlar?|düşük sitozolik osmolaritenin devamını sağlar. Bu depo formların uzun süreli enerji eldesi için kullanımı ne amaçla önemlidir?|Glukozun nişasta ve glikojen gibi depo formlarının olması düşük sitozolik osmolaritenin devamını sağlar. Bu sayede depo formlar uzun süreli ihtiyaçta enerji eldesi için kullanılabilir.
        Glikoliz|Glukozun E.Coli gibi bakterilerdeki rolü nedir|?metabolik ara ürünlerin karbon iskeletini oluşturabilir
        Glikoliz|Pentoz fosfat yolağının glikoliz ile ilişkisi nedir ve bu yolağın yükseltgenme reaksiyonları hangi biyosentetik işlevler için önemlidir?|Pentoz fosfat yolağı, glikoliz ile nasıl ilişkilidir ve bu yolağın yükseltgenme reaksiyonları, nükleik asitlerin yapısında bulunan riboz 5-fosfatı ve indirgen biyosentetik işlevler için NADPH’ı sağlamak amacıyla önemlidir.    
        Glikoliz|Kinazlar nedir?|Fosfat grubunu nükleofillere aktaran enzimlerdir.
        Glikoliz|Kinazlar hangi iyona ihtiyaç duyarlar?|Mg+2 ihtiyaç duyarlar.
        Glikoliz|Kinazlar hangi enzim grubuna aittir?|Transferazların alt grubudur.
        Glikoliz|Kinazların substratı hangi kompleks?|Substratı MgATP-2 kompleksidir.
        Glikoliz|MgATP-2 ne işe yarar?|ATP’nın fosforil grubunun negatif yükünü korur ve nükleofilik grup için kolay hedef haline getirir
        Glikoliz|Glikoliz nedir?|Glikozun enerji kaynağı olarak kullanımındaki ilk aşamadır.
        Glikoliz|Glikoliz hangi dokularda görünür?|Bütün dokularda
        Glikoliz|Glikoliz hangi ortamda gerçekleşebilir?|Aerob (oksijenli) ve anaerob(oksijensiz)
        Glikoliz|Glukoz piruvata kadar yıkılması nedir?|aerob glikoliz
        Glikoliz|piruvatin laktata yıkımı nedir?|anaerob glikolizdir.
        Glikoliz|Anaerob glikolize genel olarak fermentasyon denir?|fermentasyon
        Glikoliz|GlikolizEnzimlerle katalizlenen bir dizi parçalanme tepkimesidir.tepkimesidir.Salınan serbest enerji hangi şekilde korunur?|ATP ve NADH şeklinde.
        Glikoliz|Glikoliz sırasında salınan serbest enerji nasıl korunur ve hangi enerji taşıyıcıları oluşur?|Glikoliz sırasında salınan serbest enerji ATP ve NADH şeklinde korunur.
        Glikoliz|Glikolizin kaç evre kaç basamaktan oluşur?|İki evre 10 basamak. ilk beşi beşi hazırlık son beşi sonlanma evresi
        Glikoliz|Glikoliz Hazırlık evresinde hangi süreç gerçekleşir ve sonucunda ne oluşur?|glukoz fosforillenir ve gliseraldehit 3 fosfata dönüşür.
        Glikoliz|Glukoz ATP'den gelen bir fosfat grubunu alır ve hangi forma dönüşür?|Glukoz 6 Fosfat formuna dönüşür.
        Glikoliz|Hazırlık evresinde kaç ATP harcanır?|2 ATP harcanır.
        Glikoliz|Enerji kazancı hangi evrededir?|Sonlanma evresindedir
        Glikoliz|Hangi enzim tarafından katalizlenir?|HEKSOKİNAZ.
        Glikoliz|Glukoz fosfatlanması ne gerektirir?|enerji. Bu sebeple 1.Basamak Glikoz 6 Fosfat Oluşumunda enerji harcanır.
        Glikoliz|Glukozun fosfatlanmasındaki amaç nedir?|Hücre dışına çıkışını önlemektir.
        Glikoliz|2. basmak nedir?|Glukoz 6 Fosfatın Fruktoz 6 Fosfata Dönüşmesi
        Glikoliz|Aldoz yapıdaki glukoz neye dönüşür?|6-fosfat ketoz yapılı fruktoz 6-fosfata dönüşür
        Glikoliz|Aldoz yapıdaki glukoz 6-fosfat ketoz yapılı fruktoz 6-fosfata dönüşür.Bu dönüşüm  neyle katalizlenir?|bir izomeraz olan FOSFOHEKSOZ (FOSFOGLUKOZ) İZOMERAZ ile
        Glikoliz|2. Basamakta tepkime kaç yönde ilerler?|Tepkime kolayca ve iki yönde ilerler
        Glikoliz|2. basamaktan sonraki basamaklar için kritik olan şey nedir?|C1 ve C2’deki karbonil ve hidroksil gruplarının yeniden düzenlenmesi 
        Glikoliz|3. basamak nedir?|Fruktoz 6 Fosfatın Fruktoz 1,6-Bifosfata Fosforillenmesi
        Glikoliz|3. basamakta enerji harcanır mı?|Evet
        Glikoliz|3. basamakta ATP’den bir fosforil grubu fruktoz 6 fosfata aktarılır. bu tepkimeyi katalizleyen enzim nedir?|FOSFOFRUKTOKİNAZ-1(FFK-1)dir.
        Glikoliz|Fosforil grubunun aktarilması ile ne oluşur?|fruktoz 1,6-bifosfat oluşur.
        Glikoliz|4.Basamak nedir?|Fruktoz 1,6-Bifosfatın Bölünmesi
        Glikoliz|Fruktoz 1,6-bifosfat iki aldoza bölünür bu tepkimeye ne ad verilir?|ALDOL KONDENSASYON
        Glikoliz|FRUKTOZ 1,6-BİFOSFAT ALDOLAZ enzimi ile katalizlenir. Bu nasıl bir tepkimedir?|tersinir bir tepkimedir.
        Glikoliz|4. basamakta oluşan iki fosfat nelerdir?|Aldoz olan gliseraldehit 3 fosfat - Ketoz olan dihidroksiaseton fosfat
        Glikoliz|5.Basamak nedir?|Trioz Fosfatların Birbirine Dönüşümü
        Glikoliz|glikoliz tepkimelerinde doğrudan yıkılabilen tek şey nedir?|gliseraldehit 3-fosfat 
        Glikoliz|Dihidroksiaseton fosfat ise TRİOZ FOSFAT İZOMERAZ ile neye dönüştürülür?|gliseraldehit 3-fosfata dönüştürülür.
        Glikoliz|6.Basamak nedir?|Gliseraldehit 3- Fosfatın 1,3- Bifosfogliserata Yükseltgenmesi
        Glikoliz|Gliseraldehit 3-fosfat,  1,3- bifosfogliserata hangi enzimle yükseltgenir?|GLİSERALDEHİT 3-FOSFAT DEHİDROGENAZ
        Glikoliz|ATP oluşumu olan iki tepkimenin ilki nedir?|Gliseraldehit 3- Fosfatın 1,3- Bifosfogliserata Yükseltgenmesi
        Glikoliz|Gliseraldehit 3-fosfatın aldehit grubu fosforik asit ile neye yükseltgenir?|karboksilik asit anhidritine 
        Glikoliz|hidroliz için  yüksek serbest enerjiye sahip olan şey?|açil fosfat
        Glikoliz|Gliseraldehit 3-Fosfat Dehidrogenaz Tepkimesinde Aktif bölgede buluna Cys NAD+ bağlandığında ne olur?|bu yapı indirgen hale gelir ve reaktif bir tiyolat formu oluşur.
        Glikoliz|tiyohemiasetal köprüsü neler arasında oluşur?|sülfüdril grubu ile substrat arasında 
        Glikoliz|Enzim substrat kompeksi  ne tarafından oksitlenir?|NAD tarafından. Yüksek enerjili ara madde ile NADH+H oluşur.
        Glikoliz|NADH gevşek bağlı olduğunda neyle yer değiştirir?|NAD ile
        Glikoliz|Yüksek enerjili bağın anorganik fosfat ile yıkılması sonucu ne olur?|enzim ve 1,3bifosfagliserat serbestleşir.
        Glikoliz|7.Basamak nedir?|1,3- Bifosfogliserattan ADP’ye Fosforil Grubu Aktarımı 
        Glikoliz|ATP + 3-Fosfogliseraldehit ne zaman oluşur?|1,3- Bifosfogliseratın karboksil grubundaki yüksek enerjili fosforil grubu ADP’ye aktarıldığında oluşur.
        Glikoliz|Bifosfogliserattan ADP’ye Fosforil Grubu Aktarımı tepkimesi neyle katalizlenir?|FOSFOGLİSERAT KİNAZ 
        Glikoliz|8.Basamak nedir?|3-Fosfogliseratin 2-Fosfogliserata Dönüşümü,
        Glikoliz|Gliseratın C2 ve C3 arasında fosforil grubunun yer değişimi nasıl bir tepkimedir?|tersinirdir
        Glikoliz|Gliseratın C2 ve C3 arasında fosforil grubunun yer değişimi neyle katalizlenir?|FOSFOGLİSERAT MUTAZ ile
        Glikoliz|Gliseratın C2 ve C3 arasında fosforil grubunun yer değişimi tepkimesi hangi iyonu kullanır?|Mg+2
        Glikoliz|Subratın C3’den fosforil aktarımı neye doğrudur?|aktif bölgede bulunan birinci His’e doğrudur
        Glikoliz|Fosfogliserat Mutaz Tepkimesinde Fosforil aktarımı neyle neyin arasındadır?|aktif bölgede bulunan His ile subsratın C2’ ye bağlı hidroksil grubu arasındadır.
        Glikoliz|9.Basamaknedir?|2-Fosfogliseratın Fosfoenolpiruvata Dehidrasyonu
        Glikoliz|2-Fosfogliserattan 1 molekül H2O çıkışı ile ne oluşur?|Fosfoenolpiruvat oluşur.
        Glikoliz|2-Fosfogliserattan 1 molekül H2O çıkışı hangi enzimle katalizlenir?|ENOLAZ 
        Glikoliz|2-Fosfogliserattan 1 molekül H2O çıkışı ne içerir?|Mg+2  ile kararlı hale gelen bir ara ürün
        Glikoliz|2-Fosfogliseratın Fosfoenolpiruvata Dehidrasyonu sonucunda ne olur?|Düşük fosforil grubu aktarma potansiyeli olan bileşiği (2-Fosfogliserat)  daha yüksek fosforil grubu aktarma potansiyeli olan bir bileşiğe (Fosfoenolpiruvat) dönüştürür.
        Glikoliz|10.Basamak nedir?|Fosfoenolpiruvattan ADP’ye Fosforil Grubunun Aktarılması
        Glikoliz|Fosforil grubu fosfoenolpiruvatan ayrılır ve ADP’ye aktarılır bunu katalizleyen enzim  nedir?|K+ ve Mg+2 veya Mn+2 kullanan PİRUVAT KİNAZdır
        Glikoliz|Piruvat enol yapısından hızlı ve kendi kendine gelişen bir tautomerleşme ile neye dönüşür?|keto yapıdaki piruvata dönüşür.
        Glikoliz|pH 7 ‘de baskın form hangisidir?|Keto yapı
        Glikoliz|Net ATP Kazancı nedir?|Sonuç olarak 4 ATP üretilmiştir ancak bunun 2ATP’sı glikolizi başlatmak için glukozun aktivasyonunda kullanılır ve son olarak 2 ATP kazanılmış olur.
        Glikoliz|Fermantasyon nedir?|Glikozun anaerobik parçalanmasıdır.
        Glikoliz|Laktik asit fermantasyonu nasıl olur?|Laktata indirgenir.Oksijen yetersiz kaldığında kaslarda üretilir. oksijen olmazsa NADH yeniden NAD+ yükseltgenemez. Piruvat NADH’dan elektron alarak laktata indirgenir ve NAD+ yenilenmiş olur.Laktat Dehidrogenaz enzimi katalizler.
        Glikoliz|Etanol(alkol) fermantasyonu nasıl olur?|Piruvat etanol ve CO2’ye dönüştürülür.
        Glikoliz|Glikoliz Denetiminde hız nasıl denetlenir?|Hız kısıtlayıcı enzimlerin aktivitelerinin düzenlemesi ile denetlenir.
        Glikoliz|Enzim aktivitesinin maddeleri?|Allosterik efektör(düzenleyici), Hormonal etki sonucu kovalent modifikasyon(fosforilasyon ve defosforilasyon), Düzenleyici protein bağlanma mekanizmaları, Transkripsiyonel düzenleme
        Glikoliz|Hormonlar allosterik efektörlerin hücre içi konsantrasyonlarında da etkili midir?|Evet
        Glikoliz|Allosterik efektör ile aktivasyon-inhibisyonu, fosforilasyon ve defosforilasyonu ne kadar sürelidir?|kısa sürelidir.
        Glikoliz|Hekzokinaz - Glukokinaz nedir?|1. basamakta glikozun glikoz 6-fosfata dönüşümü bu enzimlerce sağlanır.Bu dönüşüm glikozu aktive ettiği için glikoliz başlayabilir.
        Glikoliz|Hangi enzimin düzenlenmesi glikolizin denetlenmesini sağlar?|Hekzokinaz - Glukokinaz 
        Glikoliz|Fosfofruktokinaz 1(PFK-1) nasıl düzenlenir?|Allosterik olarak 
        Glikoliz|Yüksek konsantrasyonda bulunan AMP,ADP ve fruktoz ne aktive eder?|2,3-bifosfat
        Glikoliz|Yüksek konsantrasyonda bulunan AMP,ADP ve fruktoz ne inhibite eder?|ATP ve sitrat 
        Glikoliz|Piruvat kinazın aktif formu?|defosforile hali
        Glikoliz|Piruvat kinazın deaktif formu?|fosforile hali
        Pentoz-Fosfat-Yolu|Pentoz fosfat yolu, glukoz metabolizmasında hangi iki ana fonksiyona sahiptir? | Pentoz fosfat yolu, NADPH oluşumu ve nükleotid/nükleik asit oluşumu için gerekli ribozun sentezi gibi başlıca iki ana fonksiyona sahiptir.
        Pentoz-Fosfat-Yolu|Pentoz fosfat yolu tarafından sentezlenen NADPH, hangi biyolojik süreçlerde kullanılır? | Sentez edilen NADPH, yağ asiti, steroid, kolesterol sentezi, ksenobiyotiklerin zehirsizleştirilme reaksiyonları, okside glutatyonun indirgenmesi, deoksiriboz oluşumu gibi süreçlerde kullanılır.
        Pentoz-Fosfat-Yolu|Hangi dokularda pentoz fosfat yolu daha etkin bir şekilde çalışır ve neden? | Pentoz fosfat yolu, özellikle NADPH gereksiniminin fazla olduğu dokularda daha etkin biçimde çalışır. Bu dokular arasında karaciğer, eritrositler, gonatlar, yağ dokusu bulunmaktadır.
        Pentoz-Fosfat-Yolu|Pentoz fosfat yolu reaksiyonları hangi hücre fraksiyonunda meydana gelir? | Pentoz fospat yolu reaksiyonları hücrenin sitozol fraksiyonunda meydana gelir.
        Pentoz-Fosfat-Yolu|Pentoz fospat yolu reaksiyonları kaç basamakta incelenebilir ve bunlar nelerdir? | Pentoz fospat yolu reaksiyonları 2 basamakta incelenebilir: Oksidatif reaksiyonlar ve non-oksidatif reaksiyonlar.
        Pentoz-Fosfat-Yolu|Glukoz-6 fosfat dehidrojenaz tarafından kataliz edilen reaksiyon nedir? | Bu reaksiyonda, glukoz-6 fosfatın birinci karbonundan 2 hidrojen atomu uzaklaştırılır. Oluşan karboksil grubu ile 5. karbondaki hidroksil grubu arasında esterleşme meydana gelir.
        Pentoz-Fosfat-Yolu|Glukonalakton-6 fosfat laktonaz enzimi tarafından kataliz edilen hidroliz reaksiyonu nedir? | Bu reaksiyonda, glukonalakton-6 fosfat molekülü hidroliz olur ve glikonat-6 fosfat molekülü oluşur.
        Pentoz-Fosfat-Yolu|Glukonat-6 fosfat dehidrogenaz kataliziyle ribüloz-5 fosfata ne dönüşür? | Glukonat-6 fosfat dehidrogenaz enzimi tarafından kataliz edilen bu reaksiyonda, glukonat-6 fosfat ribüloz-5 fosfata dönüşür.
        Pentoz-Fosfat-Yolu|Hangi reaksiyon yolun hız sınırlayıcı ve regüle edici aşamasıdır? | Glukoz-6 fosfat dehidrogenaz reaksiyonu, yolun hız sınırlayıcı ve regüle edici aşamasıdır. NADPH, bu enzimin güçlü bir inhibitörüdür.
        Pentoz-Fosfat-Yolu|Pentoz fosfat yolunun non-oksidatif reaksiyonları neleri kataliz eder?|Non-oksidatif reaksiyonlar, riboz-5-fosfat oluşumunu ve 3-7 karbonlu şekerlerin birbirlerine dönüşümlerini kataliz eder.
        Pentoz-Fosfat-Yolu|Non-oksidatif yolun reversible reaksiyonları ne tür glikoliz ara ürünlerinin oluşumunu sağlar?|Non-oksidatif yolun reversible reaksiyonları, glikoliz ara ürünlerinin (früktoz-6-fosfat, gliseraldehit-3-fosfat) oluşumunu sağlar.
        Pentoz-Fosfat-Yolu|Hücrenin ihtiyaçları non-oksidatif reaksiyonların hangi yöne olacağını belirler, bu doğru mu?|Evet, hücrenin ihtiyaçları non-oksidatif reaksiyonların hangi yöne olacağını belirler.
        Pentoz-Fosfat-Yolu|Nükleotid sentezi ihtiyacı olmayan bir hücrede, riboz-5-fosfat hangi yolla çevrilir?|Nükleotid sentezi ihtiyacı olmayan bir hücrede, oluşan riboz-5-fosfat non-oksidatif yol ile glikolitik ara ürünlere çevrilir.
        Pentoz-Fosfat-Yolu|Hücre NADPH'a ihtiyaç duyuyorsa, riboz-5-fosfat hangi yolla çevrilir?|Hücre NADPH'a ihtiyaç duyuyorsa, riboz-5-fosfat glikolitik ara ürünler üzerinden glikoz-6-fosfata dönüştürülür.
        Pentoz-Fosfat-Yolu|Hücrede nükleotid ihtiyacı yüksekse, glikolitik ara ürünler non-oksidatif yol ile nasıl kullanılır?|Hücrede nükleotid ihtiyacı yüksekse, glikolitik ara ürünler non-oksidatif yol ile 5-karbonlu şekerlerin üretimi için kullanılır.
        Pentoz-Fosfat-Yolu|Non-oksidatif yol içinde bulunan enzimler nelerdir? | İzomeraz, Epimeraz, Transketolaz, Transaldolaz.
        Pentoz-Fosfat-Yolu|Transketolaz'ın görevi nedir ve hangi kofaktörü kullanır?| Transketolaz, iki karbonlu birimlerin aktarılmasını sağlar ve kullanılan kofaktör tiamin pirofosfattır.
        Pentoz-Fosfat-Yolu|Transaldolaz ne işlevi yerine getirir?| Transaldolaz, üç karbonlu birimlerin aktarılmasını sağlar.
        Pentoz-Fosfat-Yolu|Oksidasyon basamakları sonucunda oluşan ribuloz, hangi enzimler için uygun substrat şekline dönüştürülür? | Bu amaçla epimeraz ve izomeraz enzimleri kullanılır.      
        Pentoz-Fosfat-Yolu|Glikoz-6-fosfatın pentoz fosfat yolunun oksidatif reaksiyonları ile riboz-5-fosfata dönüştürülmesi hangi durumda gerçekleşir? | Bu durum, hücrede NADPH ve riboz-5-fosfat ihtiyacının dengede olduğu durumlarda ortaya çıkar.
        Pentoz-Fosfat-Yolu|Hücrede NADPH ihtiyacı yüksek olduğunda ne tür reaksiyonlar gerçekleşir? | Hücre, pentoz fosfat yolunun oksidatif ve non-oksidatif yollarına ek olarak glikonejenez reaksiyonları ile NADPH gereksinimini karşılamak üzere yeniden glikoz-6-fosfat oluşturur.
        Pentoz-Fosfat-Yolu|Hücrede riboz-5-fosfat ihtiyacı yüksek olduğunda ne tür bir dönüşüm gerçekleşir? | Glikoz-6-fosfat büyük oranda glikoliz ile früktoz-6-fosfat ve gliser aldehit-3-fosfata dönüşür.
        Pentoz-Fosfat-Yolu|Riboz-5-fosfat sentezi hangi reaksiyonlar ile gerçekleştirilir? | Sonraki aşamada, transaldolaz ve transketolaz reaksiyonları ile riboz-5-fosfat sentezi gerçekleştirilir.
        Pentoz-Fosfat-Yolu|Hücrede NADPH ile birlikte ATP gerekiyorsa, oksidatif yol ile oluşan riboz-5-fosfat, früktoz-6-fosfat ve gliseraldehid-3-fosfat üzerinden glikolize girerek ATP üretimi nasıl gerçekleşir?|Oksidatif yol ile üretilen riboz-5-fosfat, früktoz-6-fosfat ve gliseraldehid-3-fosfat, glikoliz reaksiyonlarına katılarak NADPH ile birlikte ATP üretimini sağlar.
        Pentoz-Fosfat-Yolu|NADPH'nin biyolojik süreçlerdeki rolü nedir ve hangi reaksiyonlarda kullanılır?|NADPH, redüktif biyosentez reaksiyonlarında kullanılır. Örneğin; kolestrol, yağ asidi, steroid hormon sentezi gibi süreçlerde rol oynar.
        Pentoz-Fosfat-Yolu|Hidrojen peroksitin (H2O2) oluşumuyla ilgili olarak NADPH'nin önemi nedir?|Hidrojen peroksit, reaktif oksijen türlerinin bir üyesidir ve NADPH, bu tür zararlı moleküllerin oluşumunu engelleyerek aerobik metabolizmalarda hücrelerin korunmasına katkıda bulunur.
        Pentoz-Fosfat-Yolu|Hidrojen peroksitin zararlı etkilerini önlemek için hücreler nasıl bir koruyucu mekanizma geliştirmiştir?|Hücreler, hidrojen peroksitin zararlı etkilerini önlemek için glutatyon gibi koruyucu mekanizmalar geliştirmiştir.
        Pentoz-Fosfat-Yolu|Glutatyonun rolü nedir ve özellikle hangi hücre tipinde önemli bir rol oynar?|Glutatyon, özellikle eritrositlerde hemoglobini hidrojen peroksitin zararlı etkilerinden korumak için kullanılan önemli bir tripeptittir.
        Pentoz-Fosfat-Yolu|Karaciğer mikrozomal sitokrom P450 monoksijenaz sisteminin önemi nedir ve bu sistemin aktivitesi için neden NADPH önemlidir? | Karaciğer mikrozomal sitokrom P450 monoksijenaz sistemi, steroidler, alkoller ve bazı ilaçlar gibi aromatik ve alifatik bileşiklerin hidroksilasyonunda önemli bir rol oynar. Bu sistemin aktivitesi için NADPH önemlidir çünkü NADPH, oksidatif reaksiyonlarda elektron verici olarak görev yaparak sitokrom P450'nin katalitik döngüsünü sürdürür.
        Pentoz-Fosfat-Yolu|P450 monoksijenaz sistemi hangi tür bileşiklerin hidroksilasyonunda en önemli rolü oynar? | P450 monoksijenaz sistemi, steroidler, alkoller ve bazı ilaçlar gibi aromatik ve alifatik bileşiklerin hidroksilasyonunda en önemli rolü oynar.
        Pentoz-Fosfat-Yolu|P450 monoksijenaz sisteminin gerçekleştirdiği oksidasyon reaksiyonları hangi amaçlara hizmet eder? | Bu oksidasyon reaksiyonları, ilaçlar ve yabancı bileşiklerin çözünebilir formlarına dönüştürülerek böbrek yoluyla kolaylıkla atılabilir hale getirilip detoksifiye edilmelerine hizmet eder.
        Pentoz-Fosfat-Yolu|Fruktozun en önemli besinsel kaynağı nedir? | Fruktozun en önemli besinsel kaynağı disakkarit olan sukrozdur.
        Pentoz-Fosfat-Yolu|Fruktoz, ayrıca hangi besinlerde bulunur? | Fruktoz, bal ve birçok meyvede mono sakkarit olarak bulunur.
        Pentoz-Fosfat-Yolu|Mısır şurubunda früktozun oranı nedir? | Mısır şurubunda früktoz yüksek oranda (%55 früktoz, %45 glikoz) bulunur.
        Pentoz-Fosfat-Yolu|Heksokinazın früktoz için özellikleri nelerdir? | Heksokinaz, früktoz için düşük afiniteye sahiptir.
        Pentoz-Fosfat-Yolu|Fruktokinazın früktoz fosforilasyonundaki rolü nedir ve hangi dokularda yüksek oranda bulunur? | Fruktokinaz, früktoz fosforilasyonunda majör rol oynar ve özellikle karaciğer, böbrek ve ince bağırsakta yüksek oranda yer alır.
        Pentoz-Fosfat-Yolu|Aldolaz izoenzimleri nelerdir, ve Aldolaz B hangi dokularda yoğun olarak bulunur? | Aldolaz izoenzimleri aldolaz A ve aldolaz B'dir. Aldolaz B, karaciğer, böbrek ve ince bağırsakta yoğun olarak bulunur ve sadece früktoz-1-fosfat üzerine etki eder.
        Pentoz-Fosfat-Yolu|Glikozun belirli dokulara girişi insüline bağlı mıdır? | Hayır, glikozun retine, lens, böbrekler, periferal sinir hücrelerine girişi insülinden bağımsızdır. Bu nedenle hiperglisemi durumunda bu hücrelere yüksek oranda glikoz verilir.
        Pentoz-Fosfat-Yolu|Aldoz redüktaz enzimi ne tür bir reaksiyona neden olur? | Aldoz redüktaz enzimi yüksek oranda sorbitol oluşumuna yol açar.
        Pentoz-Fosfat-Yolu|Sorbitol dehidrogenaz enzimi düşük veya yoksa hangi dokularda sorbitol birikir? | Sorbitol dehidrogenaz enzimi düşük veya yoksa (retina, lens, böbrekler ve periferal sinir hücreleri gibi) sorbitol hücrede birikir.
        Pentoz-Fosfat-Yolu|Galaktozun en önemli besinsel kaynağı nedir? | Galaktozun en önemli besinsel kaynağı süt ve sütlü ürünlerde bulunan laktozdur.
        """

        cards = [tuple(line.strip().split('|')) for line in questions_and_answers.split('\n') if line.strip()]
        return cards

    def extract_lessons(self):
        return list(set(card[0] for card in self.cards))

    def start_flashcards(self):
        try:
            print("Choose a lesson:")
            for i, lesson in enumerate(self.lessons, start=1):
                print(f"{i}-{lesson}")
            print(f"{len(self.lessons) + 1}-All Lessons")

            choice = input("Enter the number of the lesson you want to study: ")

            if choice.isdigit() and 1 <= int(choice) <= len(self.lessons) + 1:
                if int(choice) == len(self.lessons) + 1:
                    filtered_cards = self.cards
                else:
                    selected_lesson = self.lessons[int(choice) - 1]
                    filtered_cards = [card for card in self.cards if card[0] == selected_lesson]

                for card in filtered_cards:
                    print(f"Question: {card[1]}")
                    input("")
                    print(f"Answer: {card[2]}")
                    print("-" * 40)  # Separator line
                    input("")

            else:
                print("Invalid choice. Please enter a valid number.")

        except KeyboardInterrupt:
            print("\nExiting the program.")

if __name__ == "__main__":
    flashcards_app = Flashcards()
    flashcards_app.start_flashcards()