template: templates/tr/resources/faqTemplate.ptl
title: PyCharm Kurulumu

[TOC]

<p id="osspiel" class="alert alert-warning"></p>

CS Bridge boyunca kod yazmak için [PyCharm](https://www.jetbrains.com/pycharm/) adında bir uygulama kullanacaksınız. PyCharm IDE, veya _Bütünleşik Geliştirme Ortamı (Integrated Development Environment)_, türünde bir uygulamadır. Yani PyCharm kullanarak kod dosyalarınızı inceleyebilir, değiştirebilir, programlarınızı çalıştırabilir ve hata ayıklama (debugging) arayüzünü kullanarak programlarınız nasıl çalıştığını kolaylıkla inceleyebilirsiniz. PyCharm Python için geliştirilmiş en popüler IDElerden biridir ve endüstride yaygın olarak kullanılır. Bu dökümanı PyCharm kurulumunda size yol göstermek için oluşturduk. 

<div class="chromeosonly">
    <h2>Chromebook Installation Instructions</h2>
    <p class="alert alert-info">We've detected that you are using a Chromebook.  The Chromebook installation instructions are different than for other platforms - <b>please use the following steps instead to install python and PyCharm and skip the install sections below.</b>  It might seem a little less straightforward than the regular installation but we are here to help you every step of the way!</p>
    <p>The main steps will involve following along with <a href="https://www.youtube.com/watch?v=sykiO1A7J1g">this video</a>. You will essentially:</p>
    <ol>
        <li>Turn on linux (beta)</li>
        <li>Install <code>python3</code> packages via terminal</li>
        <li>Run pycharm for the first time via terminal</li>
        <li>Download an app shortcut manager that allows you to access pycharm by clicking on a button (as opposed to opening terminal every time)</li>
    </ol>
    <p>Some things not in the video:</p>
    <ul>
        <li>A few scary warnings you might see during installation, that you can ignore.</li>
        <li>Run <code>sudo apt-get install python3-tk</code> from the terminal after you follow the video to install a library.</li>
    </ul>
    <p>Once you have followed these steps, jump down to <a href="#testing-pycharm">Testing Pycharm</a> to test your installation.</p>
</div>

## Python Kurulumu
Bilgisayarınızda Python programları çalıştırabilmek için öncelikle _Python Yorumlayıcısı (Interpreter)_ yüklemeniz gerekiyor. Python Yorumlayıcısı `.py` türündeki Python kod dosyalarını okuyup onları bilgisayarınızın uygulayabileceği komutlara dönüştürmekten sorumlu bir programdır. Python'u aşağıda işletim sisteminize uygun linkten indirebilirsiniz:

<ul>
    <li class="maconly">
        <a href="https://www.python.org/ftp/python/3.8.1/python-3.8.1-macosx10.9.pkg">
            MacOS
        </a>
    </li>
    <li class="winonly">
        <a href="https://www.python.org/ftp/python/3.8.1/python-3.8.1-amd64.exe">
            Windows 64-bit
        </a>
        (Windows'unuzun 32-bit mi yoksa 64-bit mi olduğunu bilmiyorsanız <a href="https://support.microsoft.com/tr-tr/help/15056/windows-32-64-bit-faq">bu sayfayı</a> ziyaret edebilirsiniz.)
    </li>
    <li class="winonly">
        <a href="https://www.python.org/ftp/python/3.8.1/python-3.8.1.exe">
            Windows 32-bit
        </a>
        (Windows'unuzun 32-bit mi yoksa 64-bit mi olduğunu bilmiyorsanız <a href="https://support.microsoft.com/tr-tr/help/15056/windows-32-64-bit-faq">bu sayfayı</a> ziyaret edebilirsiniz.)
    </li>
</ul>

<h3 class="maconly" data-toc-skip>Mac için Python Kurulumu</h3>
<p class="note maconly">
    Tüm mac bilgisayarlar Python'un eski bir versiyonunu içerirler. Fakat CS Bridge'de Python'un en yeni versiyonunu kullanacağız. Bu yüzden zaten bilgisayarınızda Python olduğunu düşünüyorsanız bile bu talimatları uygulayın. Python'u Mac'inize kurmak için basitçe indirdiğiniz kurulum dosyasını çalıştırın ve talimatları uygulayın. Kurulum boyunca varsayılan ayarları kullanabilirsiniz. 
</p>

<h3 class="winonly" data-toc-skip>Windows İçin Python Kurulumu</h3>
<p class="winonly">
    İndirdiğiniz kurulum dosyasını açın. Kuruluma başlamadan önce "Add Python 3.8 to PATH" yazan seçeneği işaretleyin. Bu seçeneği işaretlemeniz Python'u kolaylıkla çalıştırmanız için önemlidir ve seçmediğiniz durumda sorunlara neden olacaktır. <b>Bu seçeneğin işaretli olduğundan emin olduktan sonra</b> kuruluma normal şekilde devam edebilirsiniz.
</p>

---

## PyCharm Kurulumu ve Kontrolü

### Kurulum

Öncelikle PyCharm Community versiyonunun en son versiyonunu indirin ve kurun.

<ul>
    <li class="maconly">
        <a href="https://download.jetbrains.com/python/pycharm-community-2020.1.4.dmg">
            MacOS
        </a>
        (İndirdiğiniz <code>.dmg</code> dosyasını açın ve PyCharm programını Uygulamalar klasörüne sürekleyin)
    </li>
    <li class="winonly">
        <a href="https://download.jetbrains.com/python/pycharm-community-2020.1.4.exe">
            Windows
        </a>
        (İndirdiğiniz <code>.exe</code> dosyasını çalıştırın ve PyCharm kurulumunu varsayılan seçenekleri kullanarak tamamlayın.)
    </li>
</ul>

Pycharm kurulumunu tamamladıktan sonra aşağıdaki gibi gözüken bir ekranla karşılaşacaksınız:

<div class="row">
    <div class="col-md-2"></div>
    <div class="col-md-8">
        <img
            src="{{pathToRoot}}img/pycharm/welcomescreen.png"
            style="width:100%"
            alt="PyCharm Welcome Screen"
        />
    </div>
</div>
<br />

'Configure' butonuna tıklayın ve PyCharm'ın ayarlarını açın, buna benzer bir pencere görmelisiniz:
{: #configure_interpreter}

<div class="row">
    <div class="col-md-2"></div>
    <div class="col-md-8">
        <div class="maconly">
            <img
                src="{{pathToRoot}}img/pycharm/welcomescreen-config.png"
                style="width:100%"
                alt="PyCharm Welcome Screen, with 'Configure->Preferences' highlighted"
            />
        </div>
        <div class="winonly">
            <img
                src="{{pathToRoot}}img/pycharm/welcomescreen-config-win.png"
                style="width:100%"
                alt="PyCharm Welcome Screen, with 'Configure->Preferences' highlighted"
            />
        </div>
    </div>
</div>
<br />

'Preferences' penceresinde, 'Project Interpreter' bölümünü seçin, seçeneklerin bulunduğu aşağıya doğru açılan menüye tıklayın, 'Show All' yazan seçeneği seçin:
{: #setinterpreter}

<div class="row">
    <div class="col-md-2"></div>
    <div class="col-md-8">
        <img
            src="{{pathToRoot}}img/pycharm/preferences-showinterpreters.png"
            style="width:100%"
            alt="PyCharm Preferences Window, in the 'Project Interpreter' Pane, with 'Show All' highlighted in the dropdown menu" />
    </div>
</div>
<br />

Açılan pencerede sağ üst köşede bulunan artı ikonuna tıklayın:

<div class="row">
    <div class="col-md-2"></div>
    <div class="col-md-8">
        <div class="maconly">
            <img src="{{pathToRoot}}img/pycharm/addnewinterpreter.png"
                style="width:100%"
                alt="PyCharm Interpreter List, with the plus button in the bottom left circled" />
        </div>
        <div class="winonly">
            <img src="{{pathToRoot}}img/pycharm/addnewinterpreter-win.png"
            style="width:100%"
            alt="PyCharm Interpreter List, with the plus button in the top right circled" />
        </div>
    </div>
</div>
<br />

Açılan 'Add Python Interpreter' penceresinde sağdaki seçeneklerden 'System Interpreter' yazanı seçin. Bilgisayarınızda Python'un başka versiyonları yüklü değilse Python 3.8 zaten seçili olabilir. Eğer seçili değilse veya başka bir Python versiyonu seçiliyse menüden Python 3.8'i seçin ve 'OK' butonuna tıklayın. Daha sonra tekrar 'OK' butonuna tıklayın.

<div class="row">
    <div class="col-md-2"></div>
    <div class="col-md-8">
        <img src="{{pathToRoot}}img/pycharm/addsysteminterpreter.png"
            style="width:100%"
            alt="Adding the system interpreter in PyCharm" />
    </div>
</div>
<br />

Bu şekilde görünen bir pencerede olmalısınız (listenin içerikleri değişiklik gösterebilir):

<div class="row">
    <div class="col-md-2"></div>
    <div class="col-md-8">
        <img src="{{pathToRoot}}img/pycharm/interpreterafterselection.png"
            style="width:100%"
            alt="Interpreter window after selecting system interpreter" />
    </div>
</div>
<br />

Tekrar 'OK' butonuna tıklayın. Yeniden ilk karşılaştığınız ekranda olmasınız. Artık PyCharm kurulumunu test etmeye hazırsınız!

---

### PyCharm Kurulumunu Test Etmek

PyCharm Python programlarını projeler olarak modeller. Her proje bir veya birden fazla Python (`.py`) dosyası ve programınızda kullanmak istediğiniz resim, metin dosyası gibi ekstra dosyaları içerir. PyCharm proje yapısına alışmanıza yardımcı olmak ve Python projelerinizi nasıl çalıştırabileceğinizi göstermek için örnek bir proje hazırladık. Bu projeyi [buradan]({{pathToRoot}}starter/pycharm_intro.zip)indirebilirsiniz. PyCharm çalışmaya başlamak için bu projeyi indirin <span style="display: inline-block;" class="winonly">(Windows kullanıyorsanız önce indirdiğiniz sıkıştırılmış projeyi açmanız gerekiyor. Bunun için dosya gezgininden indirdiğiniz projeyi bulun ve sağ tıklayıp 'Tümünü Ayıkla' seçeneğini seçin)</span> ve indirdiğiniz projeyi PyCharm ile açın. Projeyi açmak için gördüğünüz ilk ekranda 'Open' seçeneğini seçin ve indirdiğiniz dosya konumunu <span style="display: inline-block;" class="winonly">(Windows kullanıyorsanız projeyi ayıkladığınız konumu)</span> seçin. **PyCharm ile proje açarken sadece değişiklik yapmak istediğiniz dosyayı açmak yerine her zaman _değişiklik yapmak istediğiniz dosyaları içen klasörü_ açın.** Projeyi açtıktan sonra aşağıda gördüğünüz gibi bir pencereyle karşılaşacaksınız:

<div class="row">
    <div class="col-md-2"></div>
    <div class="col-md-8">
        <img src="{{pathToRoot}}img/pycharm/pycharmblank.png"
            style="width:100%"
            alt="Blank PyCharm Window" />
    </div>
</div>
<br />

Sol üstten 'Project' menüsünü açın.  Açılan dosya gezginini kullanarak `intro.py` dosyasını açın:

<div class="row">
    <div class="col-md-2"></div>
    <div class="col-md-8">
        <img src="{{pathToRoot}}img/pycharm/pycharmeditor.png"
            style="width:100%"
            alt="PyCharm Editor" />
    </div>
</div>
<br />

Editörde gördüğünüz kodu henüz okumak veya anlamak zorunda değilsiniz (CS Bridge'den sonra bunu kolaylıkla yapabileceksiniz!).  Program boyunca kod yazmak için bu editörü kullanacaksınız. Programı çalıştırmak için sol alt köşedeki 'Terminal' butonuna tıklayın. Bu butona tıkladığınızda editörünüzün altında bir terminal penceresi açılacak:

<div class="row">
    <div class="col-md-2"></div>
    <div class="col-md-8">
        <img src="{{pathToRoot}}img/pycharm/pycharmterminal.png"
             style="width:100%"
             alt="PyCharm Terminal" />
    </div>
</div>
<br />

Terminallerin ne olduğundan program boyunca daha detaylı bahsedeceğiz, şimdilik Python programlarını terminal kullanarak çalıştırabileceğinizi bilmeniz yeterli. İlk Python programınızı çalıştırmak için aşağıda gördüğünüz komutu terminalize yazın ve enter'a basın:

<div class="text-center">
    <code><span class="launcher">python3</span> intro.py</code>
</div>
<br />

Aşağıdakine benzer bir çıktı görmelisiniz:

<div class="maconly">
    <img src="{{pathToRoot}}img/pycharm/firstrun.png"
        style="width:100%"
        alt="First run output" />
</div>
<div class="winonly">
    <img src="{{pathToRoot}}img/pycharm/firstrun-win.png"
        style="width:100%"
        alt="First run output" />
</div>
<br />

Şimdi terminale aşağıda gördüğün komutu yaz ve çalıştır:

<div class="text-center">
    <code><span class="launcher">python3</span> intro.py &lt;SENIN ADIN&gt; </code>
</div>
<br />

Örneğin adın Papatya ise terminale <code><span class="launcher">python3</span> intro.py Papatya</code> yazmalısın.  Eğer istersen tam adını da yazabilirsin. Aşağıdakine benzer bir çıktı görmelisin:

<div class="maconly">
    <img src="{{pathToRoot}}img/pycharm/secondrun.png"
        style="width:100%"
        alt="Second run output" />
</div>
<div class="winonly">
    <img src="{{pathToRoot}}img/pycharm/secondrun-win.png"
        style="width:100%"
        alt="Second run output" />
</div>
<br />

Tebrikler! Başarıyla Python ve PyCharm kurulumunu tamamladın.

### Graphics Paketini Yüklemek
CS Bridge'de kullanacağımız grafik kütüphanesi Python'u yüklediğinizde otomatik olarak yüklenmiş olmalı.  Fakat bu kütüphane çalışmak için `Pillow` adında resimleri modifiye etmek ve ekran üzerinde çizmek için kullanılan bir pakete ihtiyaç duyuyor. `Pillow`'u indirmek için bir terminal penceresi açın (PyCharm'ın içindeki Terminal sekmesini kullanabilirsiniz) ve aşağıdaki komutu girin (Python'da paket adları büyük/küçük harfe duyarlıdır. `Pillow`'u yazarken ilk harfin büyük olmasına dikkat edin.):

<div class="text-center">
    <code><span class="launcher">python3</span> -m pip install Pillow==7.1.1</code>
</div>
<br />

"Successfully installed Pillow-7.1.1" benzer bir çıktıyla karşılaştıysanız `Pillow`'u başarıyla yüklediniz ve kodlamaya başlamaya hazırsınız!

---

## Sıkça Sorulan Sorular

### Başka bir Python versiyonu kullanabilir miyim?
Python 3.8 kullanmanızı ısrarla öneriyoruz. Eğer zaten başka bir Python versiyonuna sahipsen Python 3.8'i de paralel olarak bilgisayarına yükleyebilirsin. Program boyunca kullancağımız örnek ve çözümler Python 3.8 kullandığınızı varsayarak hazırlandı.

### PyCharm harici başka bir editör kullanabilir miyim?
Eğer hali hazırda zaten kullandığın ve hakim olduğun bir editör varsa onu tercih edebilirsin.  Fakat ekibimiz sadece PyCharm konusunda karşılaştığınız sorunlarda sizlere destek olacak.  Hangi editörü kullanırsan kullan projelerde bulundan konfigürasyon dosyalarında değişiklik yapmamalısın. 

<h3 data-toc-text="Can't open file">
    Kodumu çalıştırmaya çalıştığımda <code>can't open file intro.py: No such file or directory</code> hatası alıyorum. Bu ne anlama geliyor?
</h3>

Bu hatanın nedeni genellikle PyCharm ile yanlış dosya veya klasörü açmak. Öncelikle `intro.py` dosyasını içinde bulunduran `pycharm_intro` klasörünü açtığından emin ol.  Direkt olarak `intro.py` dosyasını veya `pycharm_intro` klasörünü içeren başka bir klasör açmadığını kontrol et. 

Bu hatayı düzeltmek için PyCharm'da sol üst köşedeki 'File' menüsünü aç ve 'Open' seçeğine tıkla. Sonra açılan dosya gezgini üstünden doğru `pycharm_intro` klasörünü bul ve aç.

Doğru klasörü açtığını kontrol etmek için terminale <span class="maconly"><code>ls</code> (ilk harf küçük 'L' harfi)</span><span class="winonly"><code>dir</code></span> komutunu yaz ve çalıştır. Bu komut sana bulunduğun klasörde bulunan tüm dosya ve klasörleri listeyelecek.<code>intro.py</code> dosyasının komutun çıktıları içinde bulunduğunu kontrol et.

<h3 data-toc-text="No Python Interpeter Configured">
    Editörü açtığımda 'No Python Interpreter configured for the project' mesajı alıyorum. Ne yapmalıyım?
</h3>

Bu muhtemelen PyCharm'da Python Yorumlayıcısı (Interpreter) seçerken bir sorun yaşadığın anlamına geliyor. Bunu düzeltmek için çıkan mesajdaki 'Configure Python Interpreter' seçeneğine tıkla ve [burada anlatılan](#setinterpreter) adımları izle. 'PyCharm Kurulumunu Test Etmek' bölümüne gelene kadar tüm adımları gerçekleştirmelisin.

<h3 data-toc-text="The default interactive shell is now zsh">
    Mac kullanıyorum ve terminali açtığımda <code>The default interactive shell is now zsh.
    To update your account to use zsh, please run `chsh -s /bin/zsh</code> mesajıyla karşılaşıyorum.  Ne yapmalıyım? 
</h3>

Bu zararsız bir bilgilendirme mesajı. Herhangi bir şey yapmana gerek yok, bu mesajı görmezden gelebilirsin.

<h3 data-toc-text="PyCharm won't open on a Mac">
    Mac kullanıyorum ve PyCharm'ı çalıştıramıyorum. Ne yapmalıyım?
</h3>

MacOS'un eski bir versiyonunu kullanıyor olabilirsin. PyCharm'ın [bu versiyonunu](https://download.jetbrains.com/python/pycharm-community-2018.3.7.dmg") indirmeyi dene.

<h3 data-toc-text="JetBrains Runtime 11 & Windows 32-bit">
    "This installation contains JetBrains Runtime 11 which does not support Microsoft Windows 32-bit version" hatası alıyorum. Ne yapmalıyım?
</h3>

PyCharm'ın [bu versiyonunu](https://download.jetbrains.com/python/pycharm-community-2018.3.7.exe) indirmeyi dene.


__Sıkça sorulan sorular sizden gelen sorular doğrultusunda güncellenecektir.__

<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-74362126-1', 'auto');
  ga('send', 'pageview');
</script>

<script>
    function setWindows() {
        toggle("maconly", "none");
        toggle("chromeosonly", "none");
        toggle("winonly", "inline-block");

        const launchers = document.getElementsByClassName("launcher");
        for (let i = 0; i < launchers.length; i++) {
            launchers[i].innerHTML = 'py';
        }

        const osSpiel = document.getElementById('osspiel');
        osSpiel.innerHTML = "We've detected you're using a Windows computer. &nbsp; &nbsp; <a href='#' onclick='setMacOS()'>I'm using a Mac</a> ||  <a href='#' onclick='setChromeOS()'>I'm using a Chromebook</a>."
    }

    function setMacOS() {
        toggle("maconly", "inline-block");
        toggle("winonly", "none");
        toggle("chromeosonly", "none");

        const launchers = document.getElementsByClassName("launcher");
        for (let i = 0; i < launchers.length; i++) {
            launchers[i].innerHTML = 'python3';
        }

        const osSpiel = document.getElementById('osspiel');
        osSpiel.innerHTML = "We've detected you're using a Mac. &nbsp; &nbsp; <a href='#' onclick='setWindows()'>I'm using a Windows Machine</a> ||  <a href='#' onclick='setChromeOS()'>I'm using a Chromebook</a>.";
    }

    function setChromeOS() {
        toggle("chromeosonly", "inline-block");
        toggle("maconly", "none");
        toggle("winonly", "none");

        const launchers = document.getElementsByClassName("launcher");
        for (let i = 0; i < launchers.length; i++) {
            launchers[i].innerHTML = 'python3';
        }

        const osSpiel = document.getElementById('osspiel');
        osSpiel.innerHTML = "We've detected you're using a Chromebook. &nbsp; &nbsp; <a href='#' onclick='setWindows()'>I'm using a Windows Machine</a> ||  <a href='#' onclick='setMacOS()'>I'm using a Mac</a>.";
    }

    function setUnknownOS() {
        toggle("chromeosonly", "none");
        toggle("maconly", "none");
        toggle("winonly", "none");
        const osSpiel = document.getElementById('osspiel');
        osSpiel.innerHTML = "We weren't able to detect what operating system you're using. Click <a href='#' onclick='setMacOS()'> here </a> if you're using a Mac, <a href='#' onclick='setWindows()'> here </a> if you're using a Windows machine, or <a href='#' onclick='setChromeOS()'>here </a> if you're using a Chromebook."
    }

    function getOS() {
        if (navigator.appVersion.indexOf("Win") != -1) return "Windows"
        if (navigator.appVersion.indexOf("Mac") != -1) return "MacOS";
        if (navigator.appVersion.indexOf("CrOS") != -1) return "ChromeOS";
        return "Unknown";
    }

    function setOS() {
        const os = getOS();
        if (os === "MacOS") setMacOS();
        else if (os === "Windows") setWindows();
        else if (os == "ChromeOS") setChromeOS();
        else setUnknownOS();
    }

    function toggle(className, displayState) {
        var elements = document.getElementsByClassName(className)

        for (var i = 0; i < elements.length; i++) {
            elements[i].style.display = displayState;
        }
    }

    window.onload = setOS;
</script>
